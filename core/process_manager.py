"""
Child Process Execution & Lifecycle Manager.
Launches simulators with isolated working directories, prevents duplicate instances,
and manages bringing existing simulator windows to the foreground.
"""

import os
import sys
import time
import threading
import subprocess
from typing import Dict, List, Optional, Tuple, Callable
import psutil

from utils.window_utils import bring_pid_to_front

SIMULATOR_KEYWORDS: Dict[str, List[str]] = {
    "spectrometer": ["SpectroMeter", "Spectrometer", "Diffraction Grating", "اسپکترومتر", "طیف‌سنج"],
    "young_double_slit": ["Young", "Double Slit", "Double-Slit", "دوشکاف", "دو شکاف", "یانگ"]
}

class ProcessManager:
    def __init__(self):
        self.processes: Dict[str, subprocess.Popen] = {}
        self.starting_sims: set = set()

    def is_starting(self, sim_id: str) -> bool:
        return sim_id in self.starting_sims

    def is_running(self, sim_id: str) -> bool:
        """Returns True if the simulator process or any of its children are alive."""
        proc = self.processes.get(sim_id)
        if proc is not None:
            if proc.poll() is None:
                return True
            # Proc exited, clean up
            try:
                del self.processes[sim_id]
            except KeyError:
                pass

        # Also check system-wide by executable name to catch existing instances
        keywords = SIMULATOR_KEYWORDS.get(sim_id, [sim_id])
        for p in psutil.process_iter(['name']):
            try:
                name = p.info['name'].lower()
                if any(k.lower().replace(" ", "_") in name for k in keywords):
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        return False

    def get_related_pids(self, sim_id: str) -> List[int]:
        """Finds all PIDs associated with this simulator (parent + children)."""
        pids = []
        proc = self.processes.get(sim_id)
        if proc and proc.poll() is None:
            pids.append(proc.pid)
            try:
                children = psutil.Process(proc.pid).children(recursive=True)
                pids.extend([c.pid for c in children])
            except Exception:
                pass

        # Search matching process names in system
        keywords = SIMULATOR_KEYWORDS.get(sim_id, [sim_id])
        for p in psutil.process_iter(['pid', 'name']):
            try:
                name = p.info['name'].lower()
                if any(k.lower().replace(" ", "_") in name for k in keywords):
                    if p.info['pid'] not in pids:
                        pids.append(p.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        return pids

    def bring_to_front(self, sim_id: str) -> bool:
        """Brings the simulator's window to foreground via Win32 API."""
        pids = self.get_related_pids(sim_id)
        keywords = SIMULATOR_KEYWORDS.get(sim_id, [sim_id])
        if not pids and not keywords:
            return False

        target_pid = pids[0] if pids else 0
        child_pids = pids[1:] if len(pids) > 1 else []
        return bring_pid_to_front(target_pid, child_pids=child_pids, title_keywords=keywords)

    def launch(
        self,
        sim_id: str,
        exe_path: str,
        on_started: Optional[Callable[[bool, str], None]] = None
    ) -> Tuple[bool, str]:
        """
        Launches or focuses the simulator executable.
        If already running, brings it to foreground immediately.
        Otherwise spawns the process and monitors until window appears.
        """
        if self.is_running(sim_id):
            focused = self.bring_to_front(sim_id)
            msg = "شبیه‌ساز در حال اجراست و به جلوی تصویر آورده شد." if focused else "شبیه‌ساز در حال اجراست."
            if on_started:
                on_started(True, msg)
            return True, msg

        if not os.path.isfile(exe_path):
            msg = f"فایل اجرایی یافت نشد: {exe_path}"
            if on_started:
                on_started(False, msg)
            return False, msg

        working_dir = os.path.dirname(os.path.abspath(exe_path))

        if exe_path.lower().endswith(".py"):
            cmd = [sys.executable, os.path.abspath(exe_path)]
        else:
            cmd = [os.path.abspath(exe_path)]

        creation_flags = 0
        if sys.platform.startswith("win"):
            creation_flags = subprocess.CREATE_NEW_PROCESS_GROUP

        try:
            self.starting_sims.add(sim_id)
            proc = subprocess.Popen(
                cmd,
                cwd=working_dir,
                creationflags=creation_flags,
                shell=False
            )
            self.processes[sim_id] = proc

            # Monitor in background thread for window creation and bring to front
            def _wait_and_focus():
                try:
                    for _ in range(30):  # Wait up to 15 seconds (30 * 0.5s)
                        time.sleep(0.5)
                        if self.bring_to_front(sim_id):
                            break
                        if proc.poll() is not None:
                            break
                finally:
                    self.starting_sims.discard(sim_id)
                    if on_started:
                        on_started(True, "شبیه‌ساز با موفقیت اجرا و باز شد.")

            threading.Thread(target=_wait_and_focus, daemon=True).start()
            return True, "در حال راه‌اندازی شبیه‌ساز..."
        except Exception as e:
            self.starting_sims.discard(sim_id)
            msg = f"خطا در اجرای شبیه‌ساز: {e}"
            if on_started:
                on_started(False, msg)
            return False, msg

    def terminate_all(self):
        """Terminates all spawned simulator processes on app shutdown."""
        for sim_id, proc in list(self.processes.items()):
            if proc.poll() is None:
                try:
                    proc.terminate()
                except Exception:
                    pass
        self.processes.clear()
        self.starting_sims.clear()
