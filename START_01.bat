@echo off
setlocal
set "ROOT=%~dp0"
if not exist "%ROOT%.venv\Scripts\python.exe" goto no_venv
pushd "%ROOT%practice_01_client_server\src"
if errorlevel 1 goto bad_path
"%ROOT%.venv\Scripts\python.exe" "init_db.py"
if errorlevel 1 goto run_failed
"%ROOT%.venv\Scripts\python.exe" "check_db.py"
if errorlevel 1 goto run_failed
echo Program finished.
popd
pause
exit /b 0
:run_failed
echo Program returned an error. See above.
popd
pause
exit /b 1
:bad_path
echo Cannot enter project src folder.
pause
exit /b 1
:no_venv
echo Run SETUP_FIRST.bat first.
pause
exit /b 1
