-- Database: attendance_system
-- MySQL Schema for Attendance Request & Approval System

-- Create Database
CREATE DATABASE IF NOT EXISTS attendance_system;
USE attendance_system;

-- Table: students
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    contact VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: users (Coordinators and HODs)
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    role ENUM('coordinator', 'hod') NOT NULL,
    department VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: requests
CREATE TABLE IF NOT EXISTS requests (
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
);

-- Table: approvals
CREATE TABLE IF NOT EXISTS approvals (
    approval_id INT PRIMARY KEY AUTO_INCREMENT,
    request_id INT NOT NULL,
    approver_role ENUM('coordinator', 'hod') NOT NULL,
    approver_name VARCHAR(100) NOT NULL,
    decision ENUM('approved', 'rejected') NOT NULL,
    remarks TEXT,
    decision_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES requests(request_id) ON DELETE CASCADE
);

-- Insert sample data

-- Sample Students
INSERT INTO students (name, department, contact, email, password) VALUES
('DOOD1', 'Computer Science', '9876543210', 'dood1@student.com', '5f4dcc3b5aa765d61d8327deb882cf99'), -- password: password
('DOOD2', 'Information Technology', '9876543211', 'dood2@student.com', '5f4dcc3b5aa765d61d8327deb882cf99'),
('DOOD3', 'Electronics', '9876543212', 'dood3@student.com', '5f4dcc3b5aa765d61d8327deb882cf99');

-- Sample Users (Coordinators and HODs)
INSERT INTO users (name, role, department, email, password) VALUES
('COORD1', 'coordinator', 'Computer Science', 'coordinator@college.com', '5f4dcc3b5aa765d61d8327deb882cf99'), -- password: password
('HOD1', 'hod', 'Computer Science', 'hod@college.com', '5f4dcc3b5aa765d61d8327deb882cf99'); -- password: password

-- Sample Requests (for testing)
INSERT INTO requests (student_id, subject, description, start_time, end_time, contact, status) VALUES
(1, 'Workshop Attendance', 'Need permission to attend Python Workshop at Tech Hub', '2025-10-15 09:00:00', '2025-10-15 17:00:00', '9876543210', 'pending'),
(2, 'Hackathon Participation', 'Participating in National Level Hackathon', '2025-10-20 08:00:00', '2025-10-22 18:00:00', '9876543211', 'pending');

-- Create indexes for better performance
CREATE INDEX idx_requests_status ON requests(status);
CREATE INDEX idx_requests_student ON requests(student_id);
CREATE INDEX idx_approvals_request ON approvals(request_id);

-- Display tables
SHOW TABLES;
