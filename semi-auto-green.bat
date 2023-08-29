cd E:\vscode\Program\semi-auto-green
start python test.py
set /p count=<./count.txt
start "" "C:\Program Files\Git\git-bash.exe" -c "git add .  && git commit -m %count% && git push"