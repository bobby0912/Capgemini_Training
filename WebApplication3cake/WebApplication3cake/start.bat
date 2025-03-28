@echo off
start /B cmd /c "dotnet run"
timeout /t 5 /nobreak >nul
cd ExpenseFrontend
npm start
