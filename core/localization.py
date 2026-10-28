"""
Bilingual localization service (Persian & English) with clean typography.
Ensures zero emoji usage and correct native font rendering without corrupted bidi reversal.
"""

import re
from typing import Dict, Any

def clean_persian_text(text: str) -> str:
    """Removes stray directional control marks that cause square glyphs on Windows."""
    if not text:
        return ""
    return re.sub(r"[‎‏‪-‮⁦-⁩]", "", str(text))

TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "app_title": {
      "fa": "آزمایشگاه مجازی فیزیک",
      "en": "Virtual Physics Laboratory"
    },
    "app_subtitle": {
      "fa": "مجموعه شبیه‌سازهای تعاملی فیزیک",
      "en": "Interactive Physics Simulation Suite"
    },
    "search_placeholder": {
      "fa": "جستجو در عنوان، توضیحات یا تگ‌های شبیه‌سازها...",
      "en": "Search in titles, descriptions, or tags..."
    },
    "all_categories": {
      "fa": "همه شبیه‌سازها",
      "en": "All Simulators"
    },
    "total_simulators": {
      "fa": "تعداد شبیه‌سازها: {count}",
      "en": "Simulators: {count}"
    },
    "btn_add_simulator": {
      "fa": "+ افزودن شبیه‌ساز",
      "en": "+ Add Simulator"
    },
    "btn_about": {
      "fa": "درباره نرم‌افزار",
      "en": "About Software"
    },
    "btn_launch": {
      "fa": "ورود به شبیه‌ساز",
      "en": "Launch Simulator"
    },
    "btn_starting": {
      "fa": "در حال راه‌اندازی...",
      "en": "Starting..."
    },
    "btn_running": {
      "fa": "در حال اجرا (تمرکز)",
      "en": "Running (Focus)"
    },
    "status_ready": {
      "fa": "آماده اجرا",
      "en": "Ready"
    },
    "status_starting": {
      "fa": "در حال راه‌اندازی",
      "en": "Starting"
    },
    "status_running": {
      "fa": "در حال اجرا",
      "en": "Running"
    },
    "status_unavailable": {
      "fa": "فایل یافت نشد",
      "en": "Not Found"
    },
    "author_label": {
      "fa": "طراح و توسعه‌دهنده:",
      "en": "Author:"
    },
    "version_label": {
      "fa": "نسخه:",
      "en": "Version:"
    },
    "category_label": {
      "fa": "دسته‌بندی:",
      "en": "Category:"
    },
    # Add Simulator Dialog
    "dlg_add_title": {
      "fa": "افزودن شبیه‌ساز جدید",
      "en": "Add New Simulator"
    },
    "dlg_field_title_fa": {
      "fa": "عنوان فارسی:",
      "en": "Persian Title:"
    },
    "dlg_field_title_en": {
      "fa": "عنوان انگلیسی (اختیاری):",
      "en": "English Title (Optional):"
    },
    "dlg_field_category": {
      "fa": "دسته‌بندی موضوعی:",
      "en": "Subject Category:"
    },
    "dlg_field_exe": {
      "fa": "مسیر فایل اجرایی (EXE یا Python):",
      "en": "Executable File Path (EXE / Python):"
    },
    "dlg_field_icon": {
      "fa": "مسیر فایل آیکون (اختیاری):",
      "en": "Icon File Path (Optional):"
    },
    "dlg_field_desc": {
      "fa": "توضیحات و اهداف آموزشی:",
      "en": "Description & Learning Objectives:"
    },
    "dlg_field_tags": {
      "fa": "کلمات کلیدی (با کاما جدا کنید):",
      "en": "Keywords / Tags (comma separated):"
    },
    "dlg_btn_browse": {
      "fa": "انتخاب فایل...",
      "en": "Browse..."
    },
    "dlg_btn_save": {
      "fa": "ثبت شبیه‌ساز",
      "en": "Save Simulator"
    },
    "dlg_btn_cancel": {
      "fa": "انصراف",
      "en": "Cancel"
    },
    "dlg_err_missing_fields": {
      "fa": "لطفاً عنوان و مسیر فایل اجرایی را مشخص فرمایید.",
      "en": "Please provide both title and executable path."
    },
    "dlg_err_exe_not_found": {
      "fa": "فایل اجرایی انتخاب‌شده یافت نشد یا معتبر نیست.",
      "en": "Selected executable not found or invalid."
    },
    # Footer
    "footer_credits": {
      "fa": "طراحی و توسعه: امیرمحمد یوسف‌وند | دانشگاه فرهنگیان پردیس شهید باهنر اراک",
      "en": "Developed by Amirmohammad Yousefvand | Farhangian University, Shahid Bahonar Campus Arak"
    },
    "footer_rights": {
      "fa": "آزمایشگاه فیزیک | پاییز ۱۴۰۵",
      "en": "Physics Laboratory | Fall 2026"
    }
}

class Localization:
    _current_lang = "fa"

    @classmethod
    def set_language(cls, lang: str):
        if lang in ("fa", "en"):
            cls._current_lang = lang

    @classmethod
    def get_language(cls) -> str:
        return cls._current_lang

    @classmethod
    def tr(cls, key: str, **kwargs) -> str:
        entry = TRANSLATIONS.get(key, {})
        text = entry.get(cls._current_lang, entry.get("fa", key))
        if kwargs:
            text = text.format(**kwargs)
        return clean_persian_text(text)
