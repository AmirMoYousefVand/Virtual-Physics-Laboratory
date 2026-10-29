"""
Responsive Grid Container for Simulator Cards with Real-time State Updates.
Adapts column count (1 vs 2) based on viewport width for 1280x720 and 1024x768 screens.
"""

from typing import List, Dict, Any, Callable
import customtkinter as ctk

from config.settings import BG_MAIN, TEXT_MUTED
from utils.font_manager import FontManager
from ui.components.simulator_card import SimulatorCard
from core.config_manager import ConfigManager
from core.process_manager import ProcessManager

class SimulatorGrid(ctk.CTkScrollableFrame):
    def __init__(
        self,
        master,
        config_manager: ConfigManager,
        process_manager: ProcessManager,
        on_launch: Callable[[str], None],
        **kwargs
    ):
        super().__init__(
            master,
            fg_color=BG_MAIN,
            corner_radius=0,
            **kwargs
        )
        self.config_manager = config_manager
        self.process_manager = process_manager
        self.on_launch = on_launch

        self.cards: Dict[str, SimulatorCard] = {}
        self._current_sims: List[Dict[str, Any]] = []
        self._current_cols = 2

        self.grid_columnconfigure(0, weight=1, uniform="col")
        self.grid_columnconfigure(1, weight=1, uniform="col")

        self.bind("<Configure>", self._on_resize)

    def _on_resize(self, event):
        new_cols = 2 if event.width >= 920 else 1
        if new_cols != self._current_cols:
            self._current_cols = new_cols
            self._regrid_cards()

    def _regrid_cards(self):
        if self._current_cols == 1:
            self.grid_columnconfigure(1, weight=0, uniform="")
            self.grid_columnconfigure(0, weight=1, uniform="")
        else:
            self.grid_columnconfigure(0, weight=1, uniform="col")
            self.grid_columnconfigure(1, weight=1, uniform="col")

        card_list = list(self.cards.values())
        for idx, card in enumerate(card_list):
            row = idx if self._current_cols == 1 else idx // 2
            col = 0 if self._current_cols == 1 else idx % 2
            card.grid_configure(row=row, column=col, padx=10, pady=8, sticky="nsew")

    def populate(self, simulators: List[Dict[str, Any]]):
        """Rebuilds cards for the given filtered simulator list."""
        self._current_sims = simulators

        for card in self.cards.values():
            card.destroy()
        self.cards.clear()

        for child in self.winfo_children():
            child.destroy()

        if not simulators:
            empty_lbl = ctk.CTkLabel(
                self,
                text="هیچ شبیه‌سازی با این مشخصات یافت نشد.\nمی‌توانید با دکمه «+ افزودن شبیه‌ساز» شبیه‌ساز جدید اضافه کنید.",
                font=FontManager.get_persian_font(size=13),
                text_color=TEXT_MUTED
            )
            empty_lbl.grid(row=0, column=0, columnspan=2, pady=60)
            return

        for idx, sim in enumerate(simulators):
            sim_id = sim.get("id", "")
            exe_path = self.config_manager.resolve_executable_path(sim)
            is_available = (exe_path is not None)
            is_running = self.process_manager.is_running(sim_id)
            icon_path = self.config_manager.resolve_icon_path(sim)

            row = idx if self._current_cols == 1 else idx // 2
            col = 0 if self._current_cols == 1 else idx % 2

            card = SimulatorCard(
                self,
                sim_data=sim,
                icon_path=icon_path,
                is_available=is_available,
                is_running=is_running,
                on_launch=self.on_launch
            )
            card.grid(row=row, column=col, padx=10, pady=8, sticky="nsew")
            self.cards[sim_id] = card

    def update_states(self):
        """Polled periodically to update running state of visible cards."""
        for sim_id, card in self.cards.items():
            sim = card.sim_data
            exe_path = self.config_manager.resolve_executable_path(sim)
            is_available = (exe_path is not None)
            is_running = self.process_manager.is_running(sim_id)
            is_starting = self.process_manager.is_starting(sim_id)
            card.set_running_state(is_running, is_available, is_starting)
