# -*- coding: utf-8 -*-
"""
Script to generate the official Persian PDF document for:
4-4 تولید نمونه‌ اولیه آزمایشگاهی (Laboratory Prototype & Functional Software Implementation Report)
for Virtual Physics Laboratory Suite (آزمایشگاه مجازی فیزیک).
Uses B Titr for headings and B Nazanin for body text with strict vertical pacing.
"""

import os
import subprocess
import base64

def get_base64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    logo_base64 = get_base64_image(os.path.join(root_dir, "assets", "branding", "icon.png"))

    html_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="fa">
<head>
<meta charset="utf-8">
<title>گزارش تولید نمونه اولیه آزمایشگاهی — آزمایشگاه مجازی فیزیک</title>
<style>
@font-face {{
    font-family: 'BTitr';
    src: url('file:///C:/Windows/Fonts/BTitrBd.ttf') format('truetype');
    font-weight: bold;
}}
@font-face {{
    font-family: 'BNazanin';
    src: url('file:///C:/Windows/Fonts/B%20Nazanin_YasDL.com.ttf') format('truetype');
    font-weight: normal;
}}
@font-face {{
    font-family: 'BNazanin';
    src: url('file:///C:/Windows/Fonts/B%20Nazanin%20Bold_YasDL.com.ttf') format('truetype');
    font-weight: bold;
}}

@page {{
    size: A4 portrait;
    margin: 10mm 15mm 12mm 15mm;
}}

*, *:before, *:after {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}

body {{
    font-family: 'BNazanin', 'B Nazanin', 'Vazirmatn', Tahoma, sans-serif;
    font-size: 11pt;
    line-height: 1.48;
    color: #1a1a1a;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
    direction: rtl;
    text-align: justify;
}}

h1, h2, h3, h4 {{
    font-family: 'BTitr', 'B Titr', Tahoma, sans-serif;
    color: #0c2340;
    margin-top: 0;
    margin-bottom: 3px;
    font-weight: bold;
}}

.page {{
    page-break-after: always;
    height: 272mm;
    max-height: 272mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
    padding-bottom: 0;
}}
.page:last-child {{
    page-break-after: avoid;
}}

.page-body {{
    flex: 1 1 auto;
}}

/* Header Banner */
.official-header {{
    border-bottom: 2px solid #0284c7;
    padding-bottom: 5px;
    margin-bottom: 7px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}
.header-titles {{
    flex: 1;
    text-align: center;
}}
.header-titles .ministry {{
    font-size: 13.5pt;
    font-family: 'BTitr', sans-serif;
    color: #0f172a;
    margin-bottom: 2px;
}}
.header-titles .doc-title {{
    font-size: 14pt;
    font-family: 'BTitr', sans-serif;
    color: #0284c7;
}}
.header-logo {{
    width: 60px;
    height: 60px;
    object-fit: contain;
}}
.header-meta {{
    font-size: 9pt;
    color: #475569;
    text-align: left;
    direction: ltr;
    line-height: 1.35;
}}

/* Section Titles */
.section-title {{
    font-size: 11.5pt;
    background-color: #f1f5f9;
    border-right: 4px solid #0284c7;
    padding: 3px 10px;
    margin-top: 6px;
    margin-bottom: 4px;
    border-radius: 2px;
}}

/* Identity Table */
.info-grid {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 6px;
    font-size: 10pt;
}}
.info-grid td {{
    border: 1px solid #cbd5e1;
    padding: 3px 8px;
}}
.info-grid .label {{
    background-color: #f8fafc;
    font-family: 'BTitr', sans-serif;
    color: #334155;
    width: 22%;
    font-size: 9.5pt;
}}
.info-grid .value {{
    color: #0f172a;
    width: 28%;
}}

/* Cards and Callouts */
.feature-card {{
    border: 1px solid #e2e8f0;
    background-color: #f8fafc;
    border-radius: 5px;
    padding: 6px 10px;
    margin-bottom: 5px;
}}
.feature-card h3 {{
    font-size: 10.5pt;
    color: #0369a1;
    margin-bottom: 2px;
}}

/* Technical Specs & Data Tables */
.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 3px;
    margin-bottom: 5px;
    font-size: 9.5pt;
}}
.data-table th {{
    background-color: #0f172a;
    color: #ffffff;
    font-family: 'BTitr', sans-serif;
    padding: 3px 6px;
    text-align: center;
    border: 1px solid #0f172a;
    font-size: 9pt;
}}
.data-table td {{
    border: 1px solid #cbd5e1;
    padding: 3px 6px;
    text-align: right;
}}
.data-table tr:nth-child(even) {{
    background-color: #f8fafc;
}}

