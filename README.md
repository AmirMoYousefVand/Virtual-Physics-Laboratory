# Virtual Physics Laboratory Suite (آزمایشگاه مجازی فیزیک)

[![GitHub Repository](https://img.shields.io/badge/GitHub-AmirMoYousefVand%2FVirtual--Physics--Laboratory-181717?logo=github&logoColor=white)](https://github.com/AmirMoYousefVand/Virtual-Physics-Laboratory)
[![Latest Release](https://img.shields.io/github/v/release/AmirMoYousefVand/Virtual-Physics-Laboratory?label=release&logo=github)](https://github.com/AmirMoYousefVand/Virtual-Physics-Laboratory/releases)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Platform Windows](https://img.shields.io/badge/platform-Windows%2064--bit-0078D6.svg)](https://github.com/AmirMoYousefVand/Virtual-Physics-Laboratory)
[![GUI CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-10B981.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![License MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An integrated, extensible desktop laboratory suite for launching, exploring, and managing research-grade physics simulators. Engineered for university physics departments, wave optics laboratories, and modern physics education.

---

## Bundled Interactive Simulators

1. **Optical Spectrometer & Diffraction Grating Simulator**
   - High-precision circular goniometer ($360^\circ$ scale with $30'$ intervals)
   - Dual magnified vernier loupes with $1'$ ($1/60^\circ$) Least Count
   - Real atomic discharge spectra: Mercury (Hg), Sodium Doublet (Na D1/D2), Hydrogen Balmer Series, Helium (He), Neon (Ne)
   - Equilateral glass prism Cauchy dispersion and minimum deviation angle ($D_{\min}$) measurements
   - Automated Word report export with native Microsoft Office OMML equations

2. **Thomas Young Double-Slit Experiment Simulator**
   - Exact Fraunhofer wave-optics intensity modeling: $I(\theta) = I_0 \cos^2(\beta) \text{sinc}^2(\alpha)$
   - Quantum wave-particle duality with single-photon/electron/buckyball detection build-up
   - Which-way observer effect simulating wavefunction collapse and quantum decoherence
   - Optical slab path insertion and spatial coherence pre-barrier ($S_0$) modeling
   - 22-column scientific CSV dataset, 3D CAD OBJ model, and high-DPI figures

---

## Suite Highlights

- **Seamless Standalone Execution**: Fully portable package without requiring Python or external runtimes on target machines.
- **Dynamic Extensibility**: Register custom simulators (executable or script) via GUI modal or `config/simulators.json` without recompilation.
- **Process Lifecycle & Focus Management**: Independent working directory (`cwd`) isolation, preventing duplicate process instances and bringing running simulators to the foreground.
- **Modern Titanium UI**: Acrylic-styled dark theme built with CustomTkinter, crisp typography using Vazirmatn and Space Grotesk, live search, and category filtering.
- **Vector Iconography**: 100% clean vector icons without unstable emoji glyphs.

---

## Installation & Running

### Option A: Portable Windows Bundle (Recommended)
1. Download `CFU_Virtual_Laboratory_v1.0.0.zip` from [Releases](https://github.com/AmirMoYousefVand/Virtual-Physics-Laboratory/releases).
2. Extract the archive.
3. Run `CFU_Virtual_Laboratory.exe`.

### Option B: Running from Source
```bash
git clone https://github.com/AmirMoYousefVand/Virtual-Physics-Laboratory.git
cd Virtual-Physics-Laboratory
pip install -r requirements.txt
python main.py
```

### Running Verification Tests
```bash
python test_app.py
```

---

## Project Structure

```
├── main.py                  # Entry point and Windows AppID registration
├── build_dist.py            # Automated packaging and distribution script
├── cfu_lab.spec             # PyInstaller compilation specification
├── test_app.py              # Automated verification test suite
├── config/
│   ├── settings.py          # Theme parameters, dimensions, and metadata
│   └── simulators.json      # Dynamic simulator registry
├── core/
│   ├── config_manager.py    # JSON registry I/O, validation, and search filter
│   ├── localization.py      # Bilingual typography and text cleaning
│   └── process_manager.py   # Process execution, PID tracking, and window focus
├── ui/
│   ├── main_window.py       # Main window controller and status loop
│   ├── components/          # Header, filter bar, simulator card grid, footer
│   └── dialogs/             # Add simulator and about software dialogs
├── utils/                   # GDI font loader, resource paths, Win32 window focus
├── assets/                  # Branding (favicon, icon), fonts (Vazirmatn, Space Grotesk), icons
└── simulators/              # Bundled simulator binaries
```

---

## Author & Academic Affiliation

- **Developer**: Amirmohammad Yousefvand
- **Institution**: Farhangian University — Shahid Bahonar Campus, Arak
- **Timeline**: Fall 2026 (پاییز ۱۴۰۵)
- **GitHub Profile**: [AmirMoYousefVand](https://github.com/AmirMoYousefVand)

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
