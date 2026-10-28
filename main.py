"""
Entry Point for CFU Virtual Physics Laboratory Suite.
Farhangian University Educational & Laboratory Festival.
Author: Amirmohammad Yousefvand
"""

import sys
import os
import traceback

# Ensure UTF-8 output on Windows console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from utils.window_utils import setup_windows_appid
from utils.font_manager import FontManager
from ui.main_window import MainWindow

def log_unhandled_exception(exc_type, exc_value, exc_traceback):
    log_path = os.path.join(os.getenv("TEMP", "."), "cfu_virtual_lab_crash.log")
    err_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(f"CRITICAL ERROR:\n{err_msg}", file=sys.stderr)
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n--- CRASH REPORT ---\n{err_msg}\n")
    except Exception:
        pass

def main():
    sys.excepthook = log_unhandled_exception

    # 1. Register Windows App ID for distinct Taskbar grouping
    setup_windows_appid("CFU.VirtualLaboratory.Launcher.1.0")

    # 2. Pre-load fonts into Windows GDI
    FontManager.initialize()

    # 3. Start Application
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
