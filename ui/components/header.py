"""
Application Header Component with University & Festival Branding.
"""

import os
from typing import Callable, Optional
import customtkinter as ctk
from PIL import Image

from config.settings import (
    BG_HEADER, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED,
    ACCENT_BLUE, ACCENT_BLUE_HOVER, BORDER_COLOR
)
from utils.font_manager import FontManager
from utils.resource_utils import resource_path
from core.localization import Localization

class Header(ctk.CTkFrame):
    def __init__(
        self,
        master,
        on_add_simulator: Callable[[], None],
        on_about: Callable[[], None],
        on_language_toggle: Callable[[], None],
        **kwargs
    ):
        super().__init__(
            master,
            fg_color=BG_HEADER,
            corner_radius=0,
            border_width=0,
            **kwargs
        )
        self.on_add_simulator = on_add_simulator
        self.on_about = on_about
        self.on_language_toggle = on_language_toggle

        self._build_ui()

    def _build_ui(self):
        # Configure grid: Left (Action Buttons), Center (Spacer), Right (Logo & Title) in RTL feel
        self.grid_columnconfigure(0, weight=1)  # Title / Branding
        self.grid_columnconfigure(1, weight=0)  # Controls

        # Container for Branding (Title + Logo)
        brand_frame = ctk.CTkFrame(self, fg_color="transparent")
        brand_frame.grid(row=0, column=0, padx=20, pady=8, sticky="w")

        # Load Logo
        logo_path = resource_path(os.path.join("assets", "branding", "icon.png"))
        if os.path.exists(logo_path):
            try:
                pil_logo = Image.open(logo_path).resize((40, 40), Image.Resampling.LANCZOS)
                self.logo_img = ctk.CTkImage(light_image=pil_logo, dark_image=pil_logo, size=(40, 40))
                logo_lbl = ctk.CTkLabel(brand_frame, image=self.logo_img, text="")
                logo_lbl.pack(side="left", padx=(0, 12))
            except Exception:
                pass

        # Title and Subtitle labels
        text_box = ctk.CTkFrame(brand_frame, fg_color="transparent")
        text_box.pack(side="left", fill="both")

        self.title_lbl = ctk.CTkLabel(
            text_box,
            text=Localization.tr("app_title"),
            font=FontManager.get_persian_font(size=16, weight="bold"),
            text_color=TEXT_PRIMARY,
            anchor="w"
        )
        self.title_lbl.pack(anchor="w")

        self.subtitle_lbl = ctk.CTkLabel(
            text_box,
            text=Localization.tr("app_subtitle"),
            font=FontManager.get_persian_font(size=11, weight="normal"),
            text_color=TEXT_SECONDARY,
            anchor="w"
        )
        self.subtitle_lbl.pack(anchor="w", pady=(1, 0))

        # Controls Container (Right side)
        ctrl_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctrl_frame.grid(row=0, column=1, padx=20, pady=8, sticky="e")

        # Add Simulator Button
        self.btn_add = ctk.CTkButton(
            ctrl_frame,
            text=Localization.tr("btn_add_simulator"),
            font=FontManager.get_persian_font(size=12, weight="bold"),
            fg_color=ACCENT_BLUE,
            hover_color=ACCENT_BLUE_HOVER,
            corner_radius=8,
            height=34,
            command=self.on_add_simulator
        )
        self.btn_add.pack(side="left", padx=6)

        # About Dialog Button
        self.btn_about = ctk.CTkButton(
            ctrl_frame,
            text=Localization.tr("btn_about"),
            font=FontManager.get_persian_font(size=12, weight="normal"),
            fg_color="#1e293b",
            hover_color="#334155",
            border_width=1,
            border_color=BORDER_COLOR,
            text_color=TEXT_PRIMARY,
            corner_radius=8,
            height=34,
            width=90,
            command=self.on_about
        )
        self.btn_about.pack(side="left", padx=6)

        # Language Switcher with vector globe icon
        curr_lang = Localization.get_language().upper()
        globe_path = resource_path(os.path.join("assets", "icons", "ui", "globe.png"))
        self.globe_img = None
        if os.path.exists(globe_path):
            try:
                pil_g = Image.open(globe_path).resize((14, 14), Image.Resampling.LANCZOS)
                self.globe_img = ctk.CTkImage(light_image=pil_g, dark_image=pil_g, size=(14, 14))
            except Exception:
                pass

        self.btn_lang = ctk.CTkButton(
            ctrl_frame,
            image=self.globe_img,
            text=f" {curr_lang}",
            font=FontManager.get_english_font(size=11, weight="bold"),
            fg_color="#1e293b",
            hover_color="#334155",
            border_width=1,
            border_color=BORDER_COLOR,
            text_color=TEXT_PRIMARY,
            corner_radius=8,
            height=34,
            width=78,
            command=self.on_language_toggle
        )
        self.btn_lang.pack(side="left", padx=6)

        # Bottom Border Line
        sep = ctk.CTkFrame(self, fg_color=BORDER_COLOR, height=1, corner_radius=0)
        sep.grid(row=1, column=0, columnspan=2, sticky="ew")

    def update_texts(self):
        """Refreshes text on language change."""
        self.title_lbl.configure(text=Localization.tr("app_title"))
        self.subtitle_lbl.configure(text=Localization.tr("app_subtitle"))
        self.btn_add.configure(text=Localization.tr("btn_add_simulator"))
        self.btn_about.configure(text=Localization.tr("btn_about"))
        curr_lang = Localization.get_language().upper()
        self.btn_lang.configure(text=f" {curr_lang}")
