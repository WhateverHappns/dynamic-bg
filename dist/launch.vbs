Set oShell = CreateObject ("WScript.Shell")
Dim strArgs
userProfile = oShell.ExpandEnvironmentStrings( "%userprofile%" )
strArgs = "cmd /c " & userProfile & "\dynamic-bg\dist\launch.bat"
oShell.Run strArgs, 0, false