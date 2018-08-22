Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "bin\python\pythonw.exe scripts\executor.py"
oShell.Run strArgs, 0, false