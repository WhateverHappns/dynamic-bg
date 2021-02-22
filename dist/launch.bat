@echo off
FOR /f %%p in ('where pythonw') do SET PYTHONPATH=%%p
"%PYTHONPATH:"=%" "%USERPROFILE:"=%\dynamic-bg\main.py"
pause