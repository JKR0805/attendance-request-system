"""
Database Reset Script
This script will drop all tables and recreate them with fresh sample data.
USE WITH CAUTION - This will delete all existing data!
"""

import sys
from db_config import db

def reset_database():
    """Drop all tables and recreate with fresh data"""
    
    print("=" * 60)
    print("DATABASE RESET SCRIPT")
    print("=" * 60)
    print("\n⚠️  WARNING: This will DELETE ALL DATA in the database!")
    print("This includes:")
    print("  - All student accounts")
    print("  - All requests")
    print("  - All approvals")
    print("  - All user accounts (except what's in SQL file)")
    print("\n")
    
    confirm = input("Are you sure you want to continue? (type 'YES' to confirm): ")
    
    if confirm != 'YES':
        print("\n❌ Reset cancelled.")
        return
    
    print("\n🔄 Connecting to database...")
    if not db.connect():
        print("❌ Failed to connect to database!")
        return
    
    print("✅ Connected to database")
    
    try:
        # Drop tables in correct order (due to foreign keys)
        print("\n🗑️  Dropping existing tables...")
        
        tables = ['approvals', 'requests', 'students', 'users']
        for table in tables:
            print(f"   Dropping table: {table}")
            db.execute_query(f"DROP TABLE IF EXISTS {table}")
        
        print("✅ All tables dropped")
        
        # Recreate tables
        print("\n🏗️  Creating tables...")
        
        # Students table
        print("   Creating students table...")
        db.execute_query("""
            CREATE TABLE students (
                student_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                department VARCHAR(100) NOT NULL,
                contact VARCHAR(15) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Users table
        print("   Creating users table...")
        db.execute_query("""
            CREATE TABLE users (
                user_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                role ENUM('coordinator', 'hod') NOT NULL,
                department VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Requests table
        print("   Creating requests table...")
        db.execute_query("""
            CREATE TABLE requests (
                request_id INT PRIMARY KEY AUTO_INCREMENT,
                student_id INT NOT NULL,
                subject VARCHAR(200) NOT NULL,
                description TEXT NOT NULL,
                start_time DATETIME NOT NULL,
                end_time DATETIME NOT NULL,
                contact VARCHAR(15) NOT NULL,
                attachment_path VARCHAR(255),
                status ENUM('pending', 'approved_by_coordinator', 'approved', 'rejected') DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
            )
        """)
        
        # Approvals table
        print("   Creating approvals table...")
        db.execute_query("""
            CREATE TABLE approvals (
                approval_id INT PRIMARY KEY AUTO_INCREMENT,
                request_id INT NOT NULL,
                approver_role ENUM('coordinator', 'hod') NOT NULL,
                approver_name VARCHAR(100) NOT NULL,
                decision ENUM('approved', 'rejected') NOT NULL,
                remarks TEXT,
                decision_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (request_id) REFERENCES requests(request_id) ON DELETE CASCADE
            )
        """)
        
        # Create indexes
        print("   Creating indexes...")
        db.execute_query("CREATE INDEX idx_requests_status ON requests(status)")
        db.execute_query("CREATE INDEX idx_requests_student ON requests(student_id)")
        db.execute_query("CREATE INDEX idx_approvals_request ON approvals(request_id)")
        
        print("✅ All tables created")
        
        # Insert sample data
        print("\n📝 Inserting sample data...")
        
        # Sample students (password: password)
        print("   Adding sample students...")
        db.execute_query("""
            INSERT INTO students (name, department, contact, email, password) VALUES
        ('DOOD1', 'Computer Science', '9876543210', 'dood1@student.com', '5f4dcc3b5aa765d61d8327deb882cf99'),
        ('DOOD2', 'Information Technology', '9876543211', 'dood2@student.com', '5f4dcc3b5aa765d61d8327deb882cf99'),
        ('DOOD3', 'Electronics', '9876543212', 'dood3@student.com', '5f4dcc3b5aa765d61d8327deb882cf99')
        """)
        
        # Sample users (password: password)
        print("   Adding sample coordinators/HODs...")
        db.execute_query("""
            INSERT INTO users (name, role, department, email, password) VALUES
            ('COORD1', 'coordinator', 'Computer Science', 'coordinator@college.com', '5f4dcc3b5aa765d61d8327deb882cf99'), 
            ('HOD1', 'hod', 'Computer Science', 'hod@college.com', '5f4dcc3b5aa765d61d8327deb882cf99')
        """)
        
        # Sample requests
        print("   Adding sample requests...")
        db.execute_query("""
            INSERT INTO requests (student_id, subject, description, start_time, end_time, contact, status) VALUES
            (1, 'Workshop Attendance', 'Need permission to attend Python Workshop at Tech Hub', '2025-10-15 09:00:00', '2025-10-15 17:00:00', '9876543210', 'pending'),
            (2, 'Hackathon Participation', 'Participating in National Level Hackathon', '2025-10-20 08:00:00', '2025-10-22 18:00:00', '9876543211', 'pending')
        """)
        
        print("✅ Sample data inserted")
        
        print("\n" + "=" * 60)
        print("✅ DATABASE RESET COMPLETE!")
        print("=" * 60)
        print("\n📋 Default Login Credentials:")
        print("-" * 60)
        print("Student:")
        print("  Email: dood1@student.com")
        print("  Password: password")
        print("\nCoordinator:")
        print("  Email: coordinator@college.com")
        print("  Password: password")
        print("\nHOD:")
        print("  Email: hod@college.com")
        print("  Password: password")
        print("-" * 60)
        print("\n💡 Tip: You can now change passwords using change_password.py")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error during reset: {e}")
        print("Database may be in an inconsistent state!")
        return
    
    finally:
        db.disconnect()

if __name__ == "__main__":
    reset_database()