ul {{
    margin: 2px 0 4px 0;
    padding-right: 18px;
}}
li {{
    margin-bottom: 2px;
}}

.footer-stamp {{
    border-top: 1px solid #cbd5e1;
    padding-top: 4px;
    padding-bottom: 2px;
    font-size: 9pt;
    color: #64748b;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-shrink: 0;
}}

.badge {{
    display: inline-block;
    padding: 1px 6px;
    font-size: 8.5pt;
    background-color: #e0f2fe;
    color: #0369a1;
    border-radius: 4px;
    font-weight: bold;
}}
.badge-success {{
    background-color: #dcfce7;
    color: #15803d;
}}
</style>
</head>
<body>

<!-- ======================================================================= -->
<!-- PAGE 1: شناسنامه نمونه اولیه و مراحل تکامل مهندسی                           -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                کد سند: DOC-PROTO-0404<br>
                تاریخ: پاییز ۱۴۰۵<br>
                سطح بلوغ: نمونه اولیه کارکردی کامل
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">مستند فنی (۴-۴ تولید نمونه اولیه آزمایشگاهی)</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <table class="info-grid">
            <tr>
                <td class="label">عنوان فناوری:</td>
                <td class="value"><strong>آزمایشگاه مجازی فیزیک (Virtual Physics Laboratory)</strong></td>
                <td class="label">توسعه‌دهنده:</td>
                <td class="value"><strong>امیرمحمد یوسف‌وند</strong><br><small style="color:#475569;">دانشجومعلم رشته آموزش علوم تجربی</small></td>
            </tr>
            <tr>
                <td class="label">وضعیت نمونه اولیه:</td>
                <td class="value"><span class="badge badge-success">نمونه‌های اولیه کامل و کامپایل‌شده (EXE)</span></td>
                <td class="label">پردیس دانشگاهی:</td>
                <td class="value">دانشگاه فرهنگیان پردیس شهید باهنر اراک</td>
            </tr>
            <tr>
                <td class="label">محیط استقرار نمونه:</td>
                <td class="value">آزمایشگاه فیزیک، کارگاه کامپیوتر و رایانه شخصی</td>
                <td class="label">شاخص ارزیابی:</td>
                <td class="value">شاخص ۴-۴ تولید نمونه‌های اولیه آزمایشگاهی</td>
            </tr>
        </table>

        <div class="section-title">۱. هدف سند و تشریح تحقق نمونه‌های اولیه آزمایشگاهی (Prototype Scope)</div>
        <p style="margin: 2px 0 4px 0;">
            این مستند در پاسخ به شاخص ۴-۴ فرم ارزیابی، شواهد عینی، ساختار فنی و نتایج حاصل از <strong>طراحی، ساخت و پیاده‌سازی نمونه‌های اولیه کارکردی آزمایشگاهی (Working Prototypes)</strong> سامانه «آزمایشگاه مجازی فیزیک» را ارائه می‌نماید. فناوری توسعه‌یافته نه صرفاً یک طرح مفهومی بر روی کاغذ، بلکه شامل <strong>سه نمونه اولیه مهندسی‌شده و کاملاً عملیاتی</strong> به صورت نرم‌افزارهای دسکتاپ مستقل با رابط کاربری تعاملی، موتورهای فیزیکی اختصاصی و خروجی‌های آزمایشگاهی استاندارد است.
        </p>

        <div class="section-title">۲. مراحل چهارگانه تکامل نمونه اولیه از اثبات ایده تا محصول کارکردی</div>
        <div class="feature-card">
            <h3>فرآیند گام‌به‌گام تحقیق و توسعه مهندسی نمونه‌های اولیه (R&amp;D Pipeline)</h3>
            <ul>
                <li><strong>گام اول — اثبات مفهوم فیزیکی (Proof of Concept - PoC):</strong> استخراج فرمول‌بندی‌های تحلیلی توزیع شدت فرانهوفر، رابطه پاشندگی کوشی منشور، معادله پراش توری، روابط دوبروی ماده و مدل‌سازی ماتریسی ورنیه در اسکریپت‌های اولیه پایتون.</li>
                <li><strong>گام دوم — نمونه اولیه موتور محاسباتی (Computational Core Prototype):</strong> وکتورایز کردن محاسبات ریاضی با استفاده از توابع عددی سطح C در NumPy، بهینه‌سازی الگوریتم نمونه‌برداری معکوس تابع چگالی احتمال برای شبیه‌سازی مونت‌کارلو در زمان حقیقی.</li>
                <li><strong>گام سوم — نمونه اولیه تعاملی آزمایشگاهی (Interactive GUI Prototype):</strong> طراحی و پیاده‌سازی بوم‌های گرافیکی پویا، کنترل‌های اسلایدر، پالت‌های رنگی برتون sRGB، ورنیه‌های دوطرفه چرخان و تولبارهای ناوبری سه‌بعدی با رابط ارگونومیک CustomTkinter.</li>
                <li><strong>گام چهارم — نمونه اولیه مجتمع پرتابل (Integrated Standalone Bundle):</strong> تجمیع کامل کتابخانه‌ها، فونت‌های بومی، آیکون‌های وکتور اختصاصی و باینری‌های اجرایی در یک بسته پرتابل بدون وابستگی (Zero-Dependency) با PyInstaller.</li>
            </ul>
        </div>

        <div class="section-title">۳. ماتریس معرفی نمونه‌های اولیه آماده آزمایشگاه</div>
        <table class="data-table">
            <tr>
                <th style="width: 25%;">عنوان نمونه اولیه</th>
                <th style="width: 25%;">نوع فایل و ابعاد</th>
                <th style="width: 25%;">ویژگی کلیدی عملیاتی</th>
                <th style="width: 25%;">وضعیت دسترسی</th>
            </tr>
            <tr>
                <td><strong>لانچر جامع آزمایشگاه مجازی</strong></td>
                <td>CFU_Virtual_Laboratory.exe (۴۰ مگابایت)</td>
                <td>ایزولاسیون فرآیندها، رجیستری داینامیک، ریسپانسیو 720p</td>
                <td><span class="badge badge-success">آماده اجرا و تست</span></td>
            </tr>
            <tr>
                <td><strong>نمونه شبیه‌ساز اسپکترومتر</strong></td>
                <td>SpectroMeter_Simulator.exe (۸۰ مگابایت)</td>
                <td>ورنیه دوطرفه، منشور کوشی، استخراج ریدبرگ، طیف NIST</td>
                <td><span class="badge badge-success">آماده اجرا و تست</span></td>
            </tr>
            <tr>
                <td><strong>نمونه شبیه‌ساز دو شکاف یانگ</strong></td>
                <td>Young_Double_Slit_Simulator.exe (۵۳ مگابایت)</td>
                <td>تداخل فرانهوفر، ناظر کوانتومی، مونت‌کارلو، تیغه نوری</td>
                <td><span class="badge badge-success">آماده اجرا و تست</span></td>
            </tr>
        </table>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۴ تولید نمونه اولیه آزمایشگاهی — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۱ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 2: تشریح کارکردی نمونه‌های اولیه اسپکترومتر و یانگ                     -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش دوم: ساختار نمونه‌های اولیه<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">کالبدشناسی و اجزای فنی نمونه‌های اولیه آزمایشگاهی</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۴. مشخصات کارکردی نمونه اولیه شبیه‌ساز اسپکترومتر اپتیکی</div>
        <p style="margin: 2px 0 3px 0; font-size: 10.5pt;">
            نمونه اولیه اسپکترومتر، ماکت دقیق نرم‌افزاری دستگاه گونیومتر زاویه‌سنج آزمایشگاهی دانشگاه است و اجزای زیر در آن به طور کامل پیاده‌سازی و تست شده‌اند:
        </p>
        <ul>
            <li><strong>مکانیزم ورنیه‌های مکانیکی دوبل (Dual Verniers):</strong> دایره ۳۶۰ درجه مدرج با دقت ۱ دقیقه قوسی، امکان چرخش زاویه با درگ ماوس، اسکرول ماوس و دکمه‌های گام‌به‌گام برای شبیه‌سازی دقیق قرائت با ذره‌بین.</li>
            <li><strong>چشم‌انداز چشمی تلسکوپ (Eyepiece View):</strong> تار عنکبوت متقاطع (Reticle Crosshair)، پیچ تنظیم فوکوس تلسکوپ و کولیماتور، و شبیه‌سازی پهنای خط با تابع گسترش نقطه (Defocus PSF).</li>
            <li><strong>نمای سه‌بعدی تعاملی دستگاه (3D Apparatus):</strong> مدل‌سازی کامل سه‌بعدی پایه، کولیماتور، میز تراز شوستر و تلسکوپ با قابلیت چرخش آزاد دوربین و بزرگ‌نمایی.</li>
            <li><strong>ماژول حل مسأله معکوس (Unknown Element Quiz):</strong> تولید طیف ناشناخته تصادفی جهت تمرین کلاسی دانشجویان در اندازه‌گیری زاویه، محاسبه طول‌موج و شناسایی عنصر مجهول.</li>
        </ul>

        <div class="section-title">۵. مشخصات کارکردی نمونه اولیه شبیه‌ساز دو شکاف یانگ</div>
        <p style="margin: 2px 0 3px 0; font-size: 10.5pt;">
            نمونه اولیه آزمایش دو شکاف، ترکیب همزمان اپتیک موجی کلاسیک و شبیه‌سازی آماری ذرات کوانتومی است:
        </p>
        <ul>
            <li><strong>پرده آشکارساز دوبعدی بلادرنگ:</strong> بازسازی طیف نوری پیوسته با رنگ‌بندی دقیق طول‌موج و امکان تغییر پالت رنگی به Turbo و Inferno جهت نمایان‌سازی نوارهای پراش کم‌نور.</li>
            <li><strong>نمودار شدت و مقایسه تحلیلی (1D Profile):</strong> رسم همزمان منحنی تجربی و تئوری شدت نور، پوش پراش منفرد و محاسبه کنتراست تداخل ($V$).</li>
            <li><strong>موتور پرتاب ذرات کوانتومی (Monte Carlo Engine):</strong> شبیه‌سازی برخورد دانه‌دانه فوتون‌ها، الکترون‌ها و باکی‌بال‌ها با پرده فسفری و امکان فعال‌سازی ناظر کوانتومی Which-Way.</li>
            <li><strong>شبیه‌سازی چشمه همدوس ($S_0$) و تیغه فاز نوری:</strong> ایجاد چشمه تک‌شکاف پیش‌نیاز و اعمال تیغه شفاف در برابر پرتوها با محاسبه لحظه‌ای جابه‌جایی فریزهای تداخل.</li>
        </ul>

        <div class="section-title">۶. مشخصات مهندسی کد و معماری بسته‌های نرم‌افزاری نمونه اولیه</div>
        <table class="data-table">
            <tr>
                <th style="width: 25%;">شاخص توسعه</th>
                <th style="width: 38%;">پیاده‌سازی در نمونه اولیه آزمایشگاهی</th>
                <th style="width: 37%;">نقش در پایداری فناوری</th>
            </tr>
            <tr>
                <td>حجم کدنویسی خالص</td>
                <td>بیش از ۱۲,۰۰۰ خط کد پایتون مستندسازی‌شده</td>
                <td>توسعه ساخت‌یافته و شیءگرا (OOP)</td>
            </tr>
            <tr>
                <td>موتور گرافیکی و فریمورک</td>
                <td>CustomTkinter مدرن بر پایه Canvas و Matplotlib</td>
                <td>نرخ فریم بالا (۶۰ FPS) و عدم وابستگی به درایور سنگین</td>
            </tr>
            <tr>
                <td>مدیریت خروجی آزمایشگاهی</td>
                <td>ماژول داخلی تولید اسناد DOCX و دیتاست CSV</td>
                <td>استخراج گزارش بدون نیاز به نرم‌افزار واسط</td>
            </tr>
            <tr>
                <td>قابلیت حمل (Portability)</td>
                <td>تولید بسته مستقل پرتابل با PyInstaller</td>
                <td>عدم نیاز به نصب و راه‌اندازی در رایانه‌های مقصد</td>
            </tr>
        </table>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۴ تولید نمونه اولیه آزمایشگاهی — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۲ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 3: شواهد استقرار، آزمون میدانی و تأییدیه اصالت                        -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش سوم: شواهد عملکرد و تأییدیه<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">شواهد استقرار عملیاتی نمونه اولیه و بیانیه پدیدآورنده</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۷. شواهد پیاده‌سازی عینی و در دسترس بودن نمونه‌های اولیه</div>
        <p style="margin: 2px 0 4px 0;">
            نمونه‌های اولیه آزمایشگاهی تولیدشده هم‌اکنون به صورت کامل، عملیاتی و قابل ارزیابی توسط داوران محترم در دسترس می‌باشند:
        </p>

        <table class="data-table">
            <tr>
                <th style="width: 28%;">نوع مدرک / دارایی</th>
                <th style="width: 42%;">محل دسترسی و نام فایل</th>
                <th style="width: 30%;">محتوا و کارکرد</th>
            </tr>
            <tr>
                <td>بسته پرتابل جامع جشنواره</td>
                <td>CFU_Virtual_Laboratory_v1.0.0.zip (۱۷۷ مگابایت)</td>
                <td>لانچر + هر دو شبیه‌ساز کامپایل‌شده آماده اجرای آفلاین</td>
            </tr>
            <tr>
                <td>مخزن سورس کد لانچر</td>
                <td>github.com/AmirMoYousefVand/Virtual-Physics-Laboratory</td>
                <td>کد منبع آزاد لانچر و فایل‌های پیکربندی</td>
            </tr>
            <tr>
                <td>مخزن شبیه‌ساز اسپکترومتر</td>
                <td>github.com/AmirMoYousefVand/SpectroMeter-Simulator</td>
                <td>کد منبع نسخه v1.1.0 همراه با تست‌های ۱۲ گانه</td>
            </tr>
            <tr>
                <td>مخزن شبیه‌ساز دو شکاف یانگ</td>
                <td>github.com/AmirMoYousefVand/Double-slit-experiment-Simulator</td>
                <td>کد منبع نسخه v1.3.0 همراه با ۳۸ تست اعتبارسنجی</td>
            </tr>
        </table>

        <div class="section-title">۸. دستاوردهای کارکردی نمونه‌های اولیه در محیط واقعی آموزشی</div>
        <ul>
            <li><strong>تولید گزارش کار هوشمند:</strong> دانشجو پس از آزمایش در نمونه اولیه، با یک کلیک گزارش رسمی مایکروسافت ورد با فرمول‌های ریاضی استاندارد OMML دریافت می‌کند.</li>
            <li><strong>شبیه‌سازی شرایط آزمایشگاهی غیرایده‌آل:</strong> امکان تجربه انحراف محور دستگاه، تاری فوکوس و مرتبه‌های ناموجود بدون صدمه به تجهیزات گران‌قیمت فیزیکی.</li>
            <li><strong>آزمون کلاسی تعاملی:</strong> مدرس می‌تواند از نمونه اولیه برای سنجش و اخذ آزمون زنده کلاسی از دانشجویان استفاده نماید.</li>
        </ul>

        <div class="section-title">۹. بیانیه اصالت، تعهد اخلاقی و تأیید ساخت نمونه‌های اولیه</div>
        <p style="font-size: 10.5pt; margin-top: 3px;">
            بدین‌وسیله گواهی و تأیید می‌گردد کلیه نمونه‌های اولیه آزمایشگاهی، ماژول‌های محاسباتی، رابط‌های کاربری، فرآیندهای کامپایل مستقل و مستندات ارائه شده در این مجموعه توسط <strong>امیرمحمد یوسف‌وند</strong> (دانشجومعلم رشته آموزش علوم تجربی در <strong>دانشگاه فرهنگیان پردیس شهید باهنر اراک</strong>) با هدف ارتقای آموزش فیزیک در سطح کشور طراحی، کدنویسی، کامپایل و راستی‌آزمایی شده و نمونه‌ها به صورت کاملاً کارکردی آماده بهره‌برداری و داوری می‌باشند.
        </p>

        <div style="margin-top: 15px; text-align: center;">
            <div style="display: inline-block; border-top: 1px solid #94a3b8; padding-top: 6px; width: 300px;">
                <div style="font-family: 'BTitr', sans-serif; color: #0f172a; font-size: 11pt; margin-bottom: 2px;">طراح و توسعه‌دهنده نمونه‌های اولیه</div>
                <div style="font-size: 12pt; font-weight: bold; color: #0284c7;">امیرمحمد یوسف‌وند</div>
                <div style="font-size: 9.5pt; color: #475569; margin-top: 2px;">دانشجومعلم رشته آموزش علوم تجربی</div>
                <div style="font-size: 9pt; color: #64748b;">دانشگاه فرهنگیان — پردیس شهید باهنر اراک (پاییز ۱۴۰۵)</div>
            </div>
        </div>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۴ تولید نمونه اولیه آزمایشگاهی — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۳ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

</body>
</html>
"""

    html_path = os.path.join(root_dir, "doc_proto_4_4.html")
    pdf_path = os.path.join(root_dir, "4-4  تولید نمونه‌ اولیه آزمایشگاهی.pdf")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]

    print("[INFO] Rendering Prototype Report PDF using Microsoft Edge...")
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if res.returncode == 0 and os.path.exists(pdf_path):
        print(f"[SUCCESS] PDF generated successfully. Size: {os.path.getsize(pdf_path) / 1024:.1f} KB")
    else:
        print("[ERROR] PDF generation failed, returncode:", res.returncode)

    if os.path.exists(html_path):
        os.remove(html_path)

if __name__ == "__main__":
    import sys
    if sys.platform.startswith("win"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
