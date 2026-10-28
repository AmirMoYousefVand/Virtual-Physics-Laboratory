"""
Configuration and Simulator Registry Manager.
Handles loading, saving, path resolution, and filtering of simulator definitions.
"""

import os
import json
from typing import List, Dict, Any, Optional
from utils.resource_utils import resource_path, get_base_dir

DEFAULT_CONFIG: Dict[str, Any] = {
    "version": "1.0.0",
    "categories": [
        {"id": "all", "name_fa": "همه شبیه‌سازها", "name_en": "All Simulators"},
        {"id": "optics", "name_fa": "اپتیک و فوتونیک", "name_en": "Optics & Photonics"},
        {"id": "mechanics", "name_fa": "مکانیک کلاسیک", "name_en": "Mechanics"},
        {"id": "electromagnetism", "name_fa": "الکتریسیته و مغناطیس", "name_en": "Electromagnetism"},
        {"id": "modern_physics", "name_fa": "فیزیک نوین و کوانتوم", "name_en": "Modern Physics"}
    ],
    "simulators": []
}

class ConfigManager:
    def __init__(self, config_rel_path: str = os.path.join("config", "simulators.json")):
        self.config_rel_path = config_rel_path
        self.config_path = resource_path(config_rel_path)
        self.data: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self):
        """Loads configuration from JSON file with fallback."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
                return
            except Exception as e:
                print(f"Error loading {self.config_path}: {e}")

        # Try base directory if resource_path was different
        alt_path = os.path.join(get_base_dir(), self.config_rel_path)
        if os.path.exists(alt_path):
            try:
                with open(alt_path, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
                self.config_path = alt_path
                return
            except Exception as e:
                print(f"Error loading alt config: {e}")

    def save(self) -> bool:
        """Persists current registry back to JSON."""
        save_path = os.path.join(get_base_dir(), self.config_rel_path)
        try:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            self.config_path = save_path
            return True
        except Exception as e:
            print(f"Error saving {save_path}: {e}")
            return False

    def get_categories(self) -> List[Dict[str, str]]:
        return self.data.get("categories", DEFAULT_CONFIG["categories"])

    def get_simulators(self) -> List[Dict[str, Any]]:
        return self.data.get("simulators", [])

    def add_simulator(self, sim_data: Dict[str, Any]) -> bool:
        """Adds or updates a simulator entry and persists to disk."""
        sims = self.get_simulators()
        # Check if ID exists, update or append
        existing = next((s for s in sims if s.get("id") == sim_data.get("id")), None)
        if existing:
            existing.update(sim_data)
        else:
            sims.append(sim_data)
        self.data["simulators"] = sims
        return self.save()

    def remove_simulator(self, sim_id: str) -> bool:
        """Removes a simulator by ID."""
        sims = self.get_simulators()
        self.data["simulators"] = [s for s in sims if s.get("id") != sim_id]
        return self.save()

    def resolve_executable_path(self, sim: Dict[str, Any]) -> Optional[str]:
        """Resolves valid absolute path for a simulator executable."""
        raw_path = sim.get("executable", "")
        base_dir = get_base_dir()

        # 1. Check relative to base directory
        candidate_rel = os.path.normpath(os.path.join(base_dir, raw_path))
        if os.path.isfile(candidate_rel):
            return candidate_rel

        # 2. Check if raw_path is already absolute
        if os.path.isabs(raw_path) and os.path.isfile(raw_path):
            return os.path.normpath(raw_path)

        # 3. Check fallback path
        fallback = sim.get("fallback_path")
        if fallback and os.path.isfile(fallback):
            return os.path.normpath(fallback)

        # 4. Check relative to current working directory
        cwd_candidate = os.path.normpath(os.path.join(os.getcwd(), raw_path))
        if os.path.isfile(cwd_candidate):
            return cwd_candidate

        return None

    def resolve_icon_path(self, sim: Dict[str, Any]) -> str:
        """Resolves valid icon image path, falls back to default icon."""
        raw_icon = sim.get("icon", "")
        base_dir = get_base_dir()

        if raw_icon:
            candidate_rel = os.path.normpath(os.path.join(base_dir, raw_icon))
            if os.path.isfile(candidate_rel):
                return candidate_rel
            if os.path.isabs(raw_icon) and os.path.isfile(raw_icon):
                return os.path.normpath(raw_icon)

        default_icon = resource_path(os.path.join("assets", "icons", "default_sim.png"))
        if os.path.isfile(default_icon):
            return default_icon

        return resource_path(os.path.join("assets", "branding", "icon.png"))

    def filter_simulators(self, category: str = "all", query: str = "") -> List[Dict[str, Any]]:
        """Filters simulators by category and query string (Persian/English)."""
        sims = self.get_simulators()
        res = []
        q = query.strip().lower()

        for s in sims:
            # Category match
            if category != "all" and s.get("category") != category:
                continue

            # Query match
            if q:
                t_fa = s.get("title_fa", "").lower()
                t_en = s.get("title_en", "").lower()
                d_fa = s.get("description_fa", "").lower()
                d_en = s.get("description_en", "").lower()
                tags = " ".join(s.get("tags", [])).lower()

                if not (q in t_fa or q in t_en or q in d_fa or q in d_en or q in tags):
                    continue

            res.append(s)

        return res
