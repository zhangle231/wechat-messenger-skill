# WeChat Messenger Skill

Auto-send messages to WeChat contacts via local Windows client. Uses `Win+9` hotkey to switch to WeChat and clipboard paste to bypass IME issues.

## ✨ Features

- 🚀 **Fully automated** - No manual window switching needed
- 📋 **Clipboard paste** - Bypasses Sogou Wubi IME issues
- 🎯 **Win+9 activation** - Auto-switches to WeChat via taskbar
- ✅ **Tested and working** - Successfully deployed and tested

## 📋 Prerequisites

1. **WeChat Windows client** installed and logged in
2. **WeChat pinned to taskbar position 9** (Win+9 to activate)
3. **Python 3.8+** with pywin32:
   ```bash
   pip install pywin32
   ```
4. **Anaconda Python** (recommended path: `D:\LEO\bin\anaconda3\python.exe`)

## 📦 Installation

### Option 1: Install via OpenClaw (Recommended)

```bash
skills install https://github.com/zhangle231/wechat-messenger-skill
```

### Option 2: Manual Install

1. Download `wechat-messenger.skill` from releases
2. Place in `~/.qclaw/skills/` directory
3. Restart OpenClaw Gateway

## 🚀 Usage

### Basic Usage

In OpenClaw, simply say:
```
给李鑫发消息：今天下午3点开会
```

The skill will:
1. Press `Win+9` to switch to WeChat
2. Open search with `Ctrl+F`
3. Paste contact name via clipboard
4. Send the message

### PowerShell Direct Call

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\zhang\.qclaw\skills\wechat-messenger\scripts\wechat_send.ps1" -Contact "李鑫" -Message "测试消息"
```

### Python Direct Call

```bash
& "D:\LEO\bin\anaconda3\python.exe" "C:\Users\zhang\.qclaw\skills\wechat-messenger\scripts\wechat_send_win9.py" "李鑫" "测试消息"
```

## ⚙️ Configuration

### Change Taskbar Position

If WeChat is not in position 9:

1. Open `scripts/wechat_send_win9.py`
2. Find line with `0x39` (keycode for '9')
3. Change to your taskbar position:
   - Position 1 → `0x31`
   - Position 2 → `0x32`
   - ...
   - Position 9 → `0x39`

### Multiple Contacts

Batch send (future feature):
```powershell
# TODO: Implement batch send in next version
```

## 🐛 Troubleshooting

### Win+9 doesn't switch to WeChat

- Check WeChat's taskbar position (count from left, starting at 1)
- Make sure WeChat is pinned to taskbar
- Try `Win+9` manually to verify

### Message not sent

1. Check if WeChat window activated (look for WeChat in foreground)
2. Verify contact name exactly matches WeChat display name
3. Check Python environment: `python -c "import win32clipboard"`

### Chinese characters garbled

- Skill uses clipboard paste, should handle Chinese correctly
- If issue persists, check system locale settings

## 📁 File Structure

```
wechat-messenger/
├── SKILL.md              # Skill definition and triggers
├── README.md             # This file
└── scripts/
    ├── wechat_send_win9.py   # Main Python script (Win+9 + clipboard)
    ├── wechat_send.ps1       # PowerShell wrapper
    └── wechat_send.vbs      # VBScript backup (not used currently)
```

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

MIT License - feel free to use and modify!

## 🙏 Acknowledgments

- OpenClaw team for the skill framework
- pywin32 for Windows automation
- Tested on Windows 10/11 with WeChat 3.x

## 📧 Contact

Zhang Le - [@zhangle231](https://github.com/zhangle231)

Project Link: https://github.com/zhangle231/wechat-messenger-skill

---

**⚠️ Note**: This skill is designed for personal automation. Please use responsibly and respect WeChat's terms of service.