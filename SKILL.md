---
name: wechat-messenger
description: "WeChat auto-messaging skill. Send messages to WeChat contacts via local Windows client. Triggers when user asks to: send WeChat message, message someone on WeChat, chat with a contact. Supports single and batch messages. Uses clipboard paste to bypass IME issues."
---

# WeChat Messenger

Auto-send messages to WeChat contacts via local Windows client.

## Prerequisites

- WeChat Windows client running and logged in
- WeChat pinned to **taskbar position 9** (required for auto-activation)
- Python with pywin32: `pip install pywin32`

## Quick Send

Single message:
```
& "D:\LEO\bin\anaconda3\python.exe" "C:\Users\zhang\.qclaw\skills\wechat-messenger\scripts\wechat_send_win9.py" "联系人" "内容"
```

Or via PowerShell wrapper:
```
powershell -ExecutionPolicy Bypass -File "C:\Users\zhang\.qclaw\skills\wechat-messenger\scripts\wechat_send.ps1" -Contact "联系人" -Message "内容"
```

## How It Works

1. **Activate WeChat** - Presses `Win+9` to jump to 9th taskbar item
2. **Search** - `Ctrl+F` opens search, paste contact name via clipboard
3. **Open chat** - Press Enter
4. **Send** - Paste message via clipboard, press Enter

## Key Rules

1. **Always use clipboard paste** for Chinese text. SendKeys direct input breaks with IME (Sogou Wubi)
2. **Wait between steps** - 500-1500ms delays required
3. **Exact contact name** - Must match WeChat display name exactly
4. **Confirm** with user before sending important messages

## Troubleshooting

### Win+9 doesn't work
- Check WeChat's taskbar position (count from left, starting at 1)
- If different, modify `wechat_send_win9.py` line: change `0x39` (key 9) to the correct key

### Python import error
- Use full path: `& "D:\LEO\bin\anaconda3\python.exe"`
- Or install pywin32: `pip install pywin32`
