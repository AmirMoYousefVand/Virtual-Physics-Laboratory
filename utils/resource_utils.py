import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

def get_base_dir() -> str:
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.normpath(os.path.join(sys._MEIPASS, relative_path))
    return os.path.normpath(os.path.join(get_base_dir(), relative_path))

def apply_window_icon(window: tk.Wm):
    ico_path = resource_path(os.path.join("assets", "branding", "favicon.ico"))
    png_path = resource_path(os.path.join("assets", "branding", "icon.png"))

    if os.path.exists(ico_path):
        try:
            window.iconbitmap(ico_path)
        except Exception:
            pass

    if os.path.exists(png_path):
        try:
            pil_img = Image.open(png_path).resize((64, 64), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(pil_img)
            window.iconphoto(False, photo)
            window._app_icon_ref = photo
        except Exception:
            pass
