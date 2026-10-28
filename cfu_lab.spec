# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

ctk_datas = collect_data_files('customtkinter')

project_datas = [
    ('assets', 'assets'),
    ('config', 'config'),
] + ctk_datas

hidden_imports = [
    'PIL._tkinter_finder',
    'arabic_reshaper',
    'bidi.algorithm',
    'customtkinter',
    'psutil',
] + collect_submodules('customtkinter')

excludes = [
    'torch', 'torchvision', 'cv2', 'scipy', 'matplotlib',
    'paddle', 'IPython', 'notebook', 'pytest'
]

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=project_datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CFU_Virtual_Laboratory',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.abspath('assets/branding/favicon.ico'),
)
