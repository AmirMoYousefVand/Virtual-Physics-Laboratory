import sys
import ctypes
from typing import List, Optional

def setup_windows_appid(app_id: str = "CFU.VirtualLaboratory.Launcher.1.0"):
    if sys.platform.startswith("win"):
        try:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        except Exception:
            pass

def force_foreground_window(hwnd: int) -> bool:
    """
    Bypasses Windows Focus-Stealing restrictions using AttachThreadInput and SwitchToThisWindow.
    Ensures the target simulator window is raised to the very top and gains keyboard/mouse focus.
    """
    if not sys.platform.startswith("win"):
        return False

    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32

    try:
        # Check if already foreground
        fg_hwnd = user32.GetForegroundWindow()
        if fg_hwnd == hwnd:
            return True

        # Restore if minimized (SW_RESTORE = 9)
        user32.ShowWindow(hwnd, 9)

        cur_thread_id = kernel32.GetCurrentThreadId()
        fore_thread_id = user32.GetWindowThreadProcessId(fg_hwnd, None)

        attached = False
        if cur_thread_id != fore_thread_id and fore_thread_id != 0:
            attached = bool(user32.AttachThreadInput(cur_thread_id, fore_thread_id, True))

        user32.BringWindowToTop(hwnd)
        user32.SetForegroundWindow(hwnd)

        if attached:
            user32.AttachThreadInput(cur_thread_id, fore_thread_id, False)

        try:
            user32.SwitchToThisWindow(hwnd, True)
        except Exception:
            pass

        return True
    except Exception as e:
        print(f"Warning: force_foreground_window failed: {e}")
        return False

def find_windows_for_pids(pids: List[int], title_keywords: Optional[List[str]] = None) -> List[int]:
    """
    Finds visible top-level windows matching any of the given PIDs or title keywords.
    """
    if not sys.platform.startswith("win"):
        return []

    user32 = ctypes.windll.user32
    matching_hwnds = []
    pid_set = set(pids)

    def enum_proc(hwnd, extra):
        if not user32.IsWindowVisible(hwnd):
            return True

        lpdw_pid = ctypes.c_ulong()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(lpdw_pid))
        win_pid = lpdw_pid.value

        # Check PID match
        if win_pid in pid_set:
            # Check non-empty title or proper window dimensions
            length = user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                matching_hwnds.append(hwnd)
            return True

        # Check Title keywords match
        if title_keywords:
            buf = ctypes.create_unicode_buffer(512)
            user32.GetWindowTextW(hwnd, buf, 512)
            win_title = buf.value.lower()
            if any(k.lower() in win_title for k in title_keywords):
                matching_hwnds.append(hwnd)

        return True

    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)
    user32.EnumWindows(WNDENUMPROC(enum_proc), 0)
    return matching_hwnds

def bring_pid_to_front(target_pid: int, child_pids: Optional[List[int]] = None, title_keywords: Optional[List[str]] = None) -> bool:
    all_pids = [target_pid]
    if child_pids:
        all_pids.extend(child_pids)

    hwnds = find_windows_for_pids(all_pids, title_keywords=title_keywords)
    if not hwnds:
        return False

    # Prefer the main window with largest title
    for hwnd in hwnds:
        force_foreground_window(hwnd)
    return True
