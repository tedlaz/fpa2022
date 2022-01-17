python create_pythoninit.py
pyinstaller  -F cfpa.py
copy .\dist\cfpa.exe C:\Users\tedla\prg\.
rd /S /Q dist
rd /S /Q build
del cfpa.spec