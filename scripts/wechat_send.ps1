# WeChat Auto Sender - PowerShell Wrapper
# Uses wechat_send_win9.py (Python + keybd_event + clipboard)

param(
    [Parameter(Mandatory=$true)]
    [string]$Contact,
    
    [Parameter(Mandatory=$true)]
    [string]$Message
)

$pyScript = Join-Path $PSScriptRoot "wechat_send_win9.py"
$python = "D:\LEO\bin\anaconda3\python.exe"

& $python $pyScript $Contact $Message