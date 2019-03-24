Set objFSO = CreateObject("Scripting.FileSystemObject")
Set wshShell = WScript.CreateObject( "WScript.Shell" )
appName = InputBox("Inserisci il nome del progetto")
objFSO.CopyFolder "apps\_template", "apps\" & appName
