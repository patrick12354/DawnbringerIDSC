@echo off
echo ===========================================
echo   CorVision Engine Launcher
echo ===========================================
echo.
echo Menjalankan aplikasi Streamlit...
echo (Aplikasi akan terbuka otomatis di browser Anda)
echo.

set "SCRIPT_DIR=%~dp0"
set "ROOT_VENV_PYTHON=%SCRIPT_DIR%..\.venv\Scripts\python.exe"
set "LOCAL_VENV_PYTHON=%SCRIPT_DIR%.venv\Scripts\python.exe"

if exist "%ROOT_VENV_PYTHON%" (
    "%ROOT_VENV_PYTHON%" -m streamlit run "%SCRIPT_DIR%prototype\app.py"
) else if exist "%LOCAL_VENV_PYTHON%" (
    "%LOCAL_VENV_PYTHON%" -m streamlit run "%SCRIPT_DIR%prototype\app.py"
) else (
    echo [INFO] Virtual environment tidak ditemukan.
    echo Mencoba memakai Python dari PATH...
    py -m streamlit run "%SCRIPT_DIR%prototype\app.py" 2>nul
    if errorlevel 1 (
        python -m streamlit run "%SCRIPT_DIR%prototype\app.py" 2>nul
    )
    if errorlevel 1 (
        echo [ERROR] Python/Streamlit belum siap dipakai.
        echo Buat virtualenv dulu lalu install dependency:
        echo   cd /d "%SCRIPT_DIR%"
        echo   py -m venv ..\.venv
        echo   ..\.venv\Scripts\python -m pip install -r prototype\requirements.txt
    )
)

echo.
pause
