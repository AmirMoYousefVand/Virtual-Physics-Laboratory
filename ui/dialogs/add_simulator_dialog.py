"""
Add Simulator Modal Dialog.
Allows users to register additional simulators (EXE or Python) dynamically,
persisting them to config/simulators.json without recompilation.
"""

import os
import re
from typing import Callable, List, Dict
import customtkinter as ctk
from tkinter import filedialog, messagebox

from config.settings import (
    BG_MAIN, BG_CARD, BG_INPUT, BORDER_COLOR, TEXT_PRIMARY,
    TEXT_SECONDARY, ACCENT_BLUE, ACCENT_BLUE_HOVER, ACCENT_AMBER
)
from utils.font_manager import FontManager
from utils.resource_utils import apply_window_icon
from core.localization import Localization
from core.config_manager import ConfigManager

class AddSimulatorDialog(ctk.CTkToplevel):
    def __init__(
        self,
        master,
        config_manager: ConfigManager,
        on_added: Callable[[], None],
        **kwargs
    ):
        super().__init__(master, fg_color=BG_MAIN, **kwargs)
        self.config_manager = config_manager
        self.on_added = on_added

        self.title(Localization.tr("dlg_add_title"))
        self.geometry("620x720")
        self.resizable(False, False)
        apply_window_icon(self)

        # Modal focus
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
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=24, pady=20)

        # Title Header
        header_lbl = ctk.CTkLabel(
            scroll,
            text=Localization.tr("dlg_add_title"),
            font=FontManager.get_persian_font(size=16, weight="bold"),
            text_color=TEXT_PRIMARY,
            anchor="w"
        )
        header_lbl.pack(fill="x", pady=(0, 16))

        # 1. Title FA
        self._create_field_label(scroll, Localization.tr("dlg_field_title_fa"))
        self.entry_title_fa = self._create_entry(scroll, placeholder="مثال: شبیه‌ساز سقوط آزاد و مقاومت هوا")

        # 2. Title EN
        self._create_field_label(scroll, Localization.tr("dlg_field_title_en"))
        self.entry_title_en = self._create_entry(scroll, placeholder="e.g. Free Fall & Air Resistance Simulator")

        # 3. Category Selector
        self._create_field_label(scroll, Localization.tr("dlg_field_category"))
        cats = self.config_manager.get_categories()
        cat_options = [c.get("name_fa", c["id"]) for c in cats if c["id"] != "all"]
        self.cat_map = {c.get("name_fa", c["id"]): c["id"] for c in cats}
        self.combo_cat = ctk.CTkComboBox(
            scroll,
            values=cat_options,
            font=FontManager.get_persian_font(size=12),
            height=36,
            fg_color=BG_INPUT,
            border_color=BORDER_COLOR,
            button_color=ACCENT_BLUE
        )
        self.combo_cat.pack(fill="x", pady=(0, 12))
        if cat_options:
            self.combo_cat.set(cat_options[0])

        # 4. Executable File (with Browse)
        self._create_field_label(scroll, Localization.tr("dlg_field_exe"))
        exe_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        exe_frame.pack(fill="x", pady=(0, 12))

        self.entry_exe = self._create_entry(exe_frame, placeholder="مسیر فایل exe یا py...")
        self.entry_exe.pack(side="left", fill="x", expand=True, padx=(0, 8))

        btn_browse_exe = ctk.CTkButton(
            exe_frame,
            text=Localization.tr("dlg_btn_browse"),
            font=FontManager.get_persian_font(size=12),
            fg_color="#1e293b",
            hover_color="#334155",
            border_width=1,
            border_color=BORDER_COLOR,
            width=100,
            height=36,
            command=self._browse_exe
        )
        btn_browse_exe.pack(side="right")

        # 5. Icon File (with Browse)
        self._create_field_label(scroll, Localization.tr("dlg_field_icon"))
        icon_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        icon_frame.pack(fill="x", pady=(0, 12))

        self.entry_icon = self._create_entry(icon_frame, placeholder="مسیر فایل png یا ico...")
        self.entry_icon.pack(side="left", fill="x", expand=True, padx=(0, 8))

        btn_browse_icon = ctk.CTkButton(
            icon_frame,
            text=Localization.tr("dlg_btn_browse"),
            font=FontManager.get_persian_font(size=12),
            fg_color="#1e293b",
            hover_color="#334155",
            border_width=1,
            border_color=BORDER_COLOR,
            width=100,
            height=36,
            command=self._browse_icon
        )
        btn_browse_icon.pack(side="right")

        # 6. Description
        self._create_field_label(scroll, Localization.tr("dlg_field_desc"))
        self.txt_desc = ctk.CTkTextbox(
            scroll,
            height=85,
            font=FontManager.get_persian_font(size=12),
            fg_color=BG_INPUT,
            border_color=BORDER_COLOR,
            border_width=1,
            text_color=TEXT_PRIMARY
        )
        self.txt_desc.pack(fill="x", pady=(0, 12))

        # 7. Tags
        self._create_field_label(scroll, Localization.tr("dlg_field_tags"))
        self.entry_tags = self._create_entry(scroll, placeholder="مکانیک, شتاب, گرانش, سقوط")

        # Action Buttons
        btn_box = ctk.CTkFrame(self, fg_color="transparent")
        btn_box.pack(fill="x", padx=24, pady=16, side="bottom")

        btn_save = ctk.CTkButton(
            btn_box,
            text=Localization.tr("dlg_btn_save"),
            font=FontManager.get_persian_font(size=13, weight="bold"),
            fg_color=ACCENT_BLUE,
            hover_color=ACCENT_BLUE_HOVER,
            height=40,
            command=self._save_simulator
        )
        btn_save.pack(side="left", fill="x", expand=True, padx=(0, 8))

        btn_cancel = ctk.CTkButton(
            btn_box,
            text=Localization.tr("dlg_btn_cancel"),
            font=FontManager.get_persian_font(size=13),
            fg_color="#1e293b",
            hover_color="#334155",
            height=40,
            width=100,
            command=self.destroy
        )
        btn_cancel.pack(side="right")

    def _create_field_label(self, parent, text: str):
        lbl = ctk.CTkLabel(
            parent,
            text=text,
            font=FontManager.get_persian_font(size=12, weight="bold"),
            text_color=TEXT_SECONDARY,
            anchor="w"
        )
        lbl.pack(fill="x", pady=(4, 2))

    def _create_entry(self, parent, placeholder: str = "") -> ctk.CTkEntry:
        entry = ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            font=FontManager.get_persian_font(size=12),
            height=36,
            fg_color=BG_INPUT,
            border_color=BORDER_COLOR,
            border_width=1,
            text_color=TEXT_PRIMARY
        )
        entry.pack(fill="x", pady=(0, 8))
        return entry

    def _browse_exe(self):
        filetypes = [
            ("Executable Files & Python", "*.exe;*.py"),
            ("Executable Files (*.exe)", "*.exe"),
            ("Python Scripts (*.py)", "*.py"),
            ("All Files", "*.*")
        ]
        fpath = filedialog.askopenfilename(title="انتخاب فایل اجرایی شبیه‌ساز", filetypes=filetypes)
        if fpath:
            self.entry_exe.delete(0, "end")
            self.entry_exe.insert(0, os.path.normpath(fpath))

    def _browse_icon(self):
        filetypes = [
            ("Image Files", "*.png;*.ico;*.jpg;*.jpeg"),
            ("All Files", "*.*")
        ]
        fpath = filedialog.askopenfilename(title="انتخاب آیکون شبیه‌ساز", filetypes=filetypes)
        if fpath:
            self.entry_icon.delete(0, "end")
            self.entry_icon.insert(0, os.path.normpath(fpath))

    def _save_simulator(self):
        title_fa = self.entry_title_fa.get().strip()
        exe_path = self.entry_exe.get().strip()

        if not title_fa or not exe_path:
            messagebox.showwarning("خطای ورودی", Localization.tr("dlg_err_missing_fields"))
            return

        if not os.path.isfile(exe_path):
            messagebox.showerror("خطای مسیر", Localization.tr("dlg_err_exe_not_found"))
            return

        title_en = self.entry_title_en.get().strip() or title_fa
        selected_cat_name = self.combo_cat.get()
        cat_id = self.cat_map.get(selected_cat_name, "general")
        icon_path = self.entry_icon.get().strip()
        desc = self.txt_desc.get("1.0", "end").strip()
        tags_raw = self.entry_tags.get().strip()
        tags = [t.strip() for t in tags_raw.replace("،", ",").split(",") if t.strip()]

        # Generate unique ID
        sim_id = re.sub(r"[^a-zA-Z0-9_]", "_", title_en.lower()).strip("_")
        if not sim_id or len(sim_id) < 3:
            sim_id = f"sim_{len(self.config_manager.get_simulators()) + 1}"

        new_sim = {
            "id": sim_id,
            "title_fa": title_fa,
            "title_en": title_en,
            "category": cat_id,
            "description_fa": desc,
            "description_en": desc,
            "executable": exe_path,
            "fallback_path": exe_path,
            "icon": icon_path,
            "author_fa": "استاد / دانشجو",
            "version": "1.0.0",
            "tags": tags
        }

        success = self.config_manager.add_simulator(new_sim)
        if success:
            messagebox.showinfo("موفقیت", "شبیه‌ساز جدید با موفقیت به سامانه آزمایشگاه افزوده شد.")
            self.on_added()
            self.destroy()
        else:
            messagebox.showerror("خطا", "خطایی در ذخیره فایل تنظیمات رخ داد.")
