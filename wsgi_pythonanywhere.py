"""
WSGI Configuration for PythonAnywhere
Attendance Request & Approval System

INSTRUCTIONS:
1. Copy this entire file content
2. In PythonAnywhere Web tab, click WSGI configuration file link
3. Delete ALL existing content
4. Paste this content
5. Replace 'yourusername' on line 7 with YOUR PythonAnywhere username
6. Save the file
7. Reload your web app

Example: If your username is 'john123', change line 7 to:
project_home = '/home/john123/attendance-request-system'
"""

import sys
import os

# Add your project directory to the sys.path
# REPLACE 'yourusername' WITH YOUR ACTUAL PYTHONANYWHERE USERNAME
project_home = '/home/yourusername/attendance-request-system'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables (optional but recommended)
os.environ['FLASK_APP'] = 'app.py'
os.environ['FLASK_ENV'] = 'production'

# Optional: Load environment variables from .env file
# Uncomment these lines if you're using python-dotenv
# from dotenv import load_dotenv
# load_dotenv(os.path.join(project_home, '.env'))

# Import the Flask app
# The 'app' variable in app.py is imported as 'application' for WSGI
from app import app as application

# Optional: Database connection on startup
from db_config import db
db.connect()

# That's it! PythonAnywhere will handle running the application
# Make sure app.run() is commented out in app.py
