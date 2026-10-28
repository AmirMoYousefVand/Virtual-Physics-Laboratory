import os
import sys
import ctypes
from typing import Optional
import customtkinter as ctk
from utils.resource_utils import resource_path

class FontManager:
    _INITIALIZED = False
    _FONT_DIR = resource_path(os.path.join("assets", "fonts"))

    PERSIAN_FAMILY = "Vazirmatn"
    ENGLISH_FAMILY = "Space Grotesk"
    MONO_FAMILY = "Consolas"

    @classmethod
    def initialize(cls):
        if cls._INITIALIZED:
            return

        font_files = [
            os.path.join(cls._FONT_DIR, "Vazirmatn-Regular.ttf"),
            os.path.join(cls._FONT_DIR, "Vazirmatn-Bold.ttf"),
            os.path.join(cls._FONT_DIR, "SpaceGrotesk.ttf")
        ]

        if sys.platform.startswith("win"):
            for fpath in font_files:
                if os.path.exists(fpath):
                    abs_path = os.path.abspath(fpath)
                    try:
                        ctypes.windll.gdi32.AddFontResourceExW(abs_path, 0x10, 0)
                    except Exception as e:
                        print(f"Warning: GDI font load failed for {fpath}: {e}")

        cls._INITIALIZED = True

    @classmethod
    def get_persian_font(cls, size: int = 13, weight: str = "normal") -> ctk.CTkFont:
        cls.initialize()
        return ctk.CTkFont(family=cls.PERSIAN_FAMILY, size=size, weight=weight)

    @classmethod
    def get_english_font(cls, size: int = 12, weight: str = "normal") -> ctk.CTkFont:
        cls.initialize()
        return ctk.CTkFont(family=cls.ENGLISH_FAMILY, size=size, weight=weight)

    @classmethod
    def get_mono_font(cls, size: int = 11, weight: str = "normal") -> ctk.CTkFont:
        return ctk.CTkFont(family=cls.MONO_FAMILY, size=size, weight=weight)
