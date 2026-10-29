# -*- coding: utf-8 -*-
"""
Script to generate the official Persian PDF document for:
4-7 آماده به‌کارگیری در محیط واقعی (Real-World Operational Deployment Readiness Report)
for Virtual Physics Laboratory Suite (آزمایشگاه مجازی فیزیک).
Includes real environment screenshots, field deployment scenarios, and hardware readiness proofs.
Uses B Titr for headings and B Nazanin for body text with strict vertical pacing.
"""

import os
import subprocess
import base64

def get_base64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

def get_base64_png(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    logo_base64 = get_base64_png(os.path.join(root_dir, "assets", "branding", "icon.png"))

    opt_dir = os.path.join(root_dir, "assets", "screenshots", "opt")
    shot_launcher = get_base64_image(os.path.join(opt_dir, "launcher_screen.jpg"))
    shot_spec = get_base64_image(os.path.join(opt_dir, "spectrometer_screen.jpg"))
    shot_young = get_base64_image(os.path.join(opt_dir, "young_screen.jpg"))

    html_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="fa">
<head>
<meta charset="utf-8">
<title>مستند آماده به‌کارگیری در محیط واقعی — آزمایشگاه مجازی فیزیک</title>
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
    line-height: 1.45;
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

/* Screenshot Figure Boxes */
.figure-card {{
    border: 1px solid #cbd5e1;
    background-color: #f8fafc;
    border-radius: 6px;
    padding: 4px 6px;
    margin-top: 4px;
    margin-bottom: 5px;
    text-align: center;
}}
.figure-img {{
    width: 100%;
    max-height: 72mm;
    object-fit: contain;
    border-radius: 4px;
    border: 1px solid #94a3b8;
    display: block;
    margin: 0 auto;
}}
.figure-img-half {{
    width: 49%;
    max-height: 60mm;
    object-fit: contain;
    border-radius: 4px;
    border: 1px solid #94a3b8;
    display: inline-block;
}}
.figure-caption {{
    font-size: 8.5pt;
    color: #334155;
    margin-top: 3px;
    font-weight: bold;
}}

/* Technical Specs & Data Tables */
.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 3px;
    margin-bottom: 4px;
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

.math-formula {{
    direction: ltr;
    display: inline-block;
    font-family: 'Space Grotesk', 'Consolas', sans-serif;
    font-size: 9.5pt;
    color: #0369a1;
    font-weight: bold;
    padding: 0 2px;
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
<!-- PAGE 1: شناسنامه استقرار در محیط واقعی و مشخصات پکیج پرتابل              -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                کد سند: DOC-DEPLOY-0407<br>
                تاریخ: پاییز ۱۴۰۵<br>
                سطح بلوغ: TRL 8/9 استقرار عملیاتی
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">مستند فنی (۴-۷ آماده به‌کارگیری در محیط واقعی)</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <table class="info-grid">
            <tr>
                <td class="label">عنوان سامانه فناوری:</td>
                <td class="value"><strong>آزمایشگاه مجازی فیزیک (Virtual Physics Laboratory)</strong></td>
                <td class="label">توسعه‌دهنده:</td>
                <td class="value"><strong>امیرمحمد یوسف‌وند</strong><br><small style="color:#475569;">دانشجومعلم رشته آموزش علوم تجربی</small></td>
            </tr>
            <tr>
                <td class="label">وضعیت استقرار محیطی:</td>
                <td class="value"><span class="badge badge-success">آماده به‌کارگیری فوری در محیط واقعی آموزشی</span></td>
                <td class="label">پردیس دانشگاهی:</td>
                <td class="value">دانشگاه فرهنگیان پردیس شهید باهنر اراک</td>
            </tr>
            <tr>
                <td class="label">محیط واقعی هدف:</td>
                <td class="value">مدارس متوسطه، پژوهش‌سراها، آزمایشگاه‌های دانشگاه</td>
                <td class="label">شاخص ارزیابی:</td>
                <td class="value">شاخص ۴-۷ آماده به‌کارگیری در محیط واقعی</td>
            </tr>
        </table>

        <div class="section-title">۱. هدف سند و مفهوم آمادگی به‌کارگیری در محیط واقعی (Real-World Deployment)</div>
        <p style="margin: 2px 0 4px 0;">
            هدف این مستند رسمی، اثبات احراز شرایط <strong>«آماده به‌کارگیری بودن محصول در محیط‌های واقعی»</strong> شامل مدارس، کارگاه‌های رایانه، آزمایشگاه‌های فیزیک دانشگاهی و پژوهش‌سراهای دانش‌آموزی است. سامانه «آزمایشگاه مجازی فیزیک» از مرحله آزمون‌های آزمایشگاهی و محدود عبور کرده و به عنوان یک بسته نرم‌افزاری پایدار، خودکفا و تست‌شده، تمامی الزامات عملکردی، فنی و ارگونومیک لازم برای استفاده عملی توسط معلمان، اساتید و دانش‌آموزان را به طور کامل احراز نموده است.
        </p>

        <div class="section-title">۲. ارکان چهارگانه تسهیل‌کننده استقرار فوری در مدارس و دانشگاه‌ها</div>
        <div class="feature-card">
            <h3>ویژگی‌های متمایز فنی برای حذف موانع اجرایی در محیط واقعی</h3>
            <ul>
                <li><strong>استقرار از روی حافظه فلش (Portable Plug &amp; Play):</strong> بسته نرم‌افزاری کاملاً مستقل بوده و بدون نیاز به نصب (Install-Free)، مستقیماً از روی فلش‌مموری، حافظه اکسترنال یا شبکه محلی مدرسه روی هر رایانه ویندوزی با یک کلیک اجرا می‌شود.</li>
                <li><strong>بی‌نیازی از دسترسی ادمین (Zero Administrative Privileges):</strong> برای اجرای نرم‌افزار نیازی به مجوز مدیر سیستم (Run as Administrator) نبوده و بر روی رایانه‌های عمومی با محدودیت‌های دسترسی سازمانی با موفقیت اجرا می‌گردد.</li>
                <li><strong>استقلال ۱۰۰ درصدی از اینترنت (Fully Offline Capability):</strong> هیچ‌یک از توابع محاسباتی، شبیه‌سازها، داده‌های طیف NIST یا فونت‌ها به سرورهای خارجی وابسته نبوده و در نقاط دورافتاده، روستاها و کلاس‌های فاقد اینترنت عملکرد کامل دارد.</li>
                <li><strong>عدم وابستگی به سخت‌افزار گران‌قیمت:</strong> بهره‌گیری از الگوریتم‌های بهینه‌سازی‌شده برداری، امکان اجرای روان شبیه‌سازها با نرخ ۶۰ فریم بر ثانیه را حتی روی سیستم‌های قدیمی فراهم می‌آورد.</li>
            </ul>
        </div>

        <div class="section-title">۳. نمای محیط واقعی لانچر در حال استقرار و ناوبری شبیه‌سازها</div>
        <div class="figure-card">
            {"<img src='" + shot_launcher + "' class='figure-img' style='max-height: 60mm;'>" if shot_launcher else ""}
            <div class="figure-caption">تصویر شماره ۱: اسکرین‌شات از محیط عملیاتی لانچر مرکزی آزمایشگاه مجازی فیزیک آماده به‌کارگیری و ناوبری شبیه‌سازها</div>
        </div>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۷ آماده به‌کارگیری در محیط واقعی — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۱ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 2: سازگاری با شرایط سخت‌افزاری و شواهد تصویری استقرار                  -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش دوم: آزمون شرایط فیزیکی محیط<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">شواهد استقرار در کلاس‌های درس و انطباق با سخت‌افزارهای گوناگون</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۴. انطباق قطعی با نمایشگرهای کلاسی، پروژکتورها و مانیتورهای قدیمی</div>
        <p style="margin: 2px 0 3px 0; font-size: 10.5pt;">
            در شرایط واقعی محیط‌های آموزشی، تنوع بالایی از تجهیزات نمایش تصویر وجود دارد. این سامانه با تست میدانی در رزولوشن‌های گوناگون اعتبارسنجی شده است:
        </p>

        <table class="data-table">
            <tr>
                <th style="width: 26%;">محیط و تجهیزات واقعی</th>
                <th style="width: 22%;">وضوح تصویر</th>
                <th style="width: 32%;">مکانیزم پاسخ‌گویی نرم‌افزار</th>
                <th style="width: 20%;">وضعیت کارکرد</th>
            </tr>
            <tr>
                <td>ویدئوپروژکتور سالن و کلاس</td>
                <td>1280 × 720 (720p)</td>
                <td>کاهش هوشمند ارتفاع پنجره و فیت با تسک‌بار</td>
                <td><span class="badge badge-success">بدون برش فوتر</span></td>
            </tr>
            <tr>
                <td>مانیتورهای قدیمی کارگاه مدرسه</td>
                <td>1024 × 768 (4:3)</td>
                <td>تغییر خودکار گرید لانچر به تک‌ستونی</td>
                <td><span class="badge badge-success">دسترسی کامل اسکرول</span></td>
            </tr>
            <tr>
                <td>لپ‌تاپ‌های اداری معلمان</td>
                <td>1366 × 768</td>
                <td>تنظیم فونت ۱۰ بولد برای تب‌های هفت‌گانه</td>
                <td><span class="badge badge-success">بدون هم‌پوشانی</span></td>
            </tr>
            <tr>
                <td>نمایشگرهای جدید دسکتاپ</td>
                <td>1080p Full HD / 4K</td>
                <td>فعال‌سازی مقیاس‌بندی نیتیو DPI Awareness</td>
                <td><span class="badge badge-success">حداکثر وضوح گرافیک</span></td>
            </tr>
        </table>

        <div class="section-title">۵. تصاویر محیط کارکردی واقعی شبیه‌سازها در حال آزمایش و اندازه‌گیری</div>
        <div class="figure-card" style="margin-bottom: 4px;">
            <div style="display: flex; justify-content: space-between;">
                {"<img src='" + shot_spec + "' class='figure-img-half'>" if shot_spec else ""}
                {"<img src='" + shot_young + "' class='figure-img-half'>" if shot_young else ""}
            </div>
            <div class="figure-caption">تصاویر شماره ۲ و ۳: اسکرین‌شات از محیط عملیاتی شبیه‌ساز اسپکترومتر اپتیکی (راست) و شبیه‌ساز دو شکاف یانگ (چپ) در حال کارکرد واقعی</div>
        </div>

        <div class="section-title">۶. سناریوهای استقرار کلاسی و دانشگاهی در محیط واقعی</div>
        <ul>
            <li><strong>سناریوی تدریس زنده مدرس (Instructor Live Presentation):</strong> استفاده از کلید F11 برای حالت تمام‌صفحه و کلید F10 برای حالت تئاتر (جمعه شدن سایدبار و اختصاص ۱۰۰٪ تصویر به نمودارها جهت نمایش از طریق پروژکتور).</li>
            <li><strong>سناریوی آزمایش مستقل دانشجو (Student Autonomous Lab Session):</strong> انجام مراحل آزمایش با گونیومتر، ثبت زوایا، مشاهده نوارهای تداخل و استخراج فوری گزارش مستند آزمایشگاهی بدون نیاز به مربی.</li>
            <li><strong>سناریوی ارزیابی و آزمون کلاسی تعاملی:</strong> ماژول مسأله معکوس جهت شناسایی عنصر مجهول و کوییز مفاهیم اپتیک موجی برای ارزشیابی تشخیصی فراگیران در کلاس درس.</li>
        </ul>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۷ آماده به‌کارگیری در محیط واقعی — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۲ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 3: بسته‌های نهایی توزیع، دسترسی عمومی و تأییدیه استقرار               -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش سوم: پکیج توزیع و تأییدیه استقرار<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">مشخصات بسته توزیع نهایی، خروجی‌های آزمایشگاهی و بیانیه استقرار</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۷. خروجی‌های معتبر دانشگاهی برای ادغام در فرآیند آموزشی واقعی</div>
        <p style="margin: 2px 0 3px 0;">
            نرم‌افزار تنها به نمایش تصویری محدود نمی‌شود، بلکه داده‌های تجربی حاصل از شبیه‌سازی را در فرمت‌های کاملاً استاندارد و قابل استفاده در نظام دانشگاهی صادر می‌نماید:
        </p>

        <table class="data-table">
            <tr>
                <th style="width: 25%;">نوع خروجی تولیدشده</th>
                <th style="width: 45%;">ویژگی و فرمت خروجی</th>
                <th style="width: 30%;">کاربرد در محیط واقعی</th>
            </tr>
            <tr>
                <td><strong>گزارش کار رسمی Word</strong></td>
                <td>فرمت DOCX با معادلات ریاضی نیتیو OMML و جداول منظم</td>
                <td>تحویل به عنوان گزارش کار معتبر دانشجویی</td>
            </tr>
            <tr>
                <td><strong>دیتاست عددی CSV</strong></td>
                <td>جدول ۲۲ ستونه شامل مختصات، شدت و فاز با کدگذاری UTF-8-SIG</td>
                <td>تحلیل عددی در نرم‌افزارهای متلب و اکسل</td>
            </tr>
            <tr>
                <td><strong>مدل‌های سه‌بعدی OBJ</strong></td>
                <td>فایل‌های هندسی استاندارد 3D همراه با کتابخانه متریال MTL</td>
                <td>چاپ سه‌بعدی و تجسم در نرم‌افزارهای CAD</td>
            </tr>
            <tr>
                <td><strong>تصاویر علمی باکیفیت</strong></td>
                <td>تصاویر نمودارها با رزولوشن ۳۰۰ DPI با پالت‌های علمی Turbo/Inferno</td>
                <td>درج در مقالات علمی، پایان‌نامه‌ها و پوسترها</td>
            </tr>
        </table>

        <div class="section-title">۸. بسته توزیع پرتابل نهایی و کانال‌های انتشار عمومی</div>
        <ul>
            <li><strong>پکیج پرتابل جامع جشنواره (ZIP Bundle):</strong> فایل فشرده <code>CFU_Virtual_Laboratory_v1.0.0.zip</code> شامل فایل‌های باینری کامپایل‌شده، پوشه شبیه‌سازها و راهنمای مکتوب فارسی آماده بارگذاری و انتشار است.</li>
            <li><strong>ریپازیتوری‌های رسمی در گیت‌هاب:</strong> تمامی سورس‌کدها، آزمون‌های خودکار و ریلیزهای رسمی در حساب کاربری توسعه‌دهنده به آدرس <code>github.com/AmirMoYousefVand</code> به صورت دسترسی آزاد (Open Access) منتشر شده‌اند.</li>
        </ul>

        <div class="section-title">۹. گواهی و بیانیه رسمی آمادگی قطعی به‌کارگیری در محیط واقعی</div>
        <p style="font-size: 10.5pt; margin-top: 3px;">
            بدین‌وسیله رسماً تأیید و گواهی می‌گردد که سامانه <strong>«آزمایشگاه مجازی فیزیک»</strong> از بالاترین سطح آمادگی عملیاتی برخوردار بوده و تمامی آزمون‌های عملکردی در شرایط واقعی، سازگاری با سیستم‌های گوناگون آموزشی و استقلال کامل از پیش‌نیازهای نرم‌افزاری و اینترنت را با موفقیت سپری نموده است. این محصول نرم‌افزاری <strong>هم‌اکنون به صورت ۱۰۰٪ آماده به‌کارگیری و بهره‌برداری در مدارس، پژوهش‌سراها و دانشگاه‌های سراسر کشور</strong> می‌باشد.
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
        <span>مستند ۴-۷ آماده به‌کارگیری در محیط واقعی — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۳ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

</body>
</html>
"""

    html_path = os.path.join(root_dir, "doc_deploy_4_7.html")
    pdf_path = os.path.join(root_dir, "4-7 آماده به‏ کارگیری در محیط واقعی.pdf")

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

    print("[INFO] Rendering Real-World Deployment PDF using Microsoft Edge...")
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
