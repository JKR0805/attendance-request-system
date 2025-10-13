"""
Database Configuration Module
Handles MySQL database connections and operations
"""

import mysql.connector
from mysql.connector import Error
import hashlib

class DatabaseConfig:
    """Database connection and operations handler"""
    
    def __init__(self, host='localhost', database='attendance_system', 
                 user='root', password='root'):
        """
        Initialize database configuration
        
        Args:
            host: MySQL server host
            database: Database name
            user: MySQL username
            password: MySQL password
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                return True
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return False
        return False
    
    def disconnect(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def execute_query(self, query, params=None, fetch=False):
        """
        Execute a SQL query
        
        Args:
            query: SQL query string
            params: Query parameters (tuple)
            fetch: Whether to fetch results (for SELECT queries)
            
        Returns:
            For SELECT: List of results
            For INSERT: Last inserted ID
            For UPDATE/DELETE: Number of affected rows
        """
        try:
            if not self.connection or not self.connection.is_connected():
                self.connect()
            
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            
            if fetch:
                result = cursor.fetchall()
                cursor.close()
                return result
            else:
                self.connection.commit()
                last_id = cursor.lastrowid
                affected = cursor.rowcount
                cursor.close()
                return last_id if last_id else affected
                
        except Error as e:
            print(f"Error executing query: {e}")
            if self.connection:
                self.connection.rollback()
            return None
    
    @staticmethod
    def hash_password(password):
        """
        Hash password using MD5
        
        Args:
            password: Plain text password
            
        Returns:
            Hashed password string
        """
        return hashlib.md5(password.encode()).hexdigest()
    
    def verify_student_login(self, email, password):
        """
        Verify student login credentials
        
        Args:
            email: Student email
            password: Plain text password
            
        Returns:
            Student details dict if successful, None otherwise
        """
        hashed_pwd = self.hash_password(password)
        query = """
            SELECT student_id, name, department, email, contact 
            FROM students 
            WHERE email = %s AND password = %s
        """
        result = self.execute_query(query, (email, hashed_pwd), fetch=True)
        return result[0] if result else None
    
    def verify_user_login(self, email, password, role):
        """
        Verify coordinator/HOD login credentials
        
        Args:
            email: User email
            password: Plain text password
            role: 'coordinator' or 'hod'
            
        Returns:
            User details dict if successful, None otherwise
        """
        hashed_pwd = self.hash_password(password)
        query = """
            SELECT user_id, name, role, department, email 
            FROM users 
            WHERE email = %s AND password = %s AND role = %s
        """
        result = self.execute_query(query, (email, hashed_pwd, role), fetch=True)
        return result[0] if result else None
    
    def create_student(self, name, department, contact, email, password):
        """Create new student account"""
        hashed_pwd = self.hash_password(password)
        query = """
            INSERT INTO students (name, department, contact, email, password)
            VALUES (%s, %s, %s, %s, %s)
        """
        return self.execute_query(query, (name, department, contact, email, hashed_pwd))
    
    def create_request(self, student_id, subject, description, start_time, 
                      end_time, contact, attachment_path=None):
        """Create new attendance request"""
        query = """
            INSERT INTO requests (student_id, subject, description, start_time, 
                                end_time, contact, attachment_path)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (student_id, subject, description, start_time, end_time, 
                 contact, attachment_path)
        return self.execute_query(query, params)
    
    def get_requests_by_status(self, status):
        """Get all requests with specific status"""
        query = """
            SELECT r.*, s.name as student_name, s.department, s.email 
            FROM requests r
            JOIN students s ON r.student_id = s.student_id
            WHERE r.status = %s
            ORDER BY r.created_at DESC
        """
        return self.execute_query(query, (status,), fetch=True)
    
    def get_student_requests(self, student_id):
        """Get all requests for a specific student"""
        query = """
            SELECT * FROM requests 
            WHERE student_id = %s
            ORDER BY created_at DESC
        """
        return self.execute_query(query, (student_id,), fetch=True)
    
    def update_request_status(self, request_id, status):
        """Update request status"""
        query = "UPDATE requests SET status = %s WHERE request_id = %s"
        return self.execute_query(query, (status, request_id))
    
    def create_approval(self, request_id, approver_role, approver_name, 
                       decision, remarks):
        """Create approval record"""
        query = """
            INSERT INTO approvals (request_id, approver_role, approver_name, 
                                 decision, remarks)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (request_id, approver_role, approver_name, decision, remarks)
        return self.execute_query(query, params)
    
    def get_request_approvals(self, request_id):
        """Get all approvals for a request"""
        query = """
            SELECT * FROM approvals 
            WHERE request_id = %s
            ORDER BY decision_time ASC
        """
        return self.execute_query(query, (request_id,), fetch=True)
    
    def get_request_by_id(self, request_id):
        """Get request details by ID"""
        query = """
            SELECT r.*, s.name as student_name, s.department, s.email 
            FROM requests r
            JOIN students s ON r.student_id = s.student_id
            WHERE r.request_id = %s
        """
        result = self.execute_query(query, (request_id,), fetch=True)
        return result[0] if result else None


# Create a global database instance
db = DatabaseConfig()
