@echo off
setlocal
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" goto install
where py >nul 2>nul
if errorlevel 1 goto use_python
py -3 -m venv ".venv"
if not errorlevel 1 goto install
:use_python
where python >nul 2>nul
if errorlevel 1 goto python_missing
python -m venv ".venv"
if errorlevel 1 goto fail
:install
if not exist ".venv\Scripts\python.exe" goto fail
".venv\Scripts\python.exe" -m pip install -r "requirements.txt"
if errorlevel 1 goto fail
echo Setup completed successfully.
pause
exit /b 0
:python_missing
echo Python not found. Install Python 3.
:fail
echo Setup failed. Check error above.
pause
exit /b 1
