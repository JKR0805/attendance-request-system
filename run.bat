@echo off
echo Starting Attendance Request System...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if activation was successful
if %errorlevel% neq 0 (
    echo ERROR: Could not activate virtual environment
    echo Please run setup.bat first
    pause
    exit /b 1
)

REM Run the Flask application
python app.py

pause
