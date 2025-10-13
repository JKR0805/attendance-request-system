# Attendance Request & Approval System

A comprehensive web-based attendance request management system built with Flask and MySQL that streamlines the process of requesting, reviewing, and approving attendance requests in educational institutions.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [API Routes](#api-routes)
- [User Roles & Workflow](#user-roles--workflow)
- [Management Tools](#management-tools)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [Production Deployment](#production-deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The Attendance Request & Approval System is a Flask-based web application designed to digitize and streamline the attendance request process in educational institutions. It implements a hierarchical approval workflow where students submit requests, coordinators review them, and HODs provide final approval.

### Key Highlights

- **Multi-tier approval system** (Student → Coordinator → HOD)
- **File attachment support** for supporting documents
- **Role-based access control** for secure operations
- **Real-time status tracking** with comprehensive dashboards
- **Advanced filtering and search** capabilities
- **Mobile-responsive design** for access on any device
- **Complete audit trail** of all approvals and decisions

---

## ✨ Features

### For Students

- ✅ **User Registration**: Self-service account creation with validation
- ✅ **Request Submission**: Submit attendance requests with details:
  - Subject and description
  - Start and end date/time
  - Contact information
  - File attachments (PDF, DOC, DOCX, images)
- ✅ **Request Tracking**: Monitor status in real-time
  - Pending with Coordinator
  - Pending with HOD
  - Approved (Final)
  - Rejected
- ✅ **Dashboard**: View all personal requests with filtering
- ✅ **Attachment Download**: Access uploaded supporting documents

### For Coordinators

- ✅ **Request Review**: View all pending student requests
- ✅ **Approve/Reject**: First-level approval authority
- ✅ **Forward to HOD**: Send approved requests for final approval
- ✅ **Add Remarks**: Provide feedback with decisions
- ✅ **Comprehensive View**: Access all requests with search/filter

### For HODs

- ✅ **Final Approval**: Review coordinator-approved requests
- ✅ **Ultimate Authority**: Final approve/reject decisions
- ✅ **Complete Oversight**: View all requests across departments
- ✅ **Decision History**: Track approval chain and remarks

### Common Features

- 🔍 **All Requests Page**: Unified view with advanced filters
  - Filter by status (All, Pending, With HOD, Approved, Rejected)
  - Search by keyword (subject, description, student name)
  - Statistics dashboard with counts
- 📊 **Statistics**: Real-time metrics and counts
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- 🔒 **Secure Authentication**: Password hashing and session management
- 📎 **File Management**: Secure upload, storage, and download

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Client Browser                           │
│              (HTML/CSS/JavaScript)                          │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        │ HTTP/HTTPS
                        │
┌───────────────────────▼─────────────────────────────────────┐
│                  Flask Application                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Routes Layer (app.py)                              │   │
│  │  • Student Routes • Coordinator Routes • HOD Routes │   │
│  └─────────────────────┬───────────────────────────────┘   │
│  ┌─────────────────────▼───────────────────────────────┐   │
│  │  Business Logic Layer (db_config.py)                │   │
│  │  • Authentication • Request Management • Approvals  │   │
│  └─────────────────────┬───────────────────────────────┘   │
└────────────────────────┼─────────────────────────────────────┘
                         │
                         │ MySQL Connector
                         │
┌────────────────────────▼─────────────────────────────────────┐
│                  MySQL Database                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ students │  │  users   │  │ requests │  │approvals │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                  File System (uploads/)                      │
│              Attachment Storage                              │
└──────────────────────────────────────────────────────────────┘
```

### Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Backend Framework** | Flask | 3.0.0 |
| **Database** | MySQL | 8.0+ |
| **Database Connector** | mysql-connector-python | 8.2.0 |
| **Security** | Werkzeug | 3.0.1 |
| **Frontend** | HTML5, CSS3, Jinja2 | - |
| **Language** | Python | 3.x |

---

## 🚀 Installation

### Prerequisites

- Python 3.x installed
- MySQL Server 8.0+ installed and running
- pip (Python package manager)
- Git (optional)

### Step 1: Clone or Download

```cmd
git clone <repository-url>
cd attendance-request-system
```

Or download and extract the ZIP file.

### Step 2: Install Dependencies

```cmd
pip install -r requirements.txt
```

**Dependencies installed:**
- Flask 3.0.0
- mysql-connector-python 8.2.0
- Werkzeug 3.0.1

### Step 3: Setup Database

**Option A: Using MySQL Command Line**
```cmd
mysql -u root -p < database\attendance_system.sql
```

**Option B: Using MySQL Workbench**
1. Open MySQL Workbench
2. Connect to your server
3. Go to File → Run SQL Script
4. Select `database/attendance_system.sql`
5. Execute

### Step 4: Configure Database Connection

Edit `db_config.py` (around line 15):

```python
# Update with your MySQL credentials
db = DatabaseConfig(
    host='localhost',
    database='attendance_system',
    user='root',           # Your MySQL username
    password='root'        # Your MySQL password
)
```

### Step 5: Create Upload Directory

The application will automatically create this, but you can do it manually:

```cmd
mkdir uploads
```

### Step 6: Run Application

```cmd
python app.py
```

Or use the provided batch file:

```cmd
run.bat
```

### Step 7: Access Application

Open your browser and navigate to:
```
http://localhost:5000
```

---

## ⚙️ Configuration

### Application Settings

Edit `app.py` for application configuration:

```python
# Secret key for session management (line 13)
app.secret_key = 'your_secret_key_here_change_in_production'

# Upload folder (line 14)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Maximum file size: 16MB (line 15)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Allowed file extensions (line 16)
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'}

# Server port (last line)
app.run(debug=True, host='0.0.0.0', port=5000)
```

### Database Configuration

Edit `db_config.py`:

```python
class DatabaseConfig:
    def __init__(self, host='localhost', 
                 database='attendance_system', 
                 user='root', 
                 password='root'):
```

---

## 📖 Usage

### Default Login Credentials

| Role | Email | Password |
|------|-------|----------|
| **Student 1** | dood1@student.com | password |
| **Student 2** | dood2@student.com | password |
| **Student 3** | dood3@student.com | password |
| **Coordinator** | coordinator@college.com | password |
| **HOD** | hod@college.com | password |

⚠️ **Change these passwords after first login!**

### Student Workflow

1. **Register Account**
   - Navigate to "Student Login"
   - Click "Register" link
   - Fill in details: Name, Department, Contact, Email, Password
   - Submit registration

2. **Login**
   - Enter email and password
   - Access student dashboard

3. **Submit Request**
   - Click "Submit New Request"
   - Fill in form:
     - Subject (e.g., "Workshop Attendance")
     - Description (detailed reason)
     - Start Date/Time
     - End Date/Time
     - Contact Number
     - Attach supporting document (optional)
   - Submit request

4. **Track Status**
   - View dashboard for request status
   - Click "View Details" for full information
   - Check approval history and remarks
   - Download attachments if needed

5. **Use All Requests Page**
   - Click "📋 All Requests" in navigation
   - Filter by status
   - Search by keywords
   - View statistics

### Coordinator Workflow

1. **Login**
   - Navigate to "Coordinator Login"
   - Enter credentials

2. **Review Pending Requests**
   - Dashboard shows all pending requests
   - Click "View Details" to see full information
   - Download and review attachments

3. **Approve or Reject**
   - Click "Approve" to forward to HOD
   - Click "Reject" to deny request
   - Add remarks (optional but recommended)
   - Submit decision

4. **Monitor All Requests**
   - Use "All Requests" page
   - Filter and search capabilities
   - View statistics

### HOD Workflow

1. **Login**
   - Navigate to "HOD Login"
   - Enter credentials

2. **Review Coordinator-Approved Requests**
   - Dashboard shows requests pending final approval
   - Review all details and approval history

3. **Final Decision**
   - Click "Approve" for final approval
   - Click "Reject" to deny
   - Add remarks
   - Submit decision

4. **Complete Oversight**
   - Access all requests via "All Requests"
   - Monitor system statistics
   - Track approval patterns

---

## 📁 Project Structure

```
attendance-request-system/
│
├── 📄 app.py                      # Main Flask application (450+ lines)
│   ├── Route definitions (15 routes)
│   ├── File upload handling
│   ├── Session management
│   ├── Error handlers
│   └── Template filters
│
├── 📄 db_config.py                # Database handler class (250+ lines)
│   ├── DatabaseConfig class
│   ├── Connection management
│   ├── Query execution methods
│   ├── Authentication methods
│   └── CRUD operations
│
├── 📄 requirements.txt            # Python dependencies
│   ├── Flask==3.0.0
│   ├── mysql-connector-python==8.2.0
│   └── Werkzeug==3.0.1
│
├── 📄 config_template.py          # Configuration template
├── 📄 reset_database.py           # Database reset utility
├── 📄 change_password.py          # Password management tool
├── 📄 run.bat                     # Windows batch launcher
├── 📄 setup.bat                   # Windows setup script
│
├── 📂 database/
│   └── 📄 attendance_system.sql   # Complete database schema + sample data
│       ├── 4 table definitions
│       ├── Indexes for performance
│       └── Sample data for testing
│
├── 📂 templates/                  # HTML templates (14 files)
│   ├── 📄 base.html              # Master template with navigation
│   ├── 📄 index.html             # Home page
│   ├── 📄 404.html               # Not found error
│   ├── 📄 500.html               # Server error
│   │
│   ├── Student Templates (4 files)
│   ├── 📄 student_register.html  # Registration form
│   ├── 📄 student_login.html     # Login page
│   ├── 📄 student_dashboard.html # Dashboard with requests list
│   └── 📄 student_form.html      # New request submission form
│   │
│   ├── Coordinator Templates (2 files)
│   ├── 📄 coordinator_login.html # Login page
│   └── 📄 coordinator.html       # Dashboard with pending requests
│   │
│   ├── HOD Templates (2 files)
│   ├── 📄 hod_login.html         # Login page
│   └── 📄 hod.html               # Dashboard with approved requests
│   │
│   ├── Common Templates (2 files)
│   ├── 📄 view_request.html      # Detailed request view
│   └── 📄 all_requests.html      # All requests with filters
│
├── 📂 static/
│   └── 📄 style.css              # Complete styling (1300+ lines)
│       ├── Global styles
│       ├── Navigation and layout
│       ├── Forms and buttons
│       ├── Cards and badges
│       ├── Tables and lists
│       ├── Statistics dashboard
│       └── Responsive media queries
│
├── 📂 uploads/                    # User-uploaded attachments
│   └── (Files stored with timestamp prefix)
│
└── 📂 __pycache__/               # Python cache files (auto-generated)
```

### File Descriptions

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| `app.py` | Main application | 450+ | 15 routes, authentication, file handling |
| `db_config.py` | Database operations | 250+ | Connection, queries, CRUD methods |
| `style.css` | All styling | 1300+ | Responsive design, animations |
| `base.html` | Template base | 200+ | Navigation, layout structure |
| `all_requests.html` | Unified requests view | 250+ | Filters, search, statistics |

---

## 🗄️ Database Schema

### Overview

The system uses 4 interconnected tables to manage the complete request lifecycle:

```sql
students (7 columns)
    ↓ (1:N)
requests (11 columns)
    ↓ (1:N)
approvals (7 columns)
    ↑ (N:1)
users (7 columns)
```

### Table: `students`

Student account information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `student_id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `name` | VARCHAR(100) | NOT NULL | Student full name |
| `department` | VARCHAR(100) | NOT NULL | Academic department |
| `contact` | VARCHAR(15) | NOT NULL | Phone number |
| `email` | VARCHAR(100) | UNIQUE, NOT NULL | Email address (login) |
| `password` | VARCHAR(255) | NOT NULL | Hashed password (MD5) |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Account creation time |

**Indexes:**
- PRIMARY KEY on `student_id`
- UNIQUE INDEX on `email`

### Table: `users`

Staff accounts (Coordinators and HODs).

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `user_id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `name` | VARCHAR(100) | NOT NULL | Staff full name |
| `role` | ENUM | 'coordinator', 'hod', NOT NULL | Role type |
| `department` | VARCHAR(100) | NOT NULL | Department |
| `email` | VARCHAR(100) | UNIQUE, NOT NULL | Email address (login) |
| `password` | VARCHAR(255) | NOT NULL | Hashed password (MD5) |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Account creation time |

**Indexes:**
- PRIMARY KEY on `user_id`
- UNIQUE INDEX on `email`

### Table: `requests`

Attendance requests submitted by students.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `request_id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `student_id` | INT | FOREIGN KEY → students, NOT NULL | Request owner |
| `subject` | VARCHAR(200) | NOT NULL | Request subject/title |
| `description` | TEXT | NOT NULL | Detailed description |
| `start_time` | DATETIME | NOT NULL | Event start date/time |
| `end_time` | DATETIME | NOT NULL | Event end date/time |
| `contact` | VARCHAR(15) | NOT NULL | Contact during absence |
| `attachment_path` | VARCHAR(255) | NULL | File path in uploads/ |
| `status` | ENUM | See below, DEFAULT 'pending' | Current status |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Submission time |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Last modification |

**Status Values:**
- `pending` - Waiting for coordinator review
- `approved_by_coordinator` - Waiting for HOD approval
- `approved` - Finally approved by HOD
- `rejected` - Rejected by coordinator or HOD

**Indexes:**
- PRIMARY KEY on `request_id`
- INDEX on `student_id`
- INDEX on `status`

**Foreign Keys:**
- `student_id` REFERENCES `students(student_id)` ON DELETE CASCADE

### Table: `approvals`

Approval history and decision trail.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `approval_id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `request_id` | INT | FOREIGN KEY → requests, NOT NULL | Related request |
| `approver_role` | ENUM | 'coordinator', 'hod', NOT NULL | Approver type |
| `approver_name` | VARCHAR(100) | NOT NULL | Name of approver |
| `decision` | ENUM | 'approved', 'rejected', NOT NULL | Decision made |
| `remarks` | TEXT | NULL | Comments/feedback |
| `decision_time` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When decided |

**Indexes:**
- PRIMARY KEY on `approval_id`
- INDEX on `request_id`

**Foreign Keys:**
- `request_id` REFERENCES `requests(request_id)` ON DELETE CASCADE

### Relationships

```
┌─────────────┐
│  students   │
│ (1 student) │
└──────┬──────┘
       │ 1:N
       │
┌──────▼──────────┐
│   requests      │
│ (N requests)    │
└──────┬──────────┘
       │ 1:N
       │
┌──────▼──────────┐      ┌─────────────┐
│   approvals     │ N:1  │    users    │
│ (N approvals)   ├──────┤ (1 user)    │
└─────────────────┘      └─────────────┘
```

### Sample Data

The database comes pre-populated with test data:

**Students:**
- dood1@student.com (Computer Science)
- dood2@student.com (Information Technology)
- dood3@student.com (Electronics)

**Users:**
- coordinator@college.com (Coordinator, Computer Science)
- hod@college.com (HOD, Computer Science)

**Requests:**
- 2 sample requests in pending status

All default passwords are: `password` (hashed as MD5)

---

## 🛣️ API Routes

### Public Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/student/register` | GET, POST | Student registration form |
| `/student/login` | GET, POST | Student login |
| `/coordinator/login` | GET, POST | Coordinator login |
| `/hod/login` | GET, POST | HOD login |

### Student Routes (Requires Student Login)

| Route | Method | Description |
|-------|--------|-------------|
| `/student/dashboard` | GET | View all personal requests |
| `/student/request` | GET, POST | Submit new attendance request |

### Coordinator Routes (Requires Coordinator Login)

| Route | Method | Description |
|-------|--------|-------------|
| `/coordinator/dashboard` | GET | View pending requests |
| `/coordinator/action/<id>` | POST | Approve/reject request |

### HOD Routes (Requires HOD Login)

| Route | Method | Description |
|-------|--------|-------------|
| `/hod/dashboard` | GET | View coordinator-approved requests |
| `/hod/action/<id>` | POST | Final approve/reject |

### Common Routes (Requires Any Login)

| Route | Method | Description |
|-------|--------|-------------|
| `/request/view/<id>` | GET | View detailed request information |
| `/attachment/<id>` | GET | Download request attachment |
| `/all-requests` | GET | View all requests with filters |
| `/logout` | GET | Logout and clear session |

### Error Handlers

| Code | Route | Description |
|------|-------|-------------|
| 404 | Auto | Page not found |
| 500 | Auto | Internal server error |

### Route Parameters

**Query Parameters (GET):**
- `/all-requests?status=pending` - Filter by status
- `/all-requests?search=workshop` - Search by keyword

**Path Parameters:**
- `<id>` or `<request_id>` - Integer request ID

**Form Data (POST):**
- Various form fields depending on route
- Multipart form data for file uploads

---

## 👥 User Roles & Workflow

### Request Lifecycle

```
┌──────────────────────────────────────────────────────────┐
│                  STUDENT SUBMITS REQUEST                 │
│         (Subject, Description, Dates, Attachment)        │
└───────────────────────┬──────────────────────────────────┘
                        │
                        ▼
            ┌─────────────────────┐
            │  Status: pending    │
            └───────────┬─────────┘
                        │
                        ▼
┌───────────────────────────────────────────────────────────┐
│           COORDINATOR REVIEWS REQUEST                     │
│         (Can view details and attachment)                 │
└───────────────────────┬───────────────────────────────────┘
                        │
            ┌───────────┴───────────┐
            │                       │
            ▼                       ▼
    ┌──────────────┐       ┌──────────────────┐
    │   APPROVE    │       │     REJECT       │
    │ + Remarks    │       │   + Remarks      │
    └───────┬──────┘       └────────┬─────────┘
            │                       │
            ▼                       ▼
┌────────────────────────┐  ┌─────────────────┐
│Status:                 │  │Status: rejected │
│approved_by_coordinator │  │    [END]        │
└───────────┬────────────┘  └─────────────────┘
            │
            ▼
┌───────────────────────────────────────────────────────────┐
│                HOD REVIEWS REQUEST                        │
│    (Can view all details, approval history, attachment)   │
└───────────────────────┬───────────────────────────────────┘
                        │
            ┌───────────┴───────────┐
            │                       │
            ▼                       ▼
    ┌──────────────┐       ┌──────────────────┐
    │   APPROVE    │       │     REJECT       │
    │ + Remarks    │       │   + Remarks      │
    └───────┬──────┘       └────────┬─────────┘
            │                       │
            ▼                       ▼
    ┌──────────────┐       ┌─────────────────┐
    │   Status:    │       │Status: rejected │
    │   approved   │       │    [END]        │
    │   [END]      │       └─────────────────┘
    └──────────────┘
```

### Role Permissions Matrix

| Feature | Student | Coordinator | HOD |
|---------|---------|-------------|-----|
| Register Account | ✅ | ❌ | ❌ |
| Submit Request | ✅ | ❌ | ❌ |
| View Own Requests | ✅ | ❌ | ❌ |
| View All Requests | ❌ | ✅ | ✅ |
| View Pending Requests | ❌ | ✅ | ❌ |
| View Approved Requests | ❌ | ❌ | ✅ |
| First Approval | ❌ | ✅ | ❌ |
| Final Approval | ❌ | ❌ | ✅ |
| Download Own Attachments | ✅ | ❌ | ❌ |
| Download All Attachments | ❌ | ✅ | ✅ |
| View Approval History | ✅ | ✅ | ✅ |

### Authorization Checks

The system implements role-based access control:

```python
@login_required('student')  # Only students
@login_required('coordinator')  # Only coordinators
@login_required('hod')  # Only HODs
@login_required()  # Any authenticated user
```

---

## 🛠️ Management Tools

### 1. Reset Database (`reset_database.py`)

Completely resets the database to initial state with fresh sample data.

**Purpose:**
- Development testing
- Clean slate after errors
- Restore default configuration

**Usage:**
```cmd
python reset_database.py
```

**Interactive Process:**
1. Shows current configuration
2. Asks for confirmation (type "YES")
3. Drops all tables
4. Recreates schema
5. Inserts sample data
6. Verifies installation

**⚠️ WARNING:** This deletes ALL data permanently!

**What it does:**
- Drops existing tables (if any)
- Creates fresh schema
- Adds 3 sample students
- Adds 1 coordinator and 1 HOD
- Creates 2 sample requests
- Sets up indexes

**Before Running:**
- Stop Flask application
- Backup uploads/ folder if needed
- Export any data you want to keep

### 2. Change Password (`change_password.py`)

Interactive tool for password management.

**Purpose:**
- Change student passwords
- Change coordinator/HOD passwords
- List all users
- Security management

**Usage:**
```cmd
python change_password.py
```

**Menu Options:**

```
=== Attendance System - Password Manager ===
1. Change student password
2. Change coordinator/HOD password
3. List all users
4. Exit
```

**Option 1: Change Student Password**
1. Enter student email
2. Enter new password (6+ characters)
3. Confirm password
4. Password updated

**Option 2: Change Coordinator/HOD Password**
1. Enter user email
2. Select role (coordinator/hod)
3. Enter new password (6+ characters)
4. Confirm password
5. Password updated

**Option 3: List All Users**
- Shows all students
- Shows all coordinators/HODs
- Displays email addresses

**Password Requirements:**
- Minimum 6 characters
- Must be confirmed
- Automatically hashed (MD5)

**Example Session:**
```
Choose option: 1
Enter student email: dood1@student.com
Enter new password: ********
Confirm password: ********
✓ Password updated successfully for dood1@student.com
```

### 3. Batch Files (Windows)

**`run.bat`** - Quick launcher
```batch
@echo off
python app.py
pause
```

**`setup.bat`** - Initial setup
```batch
@echo off
pip install -r requirements.txt
python reset_database.py
pause
```

---

## 🔒 Security

### Authentication

**Password Hashing:**
- Uses MD5 hashing (via `hashlib`)
- Passwords never stored in plain text
- Hash comparison for verification

```python
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
```

⚠️ **Production Note:** MD5 is not recommended for production. Use bcrypt:
```python
from werkzeug.security import generate_password_hash, check_password_hash
```

**Session Management:**
- Flask sessions with secret key
- Session data:
  - `user_id` - User identifier
  - `name` - Display name
  - `role` - User role (student/coordinator/hod)
  - `email` - Email address
- Session cleared on logout
- Session timeout on browser close

### Authorization

**Role-Based Access Control:**
```python
def login_required(role=None):
    """Decorator to check if user is logged in"""
    # Checks session existence
    # Validates role if specified
    # Redirects unauthorized users
```

**File Access Control:**
- Students can only download own attachments
- Coordinators/HODs can download all attachments
- Path validation to prevent directory traversal

### File Upload Security

**Allowed Extensions:**
- PDF (.pdf)
- Images (.png, .jpg, .jpeg)
- Documents (.doc, .docx)

**File Size Limit:**
- Maximum 16MB per file
- Enforced at Flask configuration level

**Secure Filename:**
```python
from werkzeug.utils import secure_filename
filename = secure_filename(file.filename)
```

**Timestamp Prefix:**
- Files saved with timestamp: `20251013_143022_document.pdf`
- Prevents filename collisions
- Maintains upload order

### SQL Injection Protection

**Parameterized Queries:**
```python
query = "SELECT * FROM students WHERE email = %s AND password = %s"
cursor.execute(query, (email, password))
```

All database queries use parameterized statements - no string concatenation.

### CSRF Protection

**Current State:** Not implemented (suitable for educational use)

**Production Recommendation:**
```python
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)
```

### Security Checklist for Production

- [ ] Replace MD5 with bcrypt/Argon2
- [ ] Implement CSRF protection
- [ ] Add rate limiting (Flask-Limiter)
- [ ] Enable HTTPS/SSL
- [ ] Set secure session cookies
- [ ] Implement email verification
- [ ] Add two-factor authentication
- [ ] Set up logging and monitoring
- [ ] Configure firewall rules
- [ ] Use environment variables for secrets
- [ ] Implement input validation
- [ ] Add security headers
- [ ] Regular security audits

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### 1. Database Connection Failed

**Error:**
```
Error connecting to MySQL: Access denied for user 'root'@'localhost'
```

**Solution:**
Edit `db_config.py` (line 14):
```python
db = DatabaseConfig(
    host='localhost',
    database='attendance_system',
    user='YOUR_USERNAME',    # Change this
    password='YOUR_PASSWORD'  # Change this
)
```

**Verify MySQL is running:**
```cmd
mysql -u root -p
```

#### 2. Can't Download Attachments

**Symptoms:**
- "Attachment not found" error
- Download button doesn't work

**Solutions:**

**A. Check file exists:**
```cmd
dir uploads
```

**B. Verify permissions:**
- Ensure uploads/ folder is readable
- Check file ownership

**C. Check authorization:**
- Students can only download own attachments
- Must be logged in

**D. Re-login:**
```
Logout → Login again
```

#### 3. Reset Script Fails

**Error:**
```
Error: Table 'attendance_system.students' doesn't exist
```

**Solutions:**

**A. Stop Flask first:**
```
Press Ctrl+C in terminal running app.py
```

**B. Verify MySQL running:**
```cmd
mysql -u root -p -e "SHOW DATABASES;"
```

**C. Check credentials:**
- Ensure db_config.py has correct credentials
- Test MySQL connection manually

**D. Run with elevated permissions:**
```cmd
Run as Administrator (Windows)
```

#### 4. Password Change Not Working

**Symptoms:**
- "User not found" message
- Password not updating

**Solutions:**

**A. Verify email exists:**
```cmd
python change_password.py
Choose option: 3 (List all users)
```

**B. Check password length:**
- Must be 6+ characters
- Both entries must match

**C. Verify role:**
- Students don't have a role field
- Coordinators/HODs need correct role selection

#### 5. Port 5000 Already in Use

**Error:**
```
OSError: [Errno 98] Address already in use
```

**Solutions:**

**A. Kill existing process:**
```cmd
netstat -ano | findstr :5000
taskkill /PID <process_id> /F
```

**B. Change port:**
Edit `app.py` (last line):
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

#### 6. File Upload Fails

**Symptoms:**
- "File upload failed" error
- Form submits without attachment

**Solutions:**

**A. Check file size:**
- Maximum 16MB allowed
- Compress large files

**B. Verify file extension:**
- Allowed: PDF, PNG, JPG, JPEG, DOC, DOCX
- Use lowercase extensions

**C. Check uploads/ folder:**
```cmd
mkdir uploads
icacls uploads /grant Everyone:(OI)(CI)F /T
```

#### 7. Session Expires Immediately

**Symptoms:**
- Logged out after each request
- "Please login first" message

**Solutions:**

**A. Check secret key:**
Edit `app.py`:
```python
app.secret_key = 'your_secret_key_here'  # Must be set
```

**B. Enable cookies:**
- Check browser settings
- Allow cookies from localhost

**C. Check debug mode:**
```python
app.run(debug=True)  # Should be True for development
```

#### 8. Templates Not Loading

**Error:**
```
TemplateNotFound: index.html
```

**Solutions:**

**A. Verify folder structure:**
```cmd
dir templates
```

**B. Check working directory:**
```cmd
cd attendance-request-system
python app.py
```

**C. Verify template names:**
- Must match exactly (case-sensitive on Linux)

#### 9. MySQL Import Fails

**Error:**
```
ERROR 1064: You have an error in your SQL syntax
```

**Solutions:**

**A. Check MySQL version:**
```cmd
mysql --version
```
Requires MySQL 5.7+

**B. Use correct command:**
```cmd
mysql -u root -p < database\attendance_system.sql
```

**C. Import from MySQL:**
```sql
SOURCE C:/path/to/database/attendance_system.sql;
```

#### 10. Static Files Not Loading

**Symptoms:**
- No CSS styling
- Images not displaying

**Solutions:**

**A. Clear browser cache:**
```
Ctrl+Shift+Delete (Chrome/Edge)
Ctrl+Shift+R (Hard refresh)
```

**B. Check folder structure:**
```cmd
dir static
```

**C. Verify Flask route:**
```python
app = Flask(__name__)  # No custom static folder
```

### Getting Help

1. **Check application logs:**
   - Terminal output shows errors
   - Flask debug mode provides detailed traces

2. **Enable debug mode:**
   ```python
   app.run(debug=True)
   ```

3. **Test database connection:**
   ```python
   python -c "from db_config import db; print(db.connect())"
   ```

4. **Verify Python version:**
   ```cmd
   python --version
   ```
   Requires Python 3.x

5. **Check dependencies:**
   ```cmd
   pip list
   ```

---

## 💻 Development

### Setting Up Development Environment

1. **Clone repository:**
   ```cmd
   git clone <repo-url>
   cd attendance-request-system
   ```

2. **Create virtual environment (recommended):**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

4. **Setup database:**
   ```cmd
   mysql -u root -p < database\attendance_system.sql
   ```

5. **Configure:**
   - Edit `db_config.py` with your credentials

6. **Run in debug mode:**
   ```cmd
   python app.py
   ```

### Adding New Features

#### Adding a New Route

1. **Define route in `app.py`:**
```python
@app.route('/new-feature')
@login_required('student')
def new_feature():
    # Your logic here
    return render_template('new_feature.html')
```

2. **Create template in `templates/`:**
```html
{% extends "base.html" %}
{% block content %}
<!-- Your HTML -->
{% endblock %}
```

3. **Add styles in `static/style.css`:**
```css
.new-feature {
    /* Your styles */
}
```

4. **Add navigation link in `base.html`:**
```html
<a href="{{ url_for('new_feature') }}">New Feature</a>
```

#### Adding Database Methods

Edit `db_config.py`:

```python
def new_method(self, param1, param2):
    """Description of method"""
    query = "SELECT * FROM table WHERE column = %s"
    return self.execute_query(query, (param1,), fetch=True)
```

#### Custom Jinja2 Filters

Add to `app.py`:

```python
@app.template_filter('custom_filter')
def custom_filter(value):
    """Transform value"""
    return transformed_value
```

Use in templates:
```html
{{ value|custom_filter }}
```

### Code Style Guidelines

**Python (PEP 8):**
- 4 spaces indentation
- Max line length: 79 characters
- Docstrings for all functions
- Type hints where appropriate

**HTML:**
- 4 spaces indentation
- Semantic elements
- Accessible markup (ARIA labels)

**CSS:**
- Mobile-first approach
- BEM naming convention (optional)
- Organized by component

### Testing

**Manual Testing Checklist:**

- [ ] Student registration
- [ ] Student login
- [ ] Submit request with attachment
- [ ] Coordinator approval
- [ ] HOD approval
- [ ] Request rejection
- [ ] File download
- [ ] All requests filtering
- [ ] Search functionality
- [ ] Logout

**Database Testing:**
```sql
-- Verify data
SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM requests;
SELECT * FROM requests WHERE status = 'pending';
```

### Debugging Tips

1. **Enable Flask debug mode:**
   ```python
   app.run(debug=True)
   ```

2. **Add print statements:**
   ```python
   print(f"Debug: {variable_name}")
   ```

3. **Check Flask logs:**
   - Terminal shows all requests
   - Stack traces for errors

4. **Use browser DevTools:**
   - Network tab for API calls
   - Console for JavaScript errors

5. **Test database queries:**
   ```python
   from db_config import db
   result = db.execute_query("SELECT * FROM students", fetch=True)
   print(result)
   ```

### Version Control

**Git Workflow:**

```cmd
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature: description"

# Push to remote
git push origin feature/new-feature

# Create pull request
```

**Important Files to Ignore (.gitignore):**
```
__pycache__/
*.pyc
*.pyo
venv/
.env
db_config.py  # If contains sensitive data
uploads/*
!uploads/.gitkeep
*.log
.DS_Store
```

---

## 🚀 Production Deployment

### Pre-Deployment Checklist

#### Security

- [ ] Change `app.secret_key` in `app.py`
- [ ] Use bcrypt instead of MD5 for passwords
- [ ] Set `app.run(debug=False)`
- [ ] Enable CSRF protection
- [ ] Implement rate limiting
- [ ] Add security headers
- [ ] Set up HTTPS/SSL
- [ ] Use environment variables for secrets

#### Database

- [ ] Update credentials in `db_config.py`
- [ ] Set up database backups
- [ ] Configure connection pooling
- [ ] Optimize indexes
- [ ] Set up monitoring

#### Application

- [ ] Use production WSGI server (gunicorn/uWSGI)
- [ ] Set up logging
- [ ] Configure error monitoring (Sentry)
- [ ] Set up health checks
- [ ] Configure firewall rules

#### Infrastructure

- [ ] Set up reverse proxy (Nginx/Apache)
- [ ] Configure load balancing (if needed)
- [ ] Set up CDN for static files
- [ ] Configure backup strategy
- [ ] Set up monitoring (Prometheus, Grafana)

### Deployment Options

#### Option 1: Traditional Server (Linux)

**1. Setup Server:**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3 python3-pip python3-venv mysql-server nginx -y
```

**2. Setup Application:**
```bash
# Create app directory
sudo mkdir -p /var/www/attendance-system
cd /var/www/attendance-system

# Clone repository
git clone <repo-url> .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install production server
pip install gunicorn
```

**3. Configure Database:**
```bash
# Secure MySQL
sudo mysql_secure_installation

# Create database
mysql -u root -p < database/attendance_system.sql

# Update db_config.py
nano db_config.py
```

**4. Setup Gunicorn:**

Create `/etc/systemd/system/attendance.service`:
```ini
[Unit]
Description=Attendance System
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/attendance-system
Environment="PATH=/var/www/attendance-system/venv/bin"
ExecStart=/var/www/attendance-system/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 app:app

[Install]
WantedBy=multi-user.target
```

Start service:
```bash
sudo systemctl start attendance
sudo systemctl enable attendance
```

**5. Configure Nginx:**

Create `/etc/nginx/sites-available/attendance`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /var/www/attendance-system/static;
    }

    location /uploads {
        internal;
        alias /var/www/attendance-system/uploads;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/attendance /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

**6. Setup SSL (Let's Encrypt):**
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

#### Option 2: Docker Deployment

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application
COPY . .

# Create uploads directory
RUN mkdir -p uploads

# Expose port
EXPOSE 8000

# Run gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: your_password
      MYSQL_DATABASE: attendance_system
    volumes:
      - ./database/attendance_system.sql:/docker-entrypoint-initdb.d/init.sql
      - mysql_data:/var/lib/mysql
    networks:
      - app_network

  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      DB_HOST: db
      DB_USER: root
      DB_PASSWORD: your_password
      DB_NAME: attendance_system
    depends_on:
      - db
    volumes:
      - ./uploads:/app/uploads
    networks:
      - app_network

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./static:/var/www/static
    depends_on:
      - app
    networks:
      - app_network

volumes:
  mysql_data:

networks:
  app_network:
```

Deploy:
```bash
docker-compose up -d
```

#### Option 3: Cloud Platforms

**A. Heroku:**
```bash
# Install Heroku CLI
heroku create attendance-system

# Add MySQL addon
heroku addons:create jawsdb:kitefin

# Configure
heroku config:set SECRET_KEY=your_secret_key

# Deploy
git push heroku main
```

**B. AWS Elastic Beanstalk:**
```bash
# Install EB CLI
eb init -p python-3.11 attendance-system

# Create environment
eb create attendance-env

# Deploy
eb deploy
```

**C. DigitalOcean App Platform:**
1. Connect GitHub repository
2. Configure build/run commands
3. Add MySQL database
4. Deploy

### Production Configuration

**Environment Variables:**

Create `.env`:
```bash
SECRET_KEY=your_very_secret_key_here
DB_HOST=localhost
DB_USER=attendance_user
DB_PASSWORD=strong_password
DB_NAME=attendance_system
FLASK_ENV=production
```

**Update `db_config.py`:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

db = DatabaseConfig(
    host=os.getenv('DB_HOST', 'localhost'),
    database=os.getenv('DB_NAME', 'attendance_system'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', 'root')
)
```

**Update `app.py`:**
```python
app.secret_key = os.getenv('SECRET_KEY', 'default_dev_key')
app.config['SESSION_COOKIE_SECURE'] = True  # HTTPS only
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
```

### Monitoring & Maintenance

**1. Application Logs:**
```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
```

**2. Database Backups:**
```bash
# Daily backup script
mysqldump -u root -p attendance_system > backup_$(date +%Y%m%d).sql

# Automate with cron
0 2 * * * /path/to/backup_script.sh
```

**3. Monitor Resource Usage:**
```bash
# CPU/Memory
htop

# Disk space
df -h

# Network
netstat -tuln
```

**4. Set up Alerts:**
- Database connection failures
- High error rates
- Disk space warnings
- SSL certificate expiry

### Scaling Considerations

**Horizontal Scaling:**
- Load balancer (Nginx/HAProxy)
- Multiple app instances
- Shared session store (Redis)
- Centralized uploads (S3/Cloud Storage)

**Vertical Scaling:**
- Increase server resources
- Optimize database queries
- Add caching (Redis/Memcached)
- CDN for static files

**Database Optimization:**
- Connection pooling
- Read replicas
- Query optimization
- Index tuning

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### How to Contribute

1. **Fork the repository**
2. **Create feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make changes:**
   - Follow code style guidelines
   - Add comments and documentation
   - Test thoroughly
4. **Commit changes:**
   ```bash
   git commit -m "Add amazing feature"
   ```
5. **Push to branch:**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open Pull Request**

### Contribution Areas

We especially welcome:
- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- 🔒 Security improvements
- 🧪 Test coverage
- 🌍 Internationalization

### Code Review Process

1. All PRs require review
2. Tests must pass
3. Code style must be consistent
4. Documentation must be updated
5. No merge conflicts

---

## 📄 License

This project is developed for educational purposes as part of a Python-MySQL curriculum.

**For Educational Use:**
- ✅ Learning and teaching
- ✅ Academic projects
- ✅ Portfolio demonstrations
- ✅ Modified versions for education

**Commercial Use:**
- Contact the authors for licensing

---

## 📞 Support & Contact

### Getting Help

1. **Check Documentation:** This README covers most scenarios
2. **Review Troubleshooting:** Common issues section above
3. **Check Code Comments:** In-code documentation
4. **Test Database:** Use reset_database.py for clean state

### Reporting Issues

When reporting issues, include:
- Python version (`python --version`)
- MySQL version (`mysql --version`)
- Operating system
- Error messages (full stack trace)
- Steps to reproduce
- Expected vs actual behavior

### Project Information

- **Version:** 2.1
- **Last Updated:** October 13, 2025
- **Python:** 3.x
- **Flask:** 3.0.0
- **MySQL:** 8.0+

---

## 🔮 Future Enhancements

### Planned Features

- [ ] **Email Notifications**
  - Status change alerts
  - Approval reminders
  - Deadline warnings

- [ ] **Export Functionality**
  - Excel/CSV export
  - PDF reports
  - Bulk data download

- [ ] **Advanced Filters**
  - Date range selection
  - Department filtering
  - Multiple status selection

- [ ] **Bulk Operations**
  - Multi-select approval
  - Batch rejection
  - Bulk status updates

- [ ] **Request Editing**
  - Edit before approval
  - Resubmit rejected requests
  - Cancel pending requests

- [ ] **Enhanced Security**
  - Two-factor authentication
  - Password strength meter
  - Account recovery
  - Activity logs

- [ ] **Analytics Dashboard**
  - Approval statistics
  - Response time metrics
  - Department-wise reports
  - Trend analysis

- [ ] **Mobile App**
  - iOS/Android native apps
  - Push notifications
  - Offline support

- [ ] **API Endpoints**
  - REST API
  - API authentication
  - Third-party integration

- [ ] **User Management**
  - Admin panel
  - Role management
  - Permission customization

### Ideas Welcome!

Have a feature idea? Open an issue with the tag `enhancement`.

---

## 📚 Resources

### Technologies Used

- **Flask Documentation:** https://flask.palletsprojects.com/
- **MySQL Documentation:** https://dev.mysql.com/doc/
- **Jinja2 Templates:** https://jinja.palletsprojects.com/
- **Werkzeug:** https://werkzeug.palletsprojects.com/

### Learning Resources

- Python Flask Tutorial
- MySQL Database Design
- Web Security Best Practices
- RESTful API Design

---

## 🙏 Acknowledgments

- Flask community for excellent documentation
- MySQL for reliable database engine
- All contributors and testers
- Educational institutions using this system

---

## 📋 Quick Reference

### Key Commands

```cmd
# Start application
python app.py

# Reset database
python reset_database.py

# Change passwords
python change_password.py

# Install dependencies
pip install -r requirements.txt

# Database import
mysql -u root -p < database\attendance_system.sql
```

### Default Credentials

```
Students: dood1@student.com / password
Coordinator: coordinator@college.com / password
HOD: hod@college.com / password
```

### Important Paths

```
Database Config: db_config.py (line 14)
Secret Key: app.py (line 13)
Upload Folder: uploads/
Templates: templates/
Static Files: static/
```

### Status Values

```
pending → approved_by_coordinator → approved
                  ↓
               rejected
```

---

<div align="center">

### Made with ❤️ for Education

**Version 2.1** • October 13, 2025

[⬆ Back to Top](#attendance-request--approval-system)

</div>
