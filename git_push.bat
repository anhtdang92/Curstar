@echo off
REM Script to add, commit, and push all changes to origin main

set /p msg="Enter commit message: "
git add .
git commit -m "%msg%"
git push origin main

pause 