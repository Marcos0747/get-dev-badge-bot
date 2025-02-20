@echo off
echo ============================================
echo Get Dev Badge Bot Setup
echo ============================================
echo This script will:
echo 1. Install the required dependencies.
echo 2. Ask for your bot token and save it in config.py.
echo ============================================

:: Install dependencies
echo.
echo Installing dependencies...
pip install discord.py requests
if %errorlevel% equ 0 (
    echo Dependencies installed successfully!
) else (
    echo Failed to install dependencies. Please check your Python and pip installation.
    pause
    exit /b
)

:: Bot token
echo.
echo Please enter your Discord bot token.
echo You can find it in the Discord Developer Portal under your application's settings.
set /p token=Enter your bot token: 

:: Create or update config.py
echo.
echo Creating/updating config.py...
(
    echo # [Bot config]
    echo token = "%token%"
) > config.py

if %errorlevel% equ 0 (
    echo config.py has been created/updated successfully!
) else (
    echo Failed to create/update config.py.
    pause
    exit /b
)

:: Completed
echo.
echo Setup completed successfully!
echo You can now run the bot using: python main.py
pause