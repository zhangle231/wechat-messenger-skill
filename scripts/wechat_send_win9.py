import ctypes
import time
import sys

contact = sys.argv[1] if len(sys.argv) > 1 else "李鑫"
message = sys.argv[2] if len(sys.argv) > 2 else "Python自动发送"

# Simulate Win+9 using keybd_event
VK_LWIN = 0x5B

def key_down(vk):
    ctypes.windll.user32.keybd_event(vk, 0, 0, 0)

def key_up(vk):
    ctypes.windll.user32.keybd_event(vk, 0, 2, 0)

# Press Win+9 to jump to 9th taskbar item
key_down(VK_LWIN)
time.sleep(0.05)
ctypes.windll.user32.keybd_event(0x39, 0, 0, 0)  # '9' key
time.sleep(0.05)
ctypes.windll.user32.keybd_event(0x39, 0, 2, 0)  # '9' key up
key_up(VK_LWIN)
time.sleep(0.7)

# Now use ctypes to send Ctrl+F
VK_CONTROL = 0x11
ctypes.windll.user32.keybd_event(VK_CONTROL, 0, 0, 0)
ctypes.windll.user32.keybd_event(0x46, 0, 0, 0)  # 'F' key
time.sleep(0.05)
ctypes.windll.user32.keybd_event(0x46, 0, 2, 0)
ctypes.windll.user32.keybd_event(VK_CONTROL, 0, 2, 0)
time.sleep(0.8)

# Type contact name using clipboard (more reliable for Chinese)
import win32clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(contact)
win32clipboard.CloseClipboard()

# Paste
VK_CONTROL = 0x11
ctypes.windll.user32.keybd_event(VK_CONTROL, 0, 0, 0)
ctypes.windll.user32.keybd_event(0x56, 0, 0, 0)  # 'V' key
time.sleep(0.05)
ctypes.windll.user32.keybd_event(0x56, 0, 2, 0)
ctypes.windll.user32.keybd_event(VK_CONTROL, 0, 2, 0)
time.sleep(1.5)

# Press Enter
ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)  # Enter
time.sleep(0.05)
ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)
time.sleep(0.8)

# Type message using clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(message)
win32clipboard.CloseClipboard()

# Paste
ctypes.windll.user32.keybd_event(VK_CONTROL, 0, 0, 0)
ctypes.windll.user32.keybd_event(0x56, 0, 0, 0)
time.sleep(0.05)
ctypes.windll.user32.keybd_event(0x56, 0, 2, 0)
ctypes.windll.user32.keybd_event(VK_CONTROL, 0, 2, 0)
time.sleep(0.5)

# Press Enter to send
ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
time.sleep(0.05)
ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)

print("Message sent to", contact)
