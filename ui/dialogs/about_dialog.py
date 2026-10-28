"""
About Software Modal Dialog.
Clean, concise, and professional presentation without fluff or emojis.
"""

import os
import customtkinter as ctk
from PIL import Image

from config.settings import (
    BG_MAIN, BG_CARD, BORDER_COLOR, TEXT_PRIMARY,
    TEXT_SECONDARY, TEXT_MUTED, ACCENT_BLUE, ACCENT_CYAN
)
from utils.font_manager import FontManager
from utils.resource_utils import resource_path, apply_window_icon
from core.localization import Localization

class AboutDialog(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=BG_MAIN, **kwargs)
        self.title("درباره نرم‌افزار")
        self.geometry("560x580")
        self.resizable(False, False)
        apply_window_icon(self)

        self.transient(master)
        self.grab_set()

        self._build_ui()
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self):
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=24, pady=20)

        # Logo
        logo_path = resource_path(os.path.join("assets", "branding", "icon.png"))
        if os.path.exists(logo_path):
            try:
                pil_logo = Image.open(logo_path).resize((60, 60), Image.Resampling.LANCZOS)
                self.logo_img = ctk.CTkImage(light_image=pil_logo, dark_image=pil_logo, size=(60, 60))
                lbl_logo = ctk.CTkLabel(content, image=self.logo_img, text="")
                lbl_logo.pack(pady=(0, 8))
            except Exception:
                pass

        # Title
        lbl_title = ctk.CTkLabel(
            content,
            text=Localization.tr("app_title"),
            font=FontManager.get_persian_font(size=18, weight="bold"),
            text_color=TEXT_PRIMARY
        )
        lbl_title.pack()

        lbl_sub = ctk.CTkLabel(
            content,
            text=Localization.tr("app_subtitle"),
            font=FontManager.get_persian_font(size=12),
            text_color=ACCENT_CYAN
        )
        lbl_sub.pack(pady=(2, 14))

        # Info Box (Card)
        info_card = ctk.CTkFrame(
            content,
            fg_color=BG_CARD,
            border_width=1,
            border_color=BORDER_COLOR,
            corner_radius=12
        )
        info_card.pack(fill="both", expand=True, padx=4, pady=4)

        info_text = (
            "نرم‌افزار آزمایشگاه مجازی فیزیک، بسته‌ای یکپارچه برای اجرای شبیه‌سازهای فیزیک تجربی و محاسباتی است.\n\n"
            "شبیه‌سازهای فعال:\n"
            "• اسپکترومتر اپتیکی: اندازه‌گیری گونیومتری با ورنیه، توری پراش و طیف نشری عناصر\n"
            "• آزمایش دوشکاف یانگ: اپتیک موجی، نمودار تحلیلی شدت نور و تجمع تک‌فوتون کوانتومی\n\n"
            "مشخصات فنی:\n"
            "• بسته کاملاً مستقل و قابل حمل (Portable) بدون نیاز به پیش‌نیاز نرم‌افزاری\n"
            "• قابلیت ثبت و اتصال شبیه‌سازهای جدید از طریق فرم تنظیمات\n"
            "• رابط کاربری دوزبانه (فارسی و انگلیسی) با فونت استاندارد وزیرمتن\n\n"
            "توسعه‌دهنده: امیرمحمد یوسف‌وند\n"
            "دانشگاه فرهنگیان — پردیس شهید باهنر اراک\n"
            "پاییز ۱۴۰۵"
        )

        txt_info = ctk.CTkLabel(
            info_card,
            text=info_text,
            font=FontManager.get_persian_font(size=11),
            text_color=TEXT_SECONDARY,
            justify="right",
            wraplength=460
        )
        txt_info.pack(padx=16, pady=16, fill="both")

        # Close button
        btn_close = ctk.CTkButton(
            content,
            text="بستن",
            font=FontManager.get_persian_font(size=13, weight="bold"),
            fg_color=ACCENT_BLUE,
            height=36,
            width=110,
            corner_radius=8,
            command=self.destroy
        )
        btn_close.pack(pady=(12, 0))
