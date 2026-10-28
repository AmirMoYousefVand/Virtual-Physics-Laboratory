"""
Application Footer Component with Developer Credits, GitHub Link & Copyright.
"""

import os
import webbrowser
import customtkinter as ctk
from PIL import Image

from config.settings import BG_HEADER, TEXT_MUTED, TEXT_PRIMARY, BORDER_COLOR, ACCENT_BLUE_HOVER
from utils.font_manager import FontManager
from utils.resource_utils import resource_path
from core.localization import Localization

GITHUB_PROFILE_URL = "https://github.com/AmirMoYousefVand"

class Footer(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color=BG_HEADER,
            corner_radius=0,
            border_width=0,
            **kwargs
        )
        self._build_ui()

    def _build_ui(self):
        # Top border
        sep = ctk.CTkFrame(self, fg_color=BORDER_COLOR, height=1, corner_radius=0)
        sep.pack(fill="x", side="top")

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="x", padx=24, pady=8)

        # Left: Developer Credit
        self.credits_lbl = ctk.CTkLabel(
            content,
            text=Localization.tr("footer_credits"),
            font=FontManager.get_persian_font(size=11),
            text_color=TEXT_MUTED
        )
        self.credits_lbl.pack(side="left")

        # Center / Right: GitHub Profile Button
        gh_path = resource_path(os.path.join("assets", "branding", "github-mark.png"))
        self.gh_img = None
        if os.path.exists(gh_path):
            try:
                pil_gh = Image.open(gh_path).resize((16, 16), Image.Resampling.LANCZOS)
                self.gh_img = ctk.CTkImage(light_image=pil_gh, dark_image=pil_gh, size=(16, 16))
            except Exception:
                pass

        self.btn_github = ctk.CTkButton(
            content,
            image=self.gh_img,
            text="GitHub",
            font=FontManager.get_english_font(size=11, weight="bold"),
            fg_color="transparent",
            hover_color="#1e293b",
            text_color=TEXT_PRIMARY,
            corner_radius=8,
            height=28,
            width=90,
            cursor="hand2",
            command=self._open_github
        )
        self.btn_github.pack(side="right", padx=(8, 0))

        # Rights / Year
        self.rights_lbl = ctk.CTkLabel(
            content,
            text=Localization.tr("footer_rights"),
            font=FontManager.get_persian_font(size=11),
            text_color=TEXT_MUTED
        )
        self.rights_lbl.pack(side="right", padx=12)

    def _open_github(self):
        webbrowser.open_new_tab(GITHUB_PROFILE_URL)

    def update_texts(self):
        self.credits_lbl.configure(text=Localization.tr("footer_credits"))
        self.rights_lbl.configure(text=Localization.tr("footer_rights"))
