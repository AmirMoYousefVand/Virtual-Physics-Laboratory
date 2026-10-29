# -*- coding: utf-8 -*-
"""
Script to generate the official Persian PDF document for:
(4-2 آماده بهره برداری از فناوری) - Technology Readiness & Operational Deployment Documentation
for Virtual Physics Laboratory Suite (آزمایشگاه مجازی فیزیک).
Uses B Titr for headings and B Nazanin for body text with perfect page breaking.
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
<title>مستند (۴-۲ آماده بهره‌برداری از فناوری) — آزمایشگاه مجازی فیزیک</title>
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
    line-height: 1.5;
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
    margin-bottom: 4px;
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
    padding-bottom: 6px;
    margin-bottom: 8px;
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
    font-size: 12pt;
    background-color: #f1f5f9;
    border-right: 4px solid #0284c7;
    padding: 3px 10px;
    margin-top: 7px;
    margin-bottom: 5px;
    border-radius: 2px;
}}

/* Identity Table */
.info-grid {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 8px;
    font-size: 10pt;
}}
.info-grid td {{
    border: 1px solid #cbd5e1;
    padding: 4px 8px;
}}
.info-grid .label {{
    background-color: #f8fafc;
    font-family: 'BTitr', sans-serif;
    color: #334155;
    width: 20%;
    font-size: 9.5pt;
}}
.info-grid .value {{
    color: #0f172a;
    width: 30%;
}}

/* Cards and Callouts */
.feature-card {{
    border: 1px solid #e2e8f0;
    background-color: #f8fafc;
    border-radius: 5px;
    padding: 6px 10px;
    margin-bottom: 6px;
}}
.feature-card h3 {{
    font-size: 11pt;
    color: #0369a1;
    margin-bottom: 2px;
}}

/* Technical Specs Table */
.spec-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 4px;
    margin-bottom: 6px;
    font-size: 9.5pt;
}}
.spec-table th {{
    background-color: #0f172a;
    color: #ffffff;
    font-family: 'BTitr', sans-serif;
    padding: 4px 8px;
    text-align: center;
    border: 1px solid #0f172a;
}}
.spec-table td {{
    border: 1px solid #cbd5e1;
    padding: 3px 8px;
    text-align: right;
}}
.spec-table tr:nth-child(even) {{
    background-color: #f8fafc;
}}

ul {{
    margin: 2px 0 5px 0;
    padding-right: 20px;
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
.badge-warning {{
    background-color: #fef3c7;
    color: #b45309;
}}
</style>
</head>
<body>

<!-- ======================================================================= -->
<!-- PAGE 1: شناسنامه فناوری و سطح آمادگی (TRL)                                -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                کد سند: DOC-TRL-0402<br>
                تاریخ: پاییز ۱۴۰۵<br>
                وضعیت: تأیید نهایی بهره‌برداری
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">مستند فنی (۴-۲ آماده بهره‌برداری از فناوری)</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <table class="info-grid">
            <tr>
                <td class="label">نام محصول فناوری:</td>
                <td class="value"><strong>سامانه آزمایشگاه مجازی فیزیک (Virtual Physics Lab)</strong></td>
                <td class="label">توسعه‌دهنده:</td>
                <td class="value"><strong>امیرمحمد یوسف‌وند</strong><br><small style="color: #475569;">دانشجومعلم رشته آموزش علوم تجربی</small></td>
            </tr>
            <tr>
                <td class="label">محل استقرار علمی:</td>
                <td class="value">دانشگاه فرهنگیان پردیس شهید باهنر اراک</td>
                <td class="label">سطح آمادگی فناوری (TRL):</td>
                <td class="value"><span class="badge badge-success">TRL 8 (محصول کامل و اثبات‌شده در محیط عملیاتی)</span></td>
            </tr>
            <tr>
                <td class="label">نوع ساختار اجرایی:</td>
                <td class="value">پرتابل بدون وابستگی (Zero-Dependency Standalone)</td>
                <td class="label">مرجع اصالت و سورس:</td>
                <td class="value" style="direction: ltr; text-align: left; font-family: sans-serif; font-size: 8pt;">github.com/AmirMoYousefVand/Virtual-Physics-Laboratory</td>
            </tr>
        </table>

        <div class="section-title">۱. هدف سند و ارزیابی سطح آمادگی فناوری (TRL Assessment)</div>
        <p style="margin: 3px 0 6px 0;">
            هدف از تدوین این مستند، ارائه شواهد مستدل و سنجش‌پذیر بر احراز شرایط <strong>«آماده بهره‌برداری بودن کامل محصول»</strong> طبق شاخص ۴-۲ فرم ارزیابی فناوری است. سامانه آزمایشگاه مجازی فیزیک با تجمیع شبیه‌سازهای تخصصی اسپکترومتر اپتیکی و آزمایش دو شکاف یانگ به همراه لانچر مدیریت فرآیندها، آزمون‌های پایه‌ای آزمایشگاهی (TRL 4-5) و شبیه‌سازی در محیط شبیه‌سازی‌شده (TRL 6) را سپری نموده و با موفقیت به سطح <strong>TRL 8 (سیستم کامل و واجد شرایط در محیط عملیاتی کلاس درس و آزمایشگاه‌های آموزشی)</strong> نائل آمده است.
        </p>

        <div class="section-title">۲. ویژگی‌های بنیادین احراز آمادگی بهره‌برداری فوری (Plug & Play)</div>
        <div class="feature-card">
            <h3>عدم نیاز به پیش‌نیاز نرم‌افزاری و استقرار مستقل (Zero-Install Portability)</h3>
            <ul>
                <li><strong>بی‌نیازی از پایتون و مفسرها:</strong> کل سامانه و شبیه‌سازهای تابعه توسط موتور کامپایلر به کدهای باینری مستقل ۳۲ بیتی/۶۴ بیتی ویندوز تبدیل شده‌اند. کاربر بدون نیاز به نصب Python، Git یا کتابخانه‌های جانبی با یک کلیک وارد محیط کاربری می‌شود.</li>
                <li><strong>استقلال از اینترنت (۱۰۰٪ آفلاین):</strong> کلیه موتورهای حل معادلات ریاضی، مدل‌سازی مونت‌کارلو، داده‌های طیف نشری عناصر، پالت‌های رنگی فیزیکی و فونت‌ها به صورت محلی در بسته گنجانده شده‌اند و نرم‌افزار بدون اینترنت با کارایی کامل کار می‌کند.</li>
                <li><strong>پایداری فرآیند و ایزولاسیون پردازه‌ها (Crash Resilience):</strong> هر شبیه‌ساز در پوشه کاری و فرآیند سیستمی مستقل اجرا می‌گردد؛ بروز هرگونه وقفه در یک ماژول موجب توقف لانچر یا سایر شبیه‌سازها نخواهد شد.</li>
            </ul>
        </div>

        <div class="section-title">۳. ماتریس سازگاری در سیستم‌های عامل و محیط‌های اجرایی مختلف</div>
        <table class="spec-table">
            <tr>
                <th style="width: 25%;">محیط سیستم‌عامل</th>
                <th style="width: 25%;">معماری و نسخه</th>
                <th style="width: 25%;">وضعیت آزمون پایداری</th>
                <th style="width: 25%;">شاخص عملکرد</th>
            </tr>
            <tr>
                <td>مایکروسافت ویندوز ۱۰</td>
                <td>64-bit (Build 19041+)</td>
                <td><span class="badge badge-success">کاملاً پایدار و تأییدشده</span></td>
                <td>زمان بارگذاری کمتر از ۳ ثانیه</td>
            </tr>
            <tr>
                <td>مایکروسافت ویندوز ۱۱</td>
                <td>64-bit (تمام نسخه‌ها)</td>
                <td><span class="badge badge-success">کاملاً پایدار و تأییدشده</span></td>
                <td>پشتیبانی از تم آکریلیک و شتاب‌نگاشت</td>
            </tr>
            <tr>
                <td>ویندوز سرور و سیستم‌های تحت شبکه</td>
                <td>Server 2016 / 2019 / 2022</td>
                <td><span class="badge badge-success">قابل بهره‌برداری</span></td>
                <td>اجرا در بستر Remote Desktop و شبکه کلاسی</td>
            </tr>
            <tr>
                <td>رایانه‌های سازمانی مدارس و دانشگاه</td>
                <td>سیستم‌های استاندارد آموزشگاهی</td>
                <td><span class="badge badge-success">تأییدشده در محیط کلاسی</span></td>
                <td>بدون نیاز به دسترسی Administrator</td>
            </tr>
        </table>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۲ آماده بهره‌برداری از فناوری — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۱ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 2: بهره‌برداری تحت رزولوشن‌ها و سخت‌افزارهای گوناگون                -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش دوم: آزمون وضعیت‌های عملیاتی<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">ماتریس رفتار نرم‌افزار تحت شرایط و محدودیت‌های عملیاتی مختلف</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۴. سازگاری با مانیتورهای قدیمی، پروژکتورهای کلاسی و رزولوشن‌های پایین</div>
        <p style="margin: 2px 0 4px 0; font-size: 10.5pt;">
            بسیاری از کلاس‌های درس، کارگاه‌های رایانه مدارس و آزمایشگاه‌های دانشگاهی به ویدئوپروژکتورها و نمایشگرهای قدیمی با رزولوشن محدود مجهز هستند. کلیه صفحات و نماهای سامانه برای نمایش بی‌نقص در این وضعیت‌ها بهینه‌سازی قطعی شده‌اند:
        </p>

        <table class="spec-table">
            <tr>
                <th style="width: 22%;">وضوح نمایشگر</th>
                <th style="width: 28%;">نوع تجهیز متداول</th>
                <th style="width: 25%;">رفتار انطباقی نرم‌افزار</th>
                <th style="width: 25%;">وضعیت دسترس‌پذیری</th>
            </tr>
            <tr>
                <td><strong>1280 × 720 (720p HD)</strong></td>
                <td>پروژکتورهای کلاسی و مانیتور ۱۸٫۵ اینچ</td>
                <td>کاهش ارتفاع به ۶۵۰ پیکسل، کلمپ با تسک‌بار</td>
                <td><span class="badge badge-success">۱۰۰٪ دسترسی به تمام کلیدها و فوتر</span></td>
            </tr>
            <tr>
                <td><strong>1366 × 768 (WXGA)</strong></td>
                <td>لپ‌تاپ‌های اداری و دانش‌آموزی</td>
                <td>چیدمان بهینه، فونت ۱۰ بولد تب‌های ۷ گانه</td>
                <td><span class="badge badge-success">بدون سرریز افقی یا هم‌پوشانی</span></td>
            </tr>
            <tr>
                <td><strong>1024 × 768 (XGA 4:3)</strong></td>
                <td>پروژکتورهای مربعی قدیمی و مانیتور CRT</td>
                <td>تغییر گرید لانچر به تک‌ستونی خودکار</td>
                <td><span class="badge badge-success">کارت‌ها با اسکرول عمودی بدون برش</span></td>
            </tr>
            <tr>
                <td><strong>1920 × 1080 (FHD) و بالاتر</strong></td>
                <td>نمایشگرهای استاندارد دسکتاپ و 4K</td>
                <td>فعال‌سازی DPI Awareness نیتیو ویندوز</td>
                <td><span class="badge badge-success">وضوح کریستالی متون و مقیاس دقیق</span></td>
            </tr>
        </table>

        <div class="section-title">۵. پاسخ‌دهی سیستم تحت وضعیت‌های سخت‌افزاری ضعیف و آزمون بار (Stress Test)</div>
        <div class="feature-card">
            <h3>بهینه‌سازی مصرف حافظه RAM و پردازشگر گرافیکی (Low-Spec Hardware Performance)</h3>
            <ul>
                <li><strong>سخت‌افزار پایه مورد نیاز:</strong> حداقل پردازنده ۲ هسته‌ای اینتل/AMD (Core 2 Duo به بعد)، ۲ گیگابایت حافظه رم، و گرافیک یکپارچه آنبورد معمولی (بدون نیاز به کارت گرافیک مجزای انویدیا/AMD).</li>
                <li><strong>الگوریتم‌های برداری سریع (Vectorized Computation):</strong> پیاده‌سازی محاسبات تداخل فرانهوفر و شبیه‌سازی مونت‌کارلو با استفاده از کتابخانه‌های عددی کامپایل‌شده C-Level (NumPy)، که موجب شده حتی ۵۰۰۰ شلیک ذره کوانتومی در کمتر از ۱۱ میلی‌ثانیه پردازش گردد.</li>
                <li><strong>مصرف ناچیز منابع در حالت بی‌کاری (Idle):</strong> نرخ به‌روزرسانی هوشمند، مصرف پردازنده در حالت بی‌کاری را به کمتر از ۰٫۵ درصد و مصرف حافظه رم لانچر را در حدود ۴۵ مگابایت تثبیت نموده است.</li>
            </ul>
        </div>

        <div class="section-title">۶. سازگاری با تنظیمات بزرگ‌نمایی تصویر ویندوز (Windows Display Scaling)</div>
        <p style="margin: 2px 0 4px 0; font-size: 10.5pt;">
            در لپ‌تاپ‌های جدید، ویندوز به صورت پیش‌فرض مقیاس تصویر را روی ۱۲۵٪ یا ۱۵۰٪ تنظیم می‌کند که در نرم‌افزارهای عادی موجب تاری یا بیرون افتادن پنجره می‌شود. در این سامانه با فراخوانی سطح سیستمی <code>SetProcessDpiAwareness</code>، رابط کاربری با هر نرخ اسکیلینگ به صورت نیتیو و با حداکثر وضوح هندسی بدون اعوجاج تطبیق می‌یابد.
        </p>

        <div class="section-title">۷. ایمنی در برابر خطای کاربری و مدیریت قطعی فرآیندها (Fault Tolerance)</div>
        <ul>
            <li><strong>مدیریت پنجره‌ها (Bring-to-Front):</strong> در صورتی که کاربر به اشتباه چند بار روی دکمه ورود کلیک کند، نمونه تکراری ساخته نمی‌شود؛ بلکه همان پنجره فعال از پس‌زمینه به جلوی تصویر آورده می‌شود.</li>
            <li><strong>پایداری در برابر آدرس‌های نامعتبر:</strong> اعتبارسنجی درونی فایل‌های اجرایی مانع از کرش نرم‌افزار در صورت مفقود بودن فایل شده و پیام راهنمای فارسی صادر می‌کند.</li>
        </ul>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۲ آماده بهره‌برداری از فناوری — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۲ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 3: نتایج آزمون‌ها، سناریوهای استقرار و بیانیه آمادگی                   -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش سوم: نتایج صحه‌گذاری و استقرار<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">شواهد صحه‌گذاری، سناریوهای کاربری و تأییدیه بهره‌برداری عملیاتی</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۸. کارنامه آزمون‌های خودکار و صحه‌گذاری محاسبات (Automated Verification)</div>
        <p style="margin: 2px 0 4px 0;">
            آمادگی بهره‌برداری این فناوری با تکیه بر <strong>۵۰ آزمون خودکار یکپارچه (Unit & Integration Tests)</strong> در حوزه محاسبات فیزیک، پایداری رابط کاربر و صحه‌گذاری خروجی‌ها به اثبات رسیده است:
        </p>

        <table class="spec-table">
            <tr>
                <th style="width: 30%;">بخش ارزیابی‌شده</th>
                <th style="width: 20%;">تعداد آزمون‌ها</th>
                <th style="width: 30%;">شاخص اعتبارسنجی فیزیکی</th>
                <th style="width: 20%;">نتیجه آزمون</th>
            </tr>
            <tr>
                <td>شبیه‌ساز اسپکترومتر اپتیکی</td>
                <td>۱۲ آزمون تخصصی</td>
                <td>انطباق ورنیه‌ها، پراش توری، پاشندگی کوشی و ریدبرگ</td>
                <td><span class="badge badge-success">۱۰۰٪ موفقیت (Pass)</span></td>
            </tr>
            <tr>
                <td>شبیه‌ساز دو شکاف یانگ</td>
                <td>۳۸ آزمون تخصصی</td>
                <td>تداخل فرانهوفر، فروپاشی ناظر، جابه‌جایی تیغه، مونت‌کارلو</td>
                <td><span class="badge badge-success">۱۰۰٪ موفقیت (Pass)</span></td>
            </tr>
            <tr>
                <td>لانچر و مدیر پردازه‌ها</td>
                <td>سوئیت یکپارچه</td>
                <td>راه‌اندازی، عدم نشت حافظه، ریسپانسیو و فوکوس</td>
                <td><span class="badge badge-success">۱۰۰٪ موفقیت (Pass)</span></td>
            </tr>
        </table>

        <div class="section-title">۹. سناریوهای عملیاتی پیاده‌سازی‌شده برای کلاس درس و آزمایشگاه</div>
        <ul>
            <li><strong>سناریوی ۱ (تدریس کلاسی با ویدئوپروژکتور):</strong> امکان قرارگیری در حالت تمام‌صفحه (F11) یا حالت تئاتر (F10) جهت پنهان‌سازی کنترل‌ها و اختصاص ۱۰۰٪ فضای پرده به نمودارها و تصویر آزمایشگاهی.</li>
            <li><strong>سناریوی ۲ (انجام آزمایش مستقل توسط دانشجو/دانش‌آموز):</strong> دانشجو پارامترها را تنظیم، قرائت ورنیه را تمرین و با دکمه اختصاصی، گزارش رسمی مایکروسافت ورد با معادلات ریاضی استاندارد تولید می‌کند.</li>
            <li><strong>سناریوی ۳ (ارزیابی و آزمون کلاسی تعاملی):</strong> ماژول حدس عنصر ناشناخته در اسپکترومتر و آزمون کلاسی تعاملی در دو شکاف یانگ، آماده اخذ کوییز مستقیم از فراگیران در محیط آموزشی است.</li>
        </ul>

        <div class="section-title">۱۰. تعهد پشتیبانی و بیانیه آمادگی قطعی بهره‌برداری فناوری</div>
        <p style="font-size: 10.5pt; margin-top: 4px;">
            بدین‌وسیله تأیید و گواهی می‌گردد که محصول <strong>«آزمایشگاه مجازی فیزیک»</strong> از مرحله تحقیق، طراحی نظری و نمونه‌سازی عبور نموده و تمامی آزمون‌های صحت محاسبات فیزیکی، سازگاری سیستم‌عامل، مقاومت در برابر رزولوشن‌های گوناگون و استقلال کامل از پیش‌نیازهای نرم‌افزاری را با موفقیت پشت سر گذاشته است. این فناوری هم‌اکنون در قالب بسته توزیع پرتابل، مستندات آموزشی و فایل‌های اجرایی نهایی، <strong>کاملاً آماده بهره‌برداری رسمی در سطح مدارس، پژوهش‌سراهای دانش‌آموزی، پردیس‌های دانشگاه فرهنگیان و دانشکده‌های علوم پایه سراسر کشور</strong> می‌باشد.
        </p>

        <div style="margin-top: 15px; text-align: center;">
            <div style="display: inline-block; border-top: 1px solid #94a3b8; padding-top: 6px; width: 300px;">
                <div style="font-family: 'BTitr', sans-serif; color: #0f172a; font-size: 11pt; margin-bottom: 2px;">پژوهشگر و توسعه‌دهنده فناوری</div>
                <div style="font-size: 12pt; font-weight: bold; color: #0284c7;">امیرمحمد یوسف‌وند</div>
                <div style="font-size: 9.5pt; color: #475569; margin-top: 2px;">دانشجومعلم رشته آموزش علوم تجربی</div>
                <div style="font-size: 9pt; color: #64748b;">دانشگاه فرهنگیان — پردیس شهید باهنر اراک (پاییز ۱۴۰۵)</div>
            </div>
        </div>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۲ آماده بهره‌برداری از فناوری — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۳ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

</body>
</html>
"""

    html_path = os.path.join(root_dir, "doc_readiness_4_2.html")
    pdf_path = os.path.join(root_dir, "(4-2 آماده بهره برداری از فناوری).pdf")

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

    print("[INFO] Rendering TRL 4-2 Readiness PDF using Microsoft Edge...")
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
