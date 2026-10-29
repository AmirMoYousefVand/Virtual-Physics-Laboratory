"""
Application configuration, visual theme parameters, and global constants.
"""

APP_NAME_FA = "آزمایشگاه مجازی فیزیک"
APP_SUBTITLE_FA = "مجموعه شبیه‌سازهای تعاملی فیزیک"
APP_NAME_EN = "Virtual Physics Laboratory"
APP_SUBTITLE_EN = "Interactive Physics Simulation Suite"
APP_VERSION = "1.0.0"

# Window Settings (Optimized for 1280x720, 1366x768 & low-res displays)
WINDOW_DEFAULT_WIDTH = 1160
WINDOW_DEFAULT_HEIGHT = 650
WINDOW_MIN_WIDTH = 900
WINDOW_MIN_HEIGHT = 560

# Theme Settings
APPEARANCE_MODE = "Dark"  # "Dark" or "Light"
DEFAULT_COLOR_THEME = "blue"

# Color Palette (Tailwind / Slate / Cyan Modern Dark)
BG_MAIN = "#0b0f19"             # Deep slate dark background
BG_HEADER = "#0f172a"           # Header / toolbar dark
BG_CARD = "#172033"             # Card base
BG_CARD_HOVER = "#1e293b"       # Card hover
BG_SIDEBAR = "#0d1322"          # Filter sidebar / panel
BG_INPUT = "#0f172a"            # Search entry background

BORDER_COLOR = "#293548"        # Subtle card border
BORDER_ACTIVE = "#38bdf8"       # Focused/active border

TEXT_PRIMARY = "#f8fafc"        # High-contrast white
TEXT_SECONDARY = "#94a3b8"      # Medium muted
TEXT_MUTED = "#64748b"          # Low-contrast helper text

ACCENT_BLUE = "#0284c7"         # Primary blue
ACCENT_BLUE_HOVER = "#0369a1"
ACCENT_CYAN = "#06b6d4"         # Cyan highlight
ACCENT_EMERALD = "#10b981"      # Running status green
ACCENT_AMBER = "#f59e0b"        # Warning / attention
ACCENT_ROSE = "#f43f5e"         # Error / danger

STATUS_RUNNING_BG = "#064e3b"   # Emerald badge bg
STATUS_RUNNING_TEXT = "#34d399" # Emerald badge text

# Polling Interval
STATUS_CHECK_INTERVAL_MS = 1000
