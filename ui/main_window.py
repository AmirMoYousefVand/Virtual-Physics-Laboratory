"""
Main Window Controller for CFU Virtual Laboratory Suite.
Coordinates header, search/filter bar, responsive simulator card grid,
footer, and lifecycle polling loop.
"""

from typing import Optional
import customtkinter as ctk
from tkinter import messagebox

from config.settings import (
    APP_NAME_FA, WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT,
    WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT, BG_MAIN,
    STATUS_CHECK_INTERVAL_MS, APPEARANCE_MODE, DEFAULT_COLOR_THEME
)
from utils.resource_utils import apply_window_icon
from core.config_manager import ConfigManager
from core.process_manager import ProcessManager
from core.localization import Localization
from ui.components.header import Header
from ui.components.filter_bar import FilterBar
from ui.components.simulator_grid import SimulatorGrid
from ui.components.footer import Footer
from ui.dialogs.add_simulator_dialog import AddSimulatorDialog
from ui.dialogs.about_dialog import AboutDialog

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Appearance configuration
        ctk.set_appearance_mode(APPEARANCE_MODE)
        ctk.set_default_color_theme(DEFAULT_COLOR_THEME)

        # Core subsystems
        self.config_manager = ConfigManager()
        self.process_manager = ProcessManager()

        # Window configuration
        self.title(APP_NAME_FA)
        self.geometry(f"{WINDOW_DEFAULT_WIDTH}x{WINDOW_DEFAULT_HEIGHT}")
        self.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.configure(fg_color=BG_MAIN)
        apply_window_icon(self)
        self._center_window()

        self._active_category = "all"
        self._active_query = ""
        self._poll_job: Optional[str] = None

        self._build_ui()
        self._refresh_content()
        self._start_status_polling()

        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _center_window(self):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = max(0, (sw - WINDOW_DEFAULT_WIDTH) // 2)
        y = max(0, (sh - WINDOW_DEFAULT_HEIGHT) // 2)
        self.geometry(f"{WINDOW_DEFAULT_WIDTH}x{WINDOW_DEFAULT_HEIGHT}+{x}+{y}")

    def _build_ui(self):
        # 1. Header
        self.header = Header(
            self,
            on_add_simulator=self._open_add_dialog,
            on_about=self._open_about_dialog,
            on_language_toggle=self._toggle_language
        )
        self.header.pack(fill="x", side="top")

        # 2. Filter Bar
        self.filter_bar = FilterBar(
            self,
            categories=self.config_manager.get_categories(),
            on_filter_changed=self._on_filter_changed
        )
        self.filter_bar.pack(fill="x", side="top")

        # 3. Main Grid of Simulators
        self.grid_view = SimulatorGrid(
            self,
            config_manager=self.config_manager,
            process_manager=self.process_manager,
            on_launch=self._launch_simulator
        )
        self.grid_view.pack(fill="both", expand=True, side="top")

        # 4. Footer
        self.footer = Footer(self)
        self.footer.pack(fill="x", side="bottom")

    def _refresh_content(self):
        sims = self.config_manager.filter_simulators(
            category=self._active_category,
            query=self._active_query
        )
        self.grid_view.populate(sims)
        self.filter_bar.update_count(len(sims))

    def _on_filter_changed(self, category: str, query: str):
        self._active_category = category
        self._active_query = query
        self._refresh_content()

    def _launch_simulator(self, sim_id: str):
        sim = next((s for s in self.config_manager.get_simulators() if s.get("id") == sim_id), None)
        if not sim:
            messagebox.showerror("خطا", "شبیه‌ساز در رجیستری یافت نشد.")
            return

        exe_path = self.config_manager.resolve_executable_path(sim)
        if not exe_path:
            messagebox.showerror(
                "خطای فایل اجرایی",
                f"فایل اجرایی شبیه‌ساز «{sim.get('title_fa')}» در مسیر مشخص شده یافت نشد.\n\n"
                f"مسیر تعریف‌شده: {sim.get('executable')}"
            )
            return

        def _on_started_cb(ok: bool, info_msg: str):
            try:
                self.after(0, self.grid_view.update_states)
            except Exception:
                pass

        success, msg = self.process_manager.launch(sim_id, exe_path, on_started=_on_started_cb)
        if not success:
            messagebox.showerror("خطا در اجرا", msg)
        self.grid_view.update_states()

    def _start_status_polling(self):
        self.grid_view.update_states()
        self._poll_job = self.after(STATUS_CHECK_INTERVAL_MS, self._start_status_polling)

    def _open_add_dialog(self):
        AddSimulatorDialog(self, config_manager=self.config_manager, on_added=self._on_simulator_added)

    def _on_simulator_added(self):
        self._refresh_content()

    def _open_about_dialog(self):
        AboutDialog(self)

    def _toggle_language(self):
        new_lang = "en" if Localization.get_language() == "fa" else "fa"
        Localization.set_language(new_lang)

        # Update text across views
        self.title(Localization.tr("app_title"))
        self.header.update_texts()
        self.filter_bar.update_texts()
        self.footer.update_texts()
        self._refresh_content()

    def _on_close(self):
        if self._poll_job:
            try:
                self.after_cancel(self._poll_job)
            except Exception:
                pass
        self.destroy()
