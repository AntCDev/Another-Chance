@echo off

:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

:: Reaching here means Python is installed.
:: Execute stuff...
pip install -r requirements.txt

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:neof

:errorNoPython
echo Error^: Python not installed, please make sure you have installed Python 3 and it's added to PATH. It can be obtained at https://www.python.org

:neof
pause
goto:eof