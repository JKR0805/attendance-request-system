"""
Attendance Request & Approval System
Flask Application - Main Entry Point
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from db_config import db

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'  # Change this in production
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def login_required(role=None):
    """Decorator to check if user is logged in"""
    def decorator(f):
        def wrapper(*args, **kwargs):
            if 'user_id' not in session:
                flash('Please login first', 'error')
                return redirect(url_for('login'))
            if role and session.get('role') != role:
                flash('Unauthorized access', 'error')
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


# ==================== Student Routes ====================

@app.route('/student/register', methods=['GET', 'POST'])
def student_register():
    """Student registration"""
    if request.method == 'POST':
        name = request.form.get('name')
        department = request.form.get('department')
        contact = request.form.get('contact')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validate inputs
        if not all([name, department, contact, email, password]):
            flash('All fields are required', 'error')
            return redirect(url_for('student_register'))
        
        # Create student account
        result = db.create_student(name, department, contact, email, password)
        if result:
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('student_login'))
        else:
            flash('Registration failed. Email may already exist.', 'error')
    
    return render_template('student_register.html')


@app.route('/student/login', methods=['GET', 'POST'])
def student_login():
    """Student login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        student = db.verify_student_login(email, password)
        if student:
            session['user_id'] = student['student_id']
            session['name'] = student['name']
            session['role'] = 'student'
            session['email'] = student['email']
            flash(f'Welcome {student["name"]}!', 'success')
            return redirect(url_for('student_dashboard'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('student_login.html')


@app.route('/student/dashboard')
@login_required('student')
def student_dashboard():
    """Student dashboard - view requests"""
    student_id = session.get('user_id')
    requests = db.get_student_requests(student_id)
    return render_template('student_dashboard.html', requests=requests)


@app.route('/student/request', methods=['GET', 'POST'])
@login_required('student')
def student_request():
    """Submit new attendance request"""
    if request.method == 'POST':
        subject = request.form.get('subject')
        description = request.form.get('description')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        contact = request.form.get('contact')
        
        # Handle file upload
        attachment_path = None
        if 'attachment' in request.files:
            file = request.files['attachment']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"{timestamp}_{filename}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                attachment_path = filepath
        
        # Create request
        student_id = session.get('user_id')
        result = db.create_request(
            student_id, subject, description, 
            start_time, end_time, contact, attachment_path
        )
        
        if result:
            flash('Request submitted successfully!', 'success')
            return redirect(url_for('student_dashboard'))
        else:
            flash('Failed to submit request', 'error')
    
    return render_template('student_form.html')


# ==================== Coordinator Routes ====================

@app.route('/coordinator/login', methods=['GET', 'POST'])
def coordinator_login():
    """Coordinator login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = db.verify_user_login(email, password, 'coordinator')
        if user:
            session['user_id'] = user['user_id']
            session['name'] = user['name']
            session['role'] = 'coordinator'
            session['email'] = user['email']
            flash(f'Welcome {user["name"]}!', 'success')
            return redirect(url_for('coordinator_dashboard'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('coordinator_login.html')


@app.route('/coordinator/dashboard')
@login_required('coordinator')
def coordinator_dashboard():
    """Coordinator dashboard - view pending requests"""
    pending_requests = db.get_requests_by_status('pending')
    return render_template('coordinator.html', requests=pending_requests)


@app.route('/coordinator/action/<int:request_id>', methods=['POST'])
@login_required('coordinator')
def coordinator_action(request_id):
    """Coordinator approves or rejects request"""
    action = request.form.get('action')  # 'approve' or 'reject'
    remarks = request.form.get('remarks', '')
    
    if action == 'approve':
        db.update_request_status(request_id, 'approved_by_coordinator')
        db.create_approval(
            request_id, 'coordinator', session.get('name'), 
            'approved', remarks
        )
        flash('Request approved and forwarded to HOD', 'success')
    elif action == 'reject':
        db.update_request_status(request_id, 'rejected')
        db.create_approval(
            request_id, 'coordinator', session.get('name'), 
            'rejected', remarks
        )
        flash('Request rejected', 'success')
    
    return redirect(url_for('coordinator_dashboard'))


# ==================== HOD Routes ====================

@app.route('/hod/login', methods=['GET', 'POST'])
def hod_login():
    """HOD login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = db.verify_user_login(email, password, 'hod')
        if user:
            session['user_id'] = user['user_id']
            session['name'] = user['name']
            session['role'] = 'hod'
            session['email'] = user['email']
            flash(f'Welcome {user["name"]}!', 'success')
            return redirect(url_for('hod_dashboard'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('hod_login.html')


@app.route('/hod/dashboard')
@login_required('hod')
def hod_dashboard():
    """HOD dashboard - view coordinator-approved requests"""
    approved_requests = db.get_requests_by_status('approved_by_coordinator')
    return render_template('hod.html', requests=approved_requests)


@app.route('/hod/action/<int:request_id>', methods=['POST'])
@login_required('hod')
def hod_action(request_id):
    """HOD gives final approval or rejection"""
    action = request.form.get('action')  # 'approve' or 'reject'
    remarks = request.form.get('remarks', '')
    
    if action == 'approve':
        db.update_request_status(request_id, 'approved')
        db.create_approval(
            request_id, 'hod', session.get('name'), 
            'approved', remarks
        )
        flash('Request finally approved', 'success')
    elif action == 'reject':
        db.update_request_status(request_id, 'rejected')
        db.create_approval(
            request_id, 'hod', session.get('name'), 
            'rejected', remarks
        )
        flash('Request rejected', 'success')
    
    return redirect(url_for('hod_dashboard'))


# ==================== Common Routes ====================

@app.route('/request/view/<int:request_id>')
def view_request(request_id):
    """View detailed request information"""
    request_data = db.get_request_by_id(request_id)
    approvals = db.get_request_approvals(request_id)
    
    if not request_data:
        flash('Request not found', 'error')
        return redirect(url_for('index'))
    
    return render_template('view_request.html', 
                         request=request_data, 
                         approvals=approvals)


@app.route('/attachment/<int:request_id>')
def view_attachment(request_id):
    """View or download attachment for a request"""
    request_data = db.get_request_by_id(request_id)
    
    if not request_data or not request_data.get('attachment_path'):
        flash('Attachment not found', 'error')
        return redirect(url_for('index'))
    
    # Check if user is authorized
    if 'user_id' not in session:
        flash('Please login to view attachments', 'error')
        return redirect(url_for('index'))
    
    # Students can only view their own attachments
    if session.get('role') == 'student' and request_data['student_id'] != session.get('user_id'):
        flash('Unauthorized access', 'error')
        return redirect(url_for('student_dashboard'))
    
    file_path = request_data['attachment_path']
    
    if not os.path.exists(file_path):
        flash('Attachment file not found on server', 'error')
        return redirect(url_for('view_request', request_id=request_id))
    
    # Get filename and check if download is requested
    filename = os.path.basename(file_path)
    download = request.args.get('download', 'false').lower() == 'true'
    
    # Send file for viewing in browser or download
    return send_file(file_path, as_attachment=download, download_name=filename)


@app.route('/all-requests')
@login_required()
def all_requests():
    """View all requests with filters - accessible by all logged-in users"""
    role = session.get('role')
    user_id = session.get('user_id')
    
    # Get filter parameters
    status_filter = request.args.get('status', 'all')
    search_query = request.args.get('search', '')
    
    if role == 'student':
        # Students see only their requests
        if status_filter == 'all':
            requests = db.execute_query(
                """SELECT * FROM requests 
                   WHERE student_id = %s 
                   ORDER BY created_at DESC""",
                (user_id,),
                fetch=True
            )
        else:
            requests = db.execute_query(
                """SELECT * FROM requests 
                   WHERE student_id = %s AND status = %s 
                   ORDER BY created_at DESC""",
                (user_id, status_filter),
                fetch=True
            )
    else:
        # Coordinators and HODs see all requests
        if status_filter == 'all':
            requests = db.execute_query(
                """SELECT r.*, s.name as student_name, s.department, s.email 
                   FROM requests r
                   JOIN students s ON r.student_id = s.student_id
                   ORDER BY r.created_at DESC""",
                fetch=True
            )
        else:
            requests = db.execute_query(
                """SELECT r.*, s.name as student_name, s.department, s.email 
                   FROM requests r
                   JOIN students s ON r.student_id = s.student_id
                   WHERE r.status = %s
                   ORDER BY r.created_at DESC""",
                (status_filter,),
                fetch=True
            )
    
    # Apply search filter if provided
    if search_query and requests:
        search_lower = search_query.lower()
        requests = [
            r for r in requests 
            if search_lower in r.get('subject', '').lower() 
            or search_lower in r.get('description', '').lower()
            or (r.get('student_name') and search_lower in r.get('student_name', '').lower())
        ]
    
    # Calculate statistics
    stats = {
        'total': len(requests) if requests else 0,
        'pending': 0,
        'approved_by_coordinator': 0,
        'approved': 0,
        'rejected': 0
    }
    
    if requests:
        for r in requests:
            stats[r['status']] = stats.get(r['status'], 0) + 1
    
    return render_template('all_requests.html', 
                         requests=requests,
                         stats=stats,
                         current_filter=status_filter,
                         search_query=search_query)


@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))


# ==================== Error Handlers ====================

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


# ==================== Template Filters ====================

@app.template_filter('datetime')
def format_datetime(value):
    """Format datetime for display"""
    if value:
        return value.strftime('%d-%m-%Y %I:%M %p')
    return ''


@app.template_filter('date')
def format_date(value):
    """Format date for display"""
    if value:
        return value.strftime('%d-%m-%Y')
    return ''


if __name__ == '__main__':
    # Connect to database
    if db.connect():
        print("Database connected successfully!")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("Failed to connect to database. Please check your configuration.")
