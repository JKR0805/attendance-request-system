"""
Change Password Script
Allows you to change passwords for any user in the system
"""

from db_config import db
import hashlib

def hash_password(password):
    """Hash password using MD5"""
    return hashlib.md5(password.encode()).hexdigest()

def change_student_password():
    """Change password for a student"""
    print("\n📝 Change Student Password")
    print("-" * 40)
    
    email = input("Enter student email: ").strip()
    
    # Check if student exists
    student = db.execute_query(
        "SELECT student_id, name FROM students WHERE email = %s",
        (email,),
        fetch=True
    )
    
    if not student:
        print("❌ Student not found!")
        return
    
    print(f"✅ Found student: {student[0]['name']}")
    
    new_password = input("Enter new password: ").strip()
    confirm_password = input("Confirm new password: ").strip()
    
    if new_password != confirm_password:
        print("❌ Passwords don't match!")
        return
    
    if len(new_password) < 6:
        print("❌ Password must be at least 6 characters!")
        return
    
    # Update password
    hashed = hash_password(new_password)
    result = db.execute_query(
        "UPDATE students SET password = %s WHERE email = %s",
        (hashed, email)
    )
    
    if result is not None:
        print("✅ Password updated successfully!")
    else:
        print("❌ Failed to update password!")

def change_user_password():
    """Change password for coordinator/HOD"""
    print("\n📝 Change Coordinator/HOD Password")
    print("-" * 40)
    
    email = input("Enter coordinator/HOD email: ").strip()
    
    # Check if user exists
    user = db.execute_query(
        "SELECT user_id, name, role FROM users WHERE email = %s",
        (email,),
        fetch=True
    )
    
    if not user:
        print("❌ User not found!")
        return
    
    print(f"✅ Found user: {user[0]['name']} ({user[0]['role'].upper()})")
    
    new_password = input("Enter new password: ").strip()
    confirm_password = input("Confirm new password: ").strip()
    
    if new_password != confirm_password:
        print("❌ Passwords don't match!")
        return
    
    if len(new_password) < 6:
        print("❌ Password must be at least 6 characters!")
        return
    
    # Update password
    hashed = hash_password(new_password)
    result = db.execute_query(
        "UPDATE users SET password = %s WHERE email = %s",
        (hashed, email)
    )
    
    if result is not None:
        print("✅ Password updated successfully!")
    else:
        print("❌ Failed to update password!")

def list_all_users():
    """List all users in the system"""
    print("\n👥 All System Users")
    print("=" * 60)
    
    # Students
    students = db.execute_query(
        "SELECT name, email, department FROM students ORDER BY name",
        fetch=True
    )
    
    print("\n📚 STUDENTS:")
    print("-" * 60)
    if students:
        for s in students:
            print(f"  {s['name']:<30} {s['email']:<30} {s['department']}")
    else:
        print("  No students found")
    
    # Coordinators
    coordinators = db.execute_query(
        "SELECT name, email, department FROM users WHERE role = 'coordinator' ORDER BY name",
        fetch=True
    )
    
    print("\n👨‍💼 COORDINATORS:")
    print("-" * 60)
    if coordinators:
        for c in coordinators:
            print(f"  {c['name']:<30} {c['email']:<30} {c['department']}")
    else:
        print("  No coordinators found")
    
    # HODs
    hods = db.execute_query(
        "SELECT name, email, department FROM users WHERE role = 'hod' ORDER BY name",
        fetch=True
    )
    
    print("\n👔 HODs:")
    print("-" * 60)
    if hods:
        for h in hods:
            print(f"  {h['name']:<30} {h['email']:<30} {h['department']}")
    else:
        print("  No HODs found")
    
    print("=" * 60)

def main():
    """Main menu"""
    print("=" * 60)
    print("PASSWORD MANAGEMENT SYSTEM")
    print("=" * 60)
    
    if not db.connect():
        print("❌ Failed to connect to database!")
        return
    
    print("✅ Connected to database\n")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Change Student Password")
        print("2. Change Coordinator/HOD Password")
        print("3. List All Users")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            change_student_password()
        elif choice == '2':
            change_user_password()
        elif choice == '3':
            list_all_users()
        elif choice == '4':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")
    
    db.disconnect()

if __name__ == "__main__":
    main()
