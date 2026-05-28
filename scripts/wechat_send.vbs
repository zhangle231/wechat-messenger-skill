Dim WshShell
Set WshShell = CreateObject("WScript.Shell")

' Win+9 to jump to 9th taskbar item (WeChat)
' {LWIN} represents the left Windows key
WshShell.SendKeys "{LWIN down}9{LWIN up}"
WScript.Sleep 600

' Open search (Ctrl+F)
WshShell.SendKeys "^f"
WScript.Sleep 800

' Type contact name
WshShell.SendKeys WScript.Arguments(0)
WScript.Sleep 1500

' Press Enter to open chat
WshShell.SendKeys "{ENTER}"
WScript.Sleep 800

' Type message
WshShell.SendKeys WScript.Arguments(1)
WScript.Sleep 500

' Send
WshShell.SendKeys "{ENTER}"

WScript.Echo "Done"