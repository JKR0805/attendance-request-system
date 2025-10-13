"""
Configuration Template for Attendance System
Copy this file to config.py and update with your values
"""

# Database Configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'database': 'attendance_system',
    'user': 'root',
    'password': 'your_mysql_password_here'
}

# Flask Configuration
SECRET_KEY = 'change_this_to_a_random_secret_key_in_production'

# Upload Configuration
UPLOAD_FOLDER = 'uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'}

# Application Configuration
DEBUG = True  # Set to False in production
HOST = '0.0.0.0'
PORT = 5000

# Email Configuration (for future enhancement)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your_email@gmail.com'
MAIL_PASSWORD = 'your_email_password'

# Session Configuration
SESSION_COOKIE_SECURE = False  # Set to True when using HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
PERMANENT_SESSION_LIFETIME = 3600  # 1 hour in seconds

# Security Configuration (for production)
# SECURITY_PASSWORD_SALT = 'your_password_salt_here'
# WTF_CSRF_ENABLED = True
# WTF_CSRF_SECRET_KEY = 'your_csrf_secret_key'

# Logging Configuration
LOG_FILE = 'app.log'
LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR, CRITICAL
