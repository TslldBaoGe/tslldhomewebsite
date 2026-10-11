@echo off
rem Miniconda needs Library\bin on PATH or the ssl module's DLLs fail to load
set "PATH=F:\Miniconda39;F:\Miniconda39\Library\bin;%PATH%"
cd /d "%~dp0"
echo Starting backend on http://127.0.0.1:8001 ...
.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
