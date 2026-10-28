"""
Interactive Card Component for a Single Simulator.
Displays icon, title, description, category badge, live running status,
and dynamic launch/focus action button.
"""

import os
from typing import Dict, Any, Callable
import customtkinter as ctk
from PIL import Image

from config.settings import (
    BG_CARD, BG_CARD_HOVER, BORDER_COLOR, BORDER_ACTIVE,
    TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED,
    ACCENT_BLUE, ACCENT_BLUE_HOVER, ACCENT_EMERALD, ACCENT_AMBER,
    STATUS_RUNNING_BG, STATUS_RUNNING_TEXT
)
from utils.font_manager import FontManager
from utils.resource_utils import resource_path
from core.localization import Localization

class SimulatorCard(ctk.CTkFrame):
    def __init__(
        self,
        master,
        sim_data: Dict[str, Any],
        icon_path: str,
        is_available: bool,
        is_running: bool,
        on_launch: Callable[[str], None],
        **kwargs
    ):
        super().__init__(
            master,
            fg_color=BG_CARD,
            corner_radius=14,
            border_width=1,
            border_color=BORDER_COLOR,
            **kwargs
        )
        self.sim_data = sim_data
        self.sim_id = sim_data.get("id", "")
        self.icon_path = icon_path
        self.is_available = is_available
        self.is_running = is_running
        self.is_starting = False
        self.on_launch = on_launch

        self._build_ui()
        self._bind_hover(self)

    def _build_ui(self):
        lang = Localization.get_language()

        # Inner padding frame
        self.inner = ctk.CTkFrame(self, fg_color="transparent")
        self.inner.pack(fill="both", expand=True, padx=20, pady=18)

        # 1. Top Bar: Category Pill (Left) & Status Badge (Right)
        top_bar = ctk.CTkFrame(self.inner, fg_color="transparent")
        top_bar.pack(fill="x", pady=(0, 12))

        cat_name = self.sim_data.get("category", "General")

        # Load category icon
        self.cat_img = None
        cat_icon_path = resource_path(os.path.join("assets", "icons", "ui", "folder.png"))
        if os.path.exists(cat_icon_path):
            try:
                pil_f = Image.open(cat_icon_path).resize((13, 13), Image.Resampling.LANCZOS)
                self.cat_img = ctk.CTkImage(light_image=pil_f, dark_image=pil_f, size=(13, 13))
            except Exception:
                pass

        self.cat_badge = ctk.CTkLabel(
            top_bar,
            image=self.cat_img,
            compound="left",
            text=f" {cat_name}",
            font=FontManager.get_persian_font(size=11, weight="bold"),
            text_color="#38bdf8",
            fg_color="#0c2340",
            corner_radius=12,
            height=26,
            padx=10
        )
        self.cat_badge.pack(side="left")

        # Load status icons
        self._load_status_icons()

        self.status_badge = ctk.CTkLabel(
            top_bar,
            text="",
            font=FontManager.get_persian_font(size=11, weight="bold"),
            corner_radius=12,
            height=26,
            padx=10
        )
        self.status_badge.pack(side="right")
        self._update_status_badge()

        # 2. Main Content: Icon + Title
        content_frame = ctk.CTkFrame(self.inner, fg_color="transparent")
        content_frame.pack(fill="x", pady=(0, 10))

        # Icon
        self.icon_img = None
        if os.path.exists(self.icon_path):
            try:
                pil_icon = Image.open(self.icon_path).resize((64, 64), Image.Resampling.LANCZOS)
                self.icon_img = ctk.CTkImage(light_image=pil_icon, dark_image=pil_icon, size=(64, 64))
                icon_lbl = ctk.CTkLabel(content_frame, image=self.icon_img, text="")
                icon_lbl.pack(side="left", padx=(0, 14))
            except Exception:
                pass

        # Titles Frame
        title_box = ctk.CTkFrame(content_frame, fg_color="transparent")
        title_box.pack(side="left", fill="both", expand=True)

        title_fa = self.sim_data.get("title_fa", "")
        self.title_lbl = ctk.CTkLabel(
            title_box,
            text=title_fa if lang == "fa" else self.sim_data.get("title_en", title_fa),
            font=FontManager.get_persian_font(size=15, weight="bold"),
            text_color=TEXT_PRIMARY,
            anchor="w",
            justify="left"
        )
        self.title_lbl.pack(anchor="w")

        title_en = self.sim_data.get("title_en", "")
        if title_en:
            self.sub_lbl = ctk.CTkLabel(
                title_box,
                text=title_en if lang == "fa" else title_fa,
                font=FontManager.get_english_font(size=11, weight="normal"),
                text_color=TEXT_SECONDARY,
                anchor="w"
            )
            self.sub_lbl.pack(anchor="w", pady=(2, 0))

        # 3. Description (Wrapped)
        desc_fa = self.sim_data.get("description_fa", "")
        desc_en = self.sim_data.get("description_en", desc_fa)
        self.desc_lbl = ctk.CTkLabel(
            self.inner,
            text=desc_fa if lang == "fa" else desc_en,
            font=FontManager.get_persian_font(size=11),
            text_color=TEXT_SECONDARY,
            wraplength=480,
            justify="left",
            anchor="w"
        )
        self.desc_lbl.pack(fill="x", pady=(4, 12))

        # 4. Tags
        tags = self.sim_data.get("tags", [])
        if tags:
            tags_frame = ctk.CTkFrame(self.inner, fg_color="transparent")
            tags_frame.pack(fill="x", pady=(0, 14))
            for t in tags[:5]:
                t_lbl = ctk.CTkLabel(
                    tags_frame,
                    text=f"#{t}",
                    font=FontManager.get_persian_font(size=10),
                    text_color=TEXT_MUTED,
                    fg_color="#1e293b",
                    corner_radius=8,
                    height=22,
                    padx=8
                )
                t_lbl.pack(side="left", padx=3)

        # 5. Footer Line & Action Button
        footer = ctk.CTkFrame(self.inner, fg_color="transparent")
        footer.pack(fill="x", side="bottom")

        # Author info
        author = self.sim_data.get("author_fa", "")
        ver = self.sim_data.get("version", "1.0.0")
        self.info_lbl = ctk.CTkLabel(
            footer,
            text=f"{author} | v{ver}",
            font=FontManager.get_persian_font(size=10),
            text_color=TEXT_MUTED
        )
        self.info_lbl.pack(side="left")

        # Launch Button
        self.btn_launch = ctk.CTkButton(
            footer,
            text=self._get_launch_btn_text(),
            font=FontManager.get_persian_font(size=13, weight="bold"),
            fg_color=self._get_launch_btn_color(),
            hover_color=ACCENT_BLUE_HOVER,
            corner_radius=10,
            height=38,
            width=170,
            command=self._on_click_launch
        )
        self.btn_launch.pack(side="right")

    def _get_launch_btn_text(self) -> str:
        if not self.is_available:
            return Localization.tr("status_unavailable")
        if self.is_starting:
            return Localization.tr("btn_starting")
        if self.is_running:
            return Localization.tr("btn_running")
        return Localization.tr("btn_launch")

    def _get_launch_btn_color(self) -> str:
        if not self.is_available:
            return "#334155"
        if self.is_starting:
            return "#d97706"  # Amber
        if self.is_running:
            return "#059669"  # Emerald
        return ACCENT_BLUE

    def _load_status_icons(self):
        ui_icon_dir = resource_path(os.path.join("assets", "icons", "ui"))
        self.icon_alert = self._load_single_icon(os.path.join(ui_icon_dir, "alert.png"), (12, 12))
        self.icon_running = self._load_single_icon(os.path.join(ui_icon_dir, "dot_running.png"), (10, 10))
        self.icon_ready = self._load_single_icon(os.path.join(ui_icon_dir, "dot_ready.png"), (10, 10))
        self.icon_starting = self._load_single_icon(os.path.join(ui_icon_dir, "dot_starting.png"), (10, 10))

    def _load_single_icon(self, path: str, size: tuple):
        if os.path.exists(path):
            try:
                pil_im = Image.open(path).resize(size, Image.Resampling.LANCZOS)
                return ctk.CTkImage(light_image=pil_im, dark_image=pil_im, size=size)
            except Exception:
                pass
        return None

    def _update_status_badge(self):
        if not self.is_available:
            self.status_badge.configure(
                image=self.icon_alert,
                compound="left",
                text=f" {Localization.tr('status_unavailable')}",
                text_color=ACCENT_AMBER,
                fg_color="#382405"
            )
        elif self.is_starting:
            self.status_badge.configure(
                image=self.icon_starting,
                compound="left",
                text=f" {Localization.tr('status_starting')}",
                text_color="#fbbf24",
                fg_color="#451a03"
            )
        elif self.is_running:
            self.status_badge.configure(
                image=self.icon_running,
                compound="left",
                text=f" {Localization.tr('status_running')}",
                text_color=STATUS_RUNNING_TEXT,
                fg_color=STATUS_RUNNING_BG
            )
        else:
            self.status_badge.configure(
                image=self.icon_ready,
                compound="left",
                text=f" {Localization.tr('status_ready')}",
                text_color=TEXT_MUTED,
                fg_color="#1e293b"
            )

    def set_running_state(self, is_running: bool, is_available: bool, is_starting: bool = False):
        """Dynamic refresh from poll loop."""
        changed = (
            self.is_running != is_running or
            self.is_available != is_available or
            self.is_starting != is_starting
        )
        self.is_running = is_running
        self.is_available = is_available
        self.is_starting = is_starting

        if changed:
            self._update_status_badge()
            self.btn_launch.configure(
                text=self._get_launch_btn_text(),
                fg_color=self._get_launch_btn_color(),
                state="normal" if is_available else "disabled"
            )

    def _on_click_launch(self):
        if self.is_available:
            # Immediate feedback
            self.set_running_state(self.is_running, self.is_available, is_starting=True)
            self.on_launch(self.sim_id)

    def _bind_hover(self, widget):
        if isinstance(widget, ctk.CTkButton):
            return
        widget.bind("<Enter>", lambda e: self.configure(border_color=BORDER_ACTIVE, fg_color=BG_CARD_HOVER))
        widget.bind("<Leave>", lambda e: self.configure(border_color=BORDER_COLOR, fg_color=BG_CARD))
        for child in widget.winfo_children():
            self._bind_hover(child)
