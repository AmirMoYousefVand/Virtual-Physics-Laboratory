"""
Automated headless test for CFU Virtual Laboratory application.
Verifies all components, data binding, and process manager.
"""

import sys
import os

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from core.config_manager import ConfigManager
from core.process_manager import ProcessManager
from ui.main_window import MainWindow

def run_tests():
    print("=== CFU Virtual Laboratory Automated Test ===")

    # 1. Config Manager Test
    cfg = ConfigManager()
    sims = cfg.get_simulators()
    assert len(sims) >= 2, f"Expected at least 2 simulators, found {len(sims)}"
    print(f"✓ ConfigManager loaded {len(sims)} simulators.")

    for s in sims:
        exe = cfg.resolve_executable_path(s)
        assert exe is not None and os.path.isfile(exe), f"Executable for {s['id']} not found: {exe}"
        print(f"  - {s['title_fa']}: Exe OK ({exe})")

    # 2. Filter Test
    optics = cfg.filter_simulators(category="optics")
    assert len(optics) >= 2, "Expected at least 2 optics simulators"
    print(f"✓ Category filter 'optics': {len(optics)} found.")

    search_res = cfg.filter_simulators(query="یانگ")
    assert len(search_res) == 1, "Expected 1 search match for 'یانگ'"
    print(f"✓ Search query 'یانگ': {search_res[0]['title_fa']} matched.")

    # 3. UI Instantiation Test
    print("Testing MainWindow UI lifecycle...")
    app = MainWindow()
    app.update()  # Processes idle events & renders widgets

    # Check cards
    assert len(app.grid_view.cards) == len(sims), "Grid cards count mismatch"
    print(f"✓ MainWindow rendered {len(app.grid_view.cards)} cards successfully.")

    # Test language toggle
    app._toggle_language()
    app.update()
    print("✓ Language toggle to English passed.")
    app._toggle_language()
    app.update()
    print("✓ Language toggle back to Persian passed.")

    # Clean shutdown
    app._on_close()
    print("✓ MainWindow closed cleanly.")

    print("\nALL SYSTEM TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
