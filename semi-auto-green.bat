cd E:\vscode\Program\semi-auto-green
start python test.py
set /p count=<./count.txt
start "" "C:\Program Files\Git\git-bash.exe" -c "cd=E:\vscode\Program\semi-auto-green && git commit -m %count%;bash"