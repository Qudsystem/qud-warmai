@echo off
echo Starting Continuous Development System for SHΔDØW CORE V99...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Start the auto-checkpoint system in a separate window
start "Auto-Checkpoint System" cmd /c "python auto_checkpoint.py"

REM Run the model selector to show current task recommendations
echo.
echo Current Task Recommendations:
echo =============================
python model_selector.py

echo.
echo Continuous Development System is now running!
echo Auto-checkpoint system is saving progress to progress.txt.
echo.
echo Press any key to exit...
pause >nul