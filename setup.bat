@echo off
echo ================================================
echo Attendance Request System - Setup Script
echo ================================================
echo.

echo [1/5] Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    echo Please ensure Python is installed and in PATH
    pause
    exit /b 1
)
echo Virtual environment created successfully!
echo.

echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat
echo.

echo [3/5] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully!
echo.

echo [4/5] Creating uploads directory...
if not exist "uploads" mkdir uploads
echo Uploads directory ready!
echo.

echo [5/5] Setup complete!
echo.
echo ================================================
echo Next Steps:
echo ================================================
echo 1. Start MySQL Server
echo 2. Run: mysql -u root -p ^< database\attendance_system.sql
echo 3. Update database credentials in db_config.py
echo 4. Run: python app.py
echo 5. Open browser: http://localhost:5000
echo ================================================
echo.
echo Press any key to exit...
pause >nul
