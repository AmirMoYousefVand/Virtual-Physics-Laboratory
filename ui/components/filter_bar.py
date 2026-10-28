"""
Filter & Search Bar Component.
Provides real-time search across titles, descriptions, and tags,
with interactive category filter pills and live simulator counter.
"""

from typing import Callable, List, Dict
import customtkinter as ctk

from config.settings import (
    BG_HEADER, BG_INPUT, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED,
    ACCENT_BLUE, BORDER_COLOR, ACCENT_CYAN
)
from utils.font_manager import FontManager
from core.localization import Localization

class FilterBar(ctk.CTkFrame):
    def __init__(
        self,
        master,
        categories: List[Dict[str, str]],
        on_filter_changed: Callable[[str, str], None],
        **kwargs
    ):
        super().__init__(
            master,
            fg_color=BG_HEADER,
            corner_radius=0,
            border_width=0,
            **kwargs
        )
        self.categories = categories
        self.on_filter_changed = on_filter_changed
        self.current_category = "all"
        self.category_buttons: Dict[str, ctk.CTkButton] = {}

        self._build_ui()

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=0)  # Search input
        self.grid_columnconfigure(1, weight=1)  # Category pills
        self.grid_columnconfigure(2, weight=0)  # Count pill

        # 1. Search Box
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.grid(row=0, column=0, padx=(24, 16), pady=12, sticky="w")

        self.search_var = ctk.StringVar()
        self.search_var.trace_add("write", self._on_search_input)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            textvariable=self.search_var,
            placeholder_text=Localization.tr("search_placeholder"),
            font=FontManager.get_persian_font(size=12),
            width=320,
            height=38,
            corner_radius=10,
            fg_color=BG_INPUT,
            border_color=BORDER_COLOR,
            border_width=1,
            text_color=TEXT_PRIMARY
        )
        self.search_entry.pack(side="left")

        # 2. Category Pills
        pills_frame = ctk.CTkFrame(self, fg_color="transparent")
        pills_frame.grid(row=0, column=1, padx=8, pady=12, sticky="w")

        lang = Localization.get_language()
        for cat in self.categories:
            cid = cat["id"]
            name = cat.get(f"name_{lang}", cat.get("name_fa", cid))

            is_active = (cid == self.current_category)
            btn = ctk.CTkButton(
                pills_frame,
                text=name,
                font=FontManager.get_persian_font(size=12, weight="bold" if is_active else "normal"),
                fg_color=ACCENT_BLUE if is_active else "#1e293b",
                hover_color="#0284c7" if is_active else "#334155",
                border_width=0 if is_active else 1,
                border_color=BORDER_COLOR,
                text_color=TEXT_PRIMARY if is_active else TEXT_SECONDARY,
                corner_radius=20,
                height=32,
                command=lambda c=cid: self._select_category(c)
            )
            btn.pack(side="left", padx=4)
            self.category_buttons[cid] = btn

        # 3. Count indicator pill
        self.count_badge = ctk.CTkLabel(
            self,
            text=Localization.tr("total_simulators", count=0),
            font=FontManager.get_persian_font(size=12, weight="bold"),
            text_color=ACCENT_CYAN,
            fg_color="#132338",
            corner_radius=16,
            height=32,
            padx=14
        )
        self.count_badge.grid(row=0, column=2, padx=(8, 24), pady=12, sticky="e")

        # Bottom Border
        sep = ctk.CTkFrame(self, fg_color=BORDER_COLOR, height=1, corner_radius=0)
        sep.grid(row=1, column=0, columnspan=3, sticky="ew")

    def _select_category(self, cat_id: str):
        self.current_category = cat_id
        for cid, btn in self.category_buttons.items():
            is_active = (cid == cat_id)
            btn.configure(
                fg_color=ACCENT_BLUE if is_active else "#1e293b",
                hover_color="#0284c7" if is_active else "#334155",
                border_width=0 if is_active else 1,
                text_color=TEXT_PRIMARY if is_active else TEXT_SECONDARY,
                font=FontManager.get_persian_font(size=12, weight="bold" if is_active else "normal")
            )
        self.on_filter_changed(self.current_category, self.search_var.get())

    def _on_search_input(self, *args):
        self.on_filter_changed(self.current_category, self.search_var.get())

    def update_count(self, count: int):
        self.count_badge.configure(text=Localization.tr("total_simulators", count=count))

    def update_texts(self):
        self.search_entry.configure(placeholder_text=Localization.tr("search_placeholder"))
        lang = Localization.get_language()
        for cat in self.categories:
            cid = cat["id"]
            if cid in self.category_buttons:
                name = cat.get(f"name_{lang}", cat.get("name_fa", cid))
                self.category_buttons[cid].configure(text=name)
