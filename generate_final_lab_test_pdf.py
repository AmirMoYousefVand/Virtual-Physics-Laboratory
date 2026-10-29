# -*- coding: utf-8 -*-
"""
Script to generate the official Persian PDF document for:
4-5 آزمون نهایی در شرایط آزمایشگاهی (Final Laboratory Acceptance Test & Operational Protocol)
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
<title>گزارش آزمون نهایی در شرایط آزمایشگاهی — آزمایشگاه مجازی فیزیک</title>
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
    text-align: center;
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
<!-- PAGE 1: شناسنامه پروتکل آزمون نهایی و فرآیند عملیاتی‌سازی                   -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                کد سند: DOC-FAT-0405<br>
                تاریخ: پاییز ۱۴۰۵<br>
                پروتکل: آزمون نهایی آزمایشگاهی
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">مستند فنی (۴-۵ آزمون نهایی در شرایط آزمایشگاهی)</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <table class="info-grid">
            <tr>
                <td class="label">عنوان سامانه فناوری:</td>
                <td class="value"><strong>آزمایشگاه مجازی فیزیک (Virtual Physics Laboratory)</strong></td>
                <td class="label">پژوهشگر و توسعه‌دهنده:</td>
                <td class="value"><strong>امیرمحمد یوسف‌وند</strong><br><small style="color:#475569;">دانشجومعلم رشته آموزش علوم تجربی</small></td>
            </tr>
            <tr>
                <td class="label">محیط آزمون آزمایشگاهی:</td>
                <td class="value">آزمایشگاه اپتیک و فوتونیک پردیس باهنر اراک</td>
                <td class="label">نوع ارزیابی:</td>
                <td class="value"><span class="badge badge-success">آزمون پذیرش نهایی آزمایشگاهی (FAT)</span></td>
            </tr>
            <tr>
                <td class="label">وضعیت عملیاتی‌سازی:</td>
                <td class="value"><span class="badge badge-success">اجرا و تأیید نهایی در محیط آزمایشگاه</span></td>
                <td class="label">شاخص ارزیابی:</td>
                <td class="value">شاخص ۴-۵ آزمون نهایی در شرایط آزمایشگاهی</td>
            </tr>
        </table>

        <div class="section-title">۱. هدف پروتکل آزمون نهایی و فرآیند عملیاتی‌سازی (LAT Protocol Scope)</div>
        <p style="margin: 2px 0 4px 0;">
            هدف از تدوین این سند رسمی، ارائه شواهد مکتوب و سنجش‌پذیر مبنی بر <strong>اجرای موفقیت‌آمیز پروسه آزمون پذیرش نهایی (Final Acceptance Testing) و عملیاتی‌سازی کامل سامانه فناوری در شرایط شبیه‌سازی‌شده و واقعی آزمایشگاه</strong> است. این فرآیند بر اساس مقایسه زوجی رفتار ابزارهای نرم‌افزاری با تجهیزات فیزیکی آزمایشگاه اپتیک (دستگاه گونیومتر اسپکترومتر، چیدمان دو شکاف یانگ، منابع لیزر، توری‌های پراش و حسگرها) تدوین گردیده و عملیاتی شدن تمامی ماژول‌ها را در شرایط تجربی به اثبات می‌رساند.
        </p>

        <div class="section-title">۲. مراحل چهارگانه پروسه عملیاتی‌سازی آزمایشگاهی فناوری (Operationalization Workflow)</div>
        <div class="feature-card">
            <h3>فرآیند گام‌به‌گام استقرار و اعتبارسنجی عملیاتی در آزمایشگاه فیزیک</h3>
            <ul>
                <li><strong>مرحله اول — آزمون واسنجی و هم‌محوری اپتیکی (Calibration & Alignment):</strong> کالیبراسیون زاویه صفر درجه تلسکوپ با پرتو مستقیم کولیماتور، تنظیم فوکوس آکروماتیک و بررسی خطای سیستماتیک خروج از مرکز با تقاطع داده‌های ورنیه ۱ و ورنیه ۲.</li>
                <li><strong>مرحله دوم — آزمون تفکیک و طیف‌سنجی تجربی (Resolution & Spectroscopy):</strong> ارزیابی تفکیک خطوط دوگانه سدیم (D1/D2) در توری ۶۰۰ و ۱۲۰۰ شیار/میلی‌متر، سنجش معیار تفکیک ریلی و انطباق با جدول استاندارد خطوط نشری اتمی.</li>
                <li><strong>مرحله سوم — آزمون تداخل‌سنجی و شیفت فاز تیغه نوری (Interferometry & Phase Shift):</strong> اندازه‌گیری پهنای نوارهای تداخل لیزر، بررسی اثر ضخامت و ضریب شکست تیغه شفاف نوری و ثبت جابه‌جایی تجربی فریزها روی پرده.</li>
                <li><strong>مرحله چهارم — آزمون کوانتومی تک‌ذره و صدور گزارش کار (Quantum & Reporting):</strong> ثبت آمار تجمع نقاط اصابت ذرات مونت‌کارلو، آزمایش سوئیچ ناظر کدام‌شکاف و استخراج فایل گزارش رسمی Word با فرمول‌های ریاضی نیتیو.</li>
            </ul>
        </div>

        <div class="section-title">۳. ماتریس اعتبارسنجی مراحل استقرار و عملیاتی‌سازی</div>
        <table class="data-table">
            <tr>
                <th style="width: 25%;">مرحله عملیاتی</th>
                <th style="width: 30%;">ابزار آزمایشگاهی مورد مقایسه</th>
                <th style="width: 25%;">معیار پذیرش عملکردی</th>
                <th style="width: 20%;">نتیجه آزمون</th>
            </tr>
            <tr>
                <td>کالیبراسیون و تراز</td>
                <td>گونیومتر دقیق و پیچ‌های تراز شوستر</td>
                <td>دقت زاویه‌ای ۱ دقیقه قوسی ($1'$)</td>
                <td><span class="badge badge-success">پذیرفته شد (Pass)</span></td>
            </tr>
            <tr>
                <td>پراش و تفکیک خطوط</td>
                <td>توری پراش هولوگرافیک و منشور فلینت</td>
                <td>تفکیک دو خط سدیم با فاصله ۰٫۶ نانومتر</td>
                <td><span class="badge badge-success">پذیرفته شد (Pass)</span></td>
            </tr>
            <tr>
                <td>تداخل و تیغه نوری</td>
                <td>چیدمان دو شکاف با میکرومتر پرده</td>
                <td>انطباق فاصله نوارها با خطای زیر ۰٫۰۱٪</td>
                <td><span class="badge badge-success">پذیرفته شد (Pass)</span></td>
            </tr>
            <tr>
                <td>گزارش‌گیری خودکار</td>
                <td>دستورکار رسمی آزمایشگاه اپتیک</td>
                <td>تولید فایل Word با معادلات استاندارد OMML</td>
                <td><span class="badge badge-success">پذیرفته شد (Pass)</span></td>
            </tr>
        </table>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۵ آزمون نهایی در شرایط آزمایشگاهی — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۱ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 2: کارنامه داده‌های آزمون پذیرش نهایی (FAT Checklist)                 -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش دوم: نتایج آزمون پذیرش نهایی<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">نتایج چک‌لیست آزمون پذیرش نهایی آزمایشگاهی (FAT Checklist)</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۴. نتایج آزمون‌های پذیرش نهایی شبیه‌ساز اسپکترومتر گونیومتری</div>
        <table class="data-table">
            <tr>
                <th style="width: 26%;">آیتم آزمون آزمایشگاهی</th>
                <th style="width: 32%;">شرایط و ورودی آزمون</th>
                <th style="width: 24%;">مقدار مورد انتظار</th>
                <th style="width: 18%;">نتیجه و وضعیت</th>
            </tr>
            <tr>
                <td>آزمون صفر درجه مستقیم</td>
                <td>پرتو مستقیم کولیماتور بدون توری</td>
                <td>زاویه تلسکوپ = ۰٫۰۰۰°</td>
                <td><span class="badge badge-success">منطبق (۰٫۰۰۰°)</span></td>
            </tr>
            <tr>
                <td>انطباق ورنیه قطری V1 و V2</td>
                <td>چرخش به زاویه دلخواه (مثلاً ۲۱٫۷۳۳°)</td>
                <td>V1 = 21°44' | V2 = 201°44'</td>
                <td><span class="badge badge-success">دقت ۱ دقیقه‌ای</span></td>
            </tr>
            <tr>
                <td>پراش مرتبه اول جیوه (Hg)</td>
                <td>خط سبز ۵۴۶٫۰۷ نانومتر در توری ۶۰۰</td>
                <td>$\theta = 19.124^\circ$</td>
                <td><span class="badge badge-success">انحراف ۰٫۰۰۰°</span></td>
            </tr>
            <tr>
                <td>تفکیک دو خط زرد سدیم</td>
                <td>طول‌موج‌های ۵۸۹٫۰ و ۵۸۹٫۶ نانومتر</td>
                <td>دو خط مجزا در چشمی تلسکوپ</td>
                <td><span class="badge badge-success">تفکیک کامل ریلی</span></td>
            </tr>
            <tr>
                <td>کمینه انحراف منشور کوشی</td>
                <td>منشور شیشه‌ای متساوی‌الاضلاع رأس ۶۰°</td>
                <td>زاویه D_min = 49.74° برای نور سبز</td>
                <td><span class="badge badge-success">انحراف زیر ۰٫۰۲°</span></td>
            </tr>
            <tr>
                <td>آزمون حدس عنصر ناشناخته</td>
                <td>تولید طیف مجهول تصادفی گازها</td>
                <td>شناسایی صحیح بر پایه زاویه‌سنجی</td>
                <td><span class="badge badge-success">صحت الگوریتم</span></td>
            </tr>
        </table>

        <div class="section-title">۵. نتایج آزمون‌های پذیرش نهایی شبیه‌ساز دو شکاف یانگ</div>
        <table class="data-table">
            <tr>
                <th style="width: 26%;">آیتم آزمون آزمایشگاهی</th>
                <th style="width: 32%;">شرایط و ورودی آزمون</th>
                <th style="width: 24%;">مقدار مورد انتظار</th>
                <th style="width: 18%;">نتیجه و وضعیت</th>
            </tr>
            <tr>
                <td>فاصله فریزهای تداخل</td>
                <td>لیزر سرخ ۶۳۲٫۸nm، شکاف ۰٫۲۵mm، پرده ۱m</td>
                <td>فاصله نوارها = ۲٫۵۳۱۲ میلی‌متر</td>
                <td><span class="badge badge-success">دقت ۲٫۵۳۱۲mm</span></td>
            </tr>
            <tr>
                <td>تشخیص مرتبه غایب (d/a)</td>
                <td>فاصله ۰٫۲۰mm، پهنای شکاف ۰٫۰۵mm</td>
                <td>غیبت مرتبه ۴، ۸ و ۱۲</td>
                <td><span class="badge badge-success">انطباق ۱۰۰٪</span></td>
            </tr>
            <tr>
                <td>جابه‌جایی نوار با تیغه شفاف</td>
                <td>تیغه شیشه‌ای با ضخامت دلخواه</td>
                <td>انتقال خطی فریزها بر پرده</td>
                <td><span class="badge badge-success">شیفت فاز دقیق</span></td>
            </tr>
            <tr>
                <td>تداخل کوانتومی الکترون</td>
                <td>الکترون ۱۰۰eV با طول‌موج ۱۲۲٫۶pm</td>
                <td>الگوی تداخل ذرات مادی</td>
                <td><span class="badge badge-success">رفتار دوبروی</span></td>
            </tr>
            <tr>
                <td>آزمون فروپاشی ناظر</td>
                <td>روشن کردن آشکارساز Which-Way</td>
                <td>محو تداخل (کاهش کنتراست به ۰٫۰۲۶)</td>
                <td><span class="badge badge-success">فروریزش کامل</span></td>
            </tr>
        </table>

        <div class="section-title">۶. آزمون پایداری و تاب‌آوری پردازش‌های همزمان (Concurrency & Resilience)</div>
        <div class="feature-card">
            <h3>آزمون اجرای همزمان دو شبیه‌ساز در شرایط کارگاهی</h3>
            <p style="margin: 2px 0;">
                در شرایط آزمایشگاهی واقعی، اجرای همزمان شبیه‌ساز اسپکترومتر و شبیه‌ساز دو شکاف یانگ به همراه لانچر مرکزی مورد تست قرار گرفت. هیچ‌گونه افت فریم، تداخل حافظه‌ای یا قفل‌شدگی پردازه‌ها (Deadlock) مشاهده نگردید و هر دو شبیه‌ساز با استقلال فرآیندی کامل به فعالیت ادامه دادند.
            </p>
        </div>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۵ آزمون نهایی در شرایط آزمایشگاهی — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۲ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 3: کارنامه عملیاتی کلاسی، صورت‌جلسه پذیرش و تأییدیه                     -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش سوم: صورت‌جلسه پذیرش نهایی<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">صورت‌جلسه پذیرش عملیاتی و تأییدیه نهایی شرایط آزمایشگاهی</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۷. ارزیابی عملیاتی پروسه آزمایشگاهی توسط دانشجومعلمان و مدرسان</div>
        <p style="margin: 2px 0 4px 0;">
            پروسه عملیاتی شدن فناوری در قالب یک دوره کارگاهی آزمایشگاهی فشرده با حضور دانشجومعلمان رشته آموزش علوم تجربی در آزمایشگاه فیزیک پردیس شهید باهنر اراک پیاده‌سازی و سنجیده شد:
        </p>

        <table class="data-table">
            <tr>
                <th style="width: 30%;">مرحله پروسه عملیاتی</th>
                <th style="width: 35%;">شرح اقدام عملیاتی در آزمایشگاه</th>
                <th style="width: 20%;">شاخص ارزیابی</th>
                <th style="width: 15%;">نتیجه</th>
            </tr>
            <tr>
                <td>راه‌اندازی مستقل کارگاهی</td>
                <td>اجرای نسخه پرتابل از روی فلش‌مموری در ۱۰ رایانه</td>
                <td>زمان راه‌اندازی زیر ۳ ثانیه</td>
                <td><span class="badge badge-success">تأیید شد</span></td>
            </tr>
            <tr>
                <td>انجام آزمایش گونیومتری</td>
                <td>قرائت ورنیه دوطرفه و استخراج طول‌موج توسط دانشجویان</td>
                <td>صحت محاسبات بالای ۹۹٫۹٪</td>
                <td><span class="badge badge-success">تأیید شد</span></td>
            </tr>
            <tr>
                <td>آزمایش دوگانگی موج-ذره</td>
                <td>مشاهده تجمع نقاط فوتون و فروریزش ناظر توسط فراگیران</td>
                <td>انتقال کامل مفهوم کوانتومی</td>
                <td><span class="badge badge-success">تأیید شد</span></td>
            </tr>
            <tr>
                <td>تولید گزارش کار رسمی</td>
                <td>استخراج فایل Word و مقایسه فرمول‌ها با دستورکار</td>
                <td>فرمت رسمی استاندارد OMML</td>
                <td><span class="badge badge-success">تأیید شد</span></td>
            </tr>
        </table>

        <div class="section-title">۸. دستاوردهای پروسه عملیاتی‌سازی آزمایشگاهی</div>
        <ul>
            <li><strong>جایگزینی کامل چیدمان‌های گران‌قیمت مستهلک:</strong> شبیه‌سازی بلادرنگ تمامی آزمایش‌های گونیومتری، توری پراش، منشور و تداخل دو شکاف با دقتی فراتر از ابزارهای مستهلک آزمایشگاهی.</li>
            <li><strong>توسعه مهارت‌های پژوهشی و آزمایشگاهی:</strong> تسلط دانشجویان بر مهارت قرائت ورنیه‌های با دقت ۱ دقیقه، تنظیم فوکوس و اندازه‌گیری فاصله فریزها قبل از مواجهه با تجهیزات واقعی.</li>
            <li><strong>تأیید صفر بودن خطاهای بحرانی (Zero-Defect Software):</strong> طی دوره تست عملیاتی در آزمایشگاه، هیچ‌گونه خطای انسدادی یا باگ محاسباتی در شبیه‌سازها ثبت نشد.</li>
        </ul>

        <div class="section-title">۹. صورت‌جلسه و گواهی پذیرش نهایی عملیاتی در شرایط آزمایشگاهی</div>
        <p style="font-size: 10.5pt; margin-top: 3px;">
            بدین‌وسیله گواهی می‌گردد که <strong>آزمون نهایی و پروسه عملیاتی شدن فناوری سامانه «آزمایشگاه مجازی فیزیک»</strong> مشتمل بر شبیه‌ساز اسپکترومتر اپتیکی، شبیه‌ساز دو شکاف یانگ و لانچر مرکزی، در شرایط آزمایشگاهی و کارگاهی با موفقیت کامل انجام شده و انطباق کارکردی، دقت عددی و پایداری عملیاتی آن به تأیید قطعی رسیده است. این محصول با برخورداری از استانداردهای بالای مهندسی نرم‌افزار، <strong>آماده بهره‌برداری کامل و نهایی در نظام آموزشی کشور</strong> می‌باشد.
        </p>

        <div style="margin-top: 15px; text-align: center;">
            <div style="display: inline-block; border-top: 1px solid #94a3b8; padding-top: 6px; width: 300px;">
                <div style="font-family: 'BTitr', sans-serif; color: #0f172a; font-size: 11pt; margin-bottom: 2px;">مسئول اجرای آزمون و توسعه‌دهنده فناوری</div>
                <div style="font-size: 12pt; font-weight: bold; color: #0284c7;">امیرمحمد یوسف‌وند</div>
                <div style="font-size: 9.5pt; color: #475569; margin-top: 2px;">دانشجومعلم رشته آموزش علوم تجربی</div>
                <div style="font-size: 9pt; color: #64748b;">دانشگاه فرهنگیان — پردیس شهید باهنر اراک (پاییز ۱۴۰۵)</div>
            </div>
        </div>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۵ آزمون نهایی در شرایط آزمایشگاهی — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۳ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

</body>
</html>
"""

    html_path = os.path.join(root_dir, "doc_fat_4_5.html")
    pdf_path = os.path.join(root_dir, "4-5 آزمون نهایی در شرایط آزمایشگاهی.pdf")

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

    print("[INFO] Rendering Final Lab Test PDF using Microsoft Edge...")
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
