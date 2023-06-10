@echo off

set PYTHON=python
set "VENV_DIR=%~dp0%venv"

%PYTHON% -c ""
if %ERRORLEVEL% == 0 goto :check_pip
echo Couldn't launch python
goto :enof

:check_pip
pip
if %ERRORLEVEL% == 0 goto :start_install
echo Couldn't install pip
goto :enof

:start_install
%PYTHON% -m venv "env"
set PENV=env\Scripts\python.exe
%PENV% env\Scripts\pip.exe install -r requirements.txt


:enof
pause
goto :eof