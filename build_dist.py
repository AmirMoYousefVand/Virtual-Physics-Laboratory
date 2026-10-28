# -*- coding: utf-8 -*-
"""
Automated Distribution Packaging Script for CFU Virtual Laboratory Suite.
Compiles launcher with PyInstaller and packages complete portable zip for festival submission.
"""

import os
import sys
import shutil
import subprocess
import zipfile

def run_command(cmd, description):
    print(f"\n[STEP] {description}...")
    res = subprocess.run(cmd, shell=True)
    if res.returncode != 0:
        print(f"[ERROR] Failed: {description}")
        sys.exit(res.returncode)

def main():
    if sys.platform.startswith("win"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    print("=======================================================")
    print("  CFU Virtual Laboratory - Distribution Packager       ")
    print("  Farhangian University - Shahid Bahonar Campus Arak   ")
    print("=======================================================")

    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)

    # 1. Clean previous build artifacts
    print("\n[STEP] Cleaning old build artifacts...")
    for folder in ["build", "dist"]:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
            except Exception as e:
                print(f"Warning cleaning {folder}: {e}")

    # 2. Run PyInstaller
    run_command(f'pyinstaller --noconfirm --clean cfu_lab.spec', "Compiling CFU_Virtual_Laboratory.exe")

    # 3. Assemble Portable Bundle
    bundle_name = "CFU_Virtual_Laboratory_v1.0.0"
    portable_dir = os.path.join(root_dir, "dist", bundle_name)
    os.makedirs(portable_dir, exist_ok=True)

    print(f"\n[STEP] Assembling distribution bundle in {portable_dir}...")

    # Copy compiled launcher EXE
    compiled_exe = os.path.join(root_dir, "dist", "CFU_Virtual_Laboratory.exe")
    if os.path.exists(compiled_exe):
        shutil.copy2(compiled_exe, os.path.join(portable_dir, "CFU_Virtual_Laboratory.exe"))
    else:
        print(f"[ERROR] Compiled executable not found at {compiled_exe}")
        sys.exit(1)

    # Copy assets to portable and dist
    shutil.copytree(os.path.join(root_dir, "assets"), os.path.join(portable_dir, "assets"), dirs_exist_ok=True)
    shutil.copytree(os.path.join(root_dir, "assets"), os.path.join(root_dir, "dist", "assets"), dirs_exist_ok=True)

    # Copy config to portable and dist
    shutil.copytree(os.path.join(root_dir, "config"), os.path.join(portable_dir, "config"), dirs_exist_ok=True)
    shutil.copytree(os.path.join(root_dir, "config"), os.path.join(root_dir, "dist", "config"), dirs_exist_ok=True)

    # Copy simulators to portable and dist
    os.makedirs(os.path.join(portable_dir, "simulators"), exist_ok=True)
    os.makedirs(os.path.join(root_dir, "dist", "simulators"), exist_ok=True)
    sim_dir = os.path.join(root_dir, "simulators")
    for f in os.listdir(sim_dir):
        if f.endswith(".exe"):
            src_f = os.path.join(sim_dir, f)
            shutil.copy2(src_f, os.path.join(portable_dir, "simulators", f))
            shutil.copy2(src_f, os.path.join(root_dir, "dist", "simulators", f))
            print(f"  Copying simulator: {f} ({os.path.getsize(src_f) / (1024*1024):.1f} MB)")

    # Write Persian README / Guide for Festival Jury
    readme_content = (
        "===============================================================\n"
        "سامانه جامع آزمایشگاه مجازی فیزیک - دانشگاه فرهنگیان\n"
        "CFU Virtual Physics Laboratory Suite v1.0.0\n"
        "===============================================================\n\n"
        "ویژه: جشنواره تولید محتوای الکترونیکی و آموزشی\n"
        "پژوهشگر و توسعه‌دهنده: امیرمحمد یوسف‌وند\n"
        "مرکز: دانشگاه فرهنگیان — پردیس شهید باهنر اراک\n"
        "تاریخ: پاییز ۱۴۰۵ - سال ۲۰۲۶\n\n"
        "راهنمای اجرا:\n"
        "1. این بسته کاملاً پرتابل (Portable) است و نیازی به نصب پایتون یا نرم‌افزارهای جانبی ندارد.\n"
        "2. برای ورود به سامانه، کافی است روی فایل «CFU_Virtual_Laboratory.exe» دو بار کلیک فرمایید.\n"
        "3. در صفحه نخست، شبیه‌سازهای زیر در دسترس می‌باشند:\n"
        "   • شبیه‌ساز اسپکترومتر اپتیکی و توری پراش (با ورنیه‌های دوطرفه و خطوط طیفی عناصر)\n"
        "   • شبیه‌ساز آزمایش دوشکاف یانگ (اپتیک موجی، نمودار شدت و تک‌فوتون کوانتومی)\n"
        "4. با فشردن دکمه «ورود به شبیه‌ساز»، شبیه‌ساز انتخاب‌شده باز می‌شود (لطفاً ۳ الی ۵ ثانیه جهت بارگذاری اولیه شبیه‌ساز شکیبا باشید).\n"
        "5. در صورتی که شبیه‌ساز قبلاً باز شده باشد، با کلیک مجدد، پنجره آن مستقیماً به جلوی تصویر آورده می‌شود.\n"
        "6. قابلیت افزودن شبیه‌سازهای جدید از طریق دکمه «+ افزودن شبیه‌ساز» یا ویرایش فایل config/simulators.json فراهم است.\n\n"
        "با آرزوی موفقیت و بهره‌برداری مؤثر در ارتقای آموزش فیزیک کشور.\n"
    )
    with open(os.path.join(portable_dir, "راهنمای اجرا.txt"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    with open(os.path.join(root_dir, "dist", "راهنمای اجرا.txt"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 4. Create ZIP Archive for Festival Submission
    zip_path = os.path.join(root_dir, "dist", f"{bundle_name}.zip")
    print(f"\n[STEP] Creating festival upload archive: {zip_path}...")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(portable_dir):
            for file in files:
                abs_file = os.path.join(root, file)
                rel_path = os.path.relpath(abs_file, os.path.join(root_dir, "dist"))
                zf.write(abs_file, rel_path)

    zip_size_mb = os.path.getsize(zip_path) / (1024 * 1024)
    exe_size_mb = os.path.getsize(os.path.join(portable_dir, "CFU_Virtual_Laboratory.exe")) / (1024 * 1024)

    print("\n=======================================================")
    print("  BUILD & PACKAGING COMPLETED SUCCESSFULLY!            ")
    print("=======================================================")
    print(f"Launcher Executable : {exe_size_mb:.1f} MB")
    print(f"Portable Folder     : {portable_dir}")
    print(f"Festival ZIP Package: {zip_path} ({zip_size_mb:.1f} MB)")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
