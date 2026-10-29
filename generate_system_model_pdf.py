# -*- coding: utf-8 -*-
"""
Script to generate the official Persian PDF document for:
4-6 تولید نمونه اولیه (مدل سیستمی) - System Prototype & Real-Scale Software Implementation Report
Includes real screenshots from the running environments of Launcher, Spectrometer, and Young Double-Slit simulators.
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
    shot_vernier = get_base64_image(os.path.join(opt_dir, "spectrometer_verniers.jpg"))
    shot_young = get_base64_image(os.path.join(opt_dir, "young_screen.jpg"))
    shot_young_3d = get_base64_image(os.path.join(opt_dir, "young_3d.jpg"))

    html_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="fa">
<head>
<meta charset="utf-8">
<title>مستند تولید نمونه اولیه (مدل سیستمی) — آزمایشگاه مجازی فیزیک</title>
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
    margin-bottom: 6px;
    text-align: center;
}}
.figure-img {{
    width: 100%;
    max-height: 78mm;
    object-fit: contain;
    border-radius: 4px;
    border: 1px solid #94a3b8;
    display: block;
    margin: 0 auto;
}}
.figure-img-half {{
    width: 49%;
    max-height: 62mm;
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
<!-- PAGE 1: شناسنامه مدل سیستمی، انطباق ابعاد واقعی و اسکرین‌شات لانچر      -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                کد سند: DOC-SYSMOD-0406<br>
                تاریخ: پاییز ۱۴۰۵<br>
                وضعیت: مدل سیستمی ابعاد واقعی
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">مستند فنی (۴-۶ تولید نمونه اولیه - مدل سیستمی)</div>
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
                <td class="label">نوع نمونه اولیه:</td>
                <td class="value"><span class="badge badge-success">مدل سیستمی یکپارچه در ابعاد واقعی کارکرد</span></td>
                <td class="label">پردیس دانشگاهی:</td>
                <td class="value">دانشگاه فرهنگیان پردیس شهید باهنر اراک</td>
            </tr>
            <tr>
                <td class="label">تأییدیه آزمایشگاهی:</td>
                <td class="value"><span class="badge badge-success">تأییدشده در کارگاه آزمایشگاه فیزیک دانشگاه</span></td>
                <td class="label">شاخص ارزیابی:</td>
                <td class="value">شاخص ۴-۶ تولید نمونه اولیه (مدل سیستمی)</td>
            </tr>
        </table>

        <div class="section-title">۱. مفهوم مدل سیستمی در فناوری نرم‌افزاری و شبیه‌سازی آزمایشگاهی</div>
        <p style="margin: 2px 0 4px 0;">
            در مهندسی سیستم‌ها و توسعه نرم‌افزارهای شبیه‌ساز پژوهشی، <strong>«مدل سیستمی (System Prototype / System Model)»</strong> به نمونه‌ای عملیاتی و یکپارچه اطلاق می‌شود که در آن تمامی زیرسیستم‌ها (موتورهای محاسباتی فیزیک، مدل‌های سینماتیکی، موتورهای ترسیم گرافیکی، هسته مدیریت فرآیندها، و ابزارهای استخراج داده) در قالب یک چیدمان کلان گردآوری شده و <strong>در مقیاس و ابعاد کاملاً واقعی (1:1 Real-Scale Physical Dimensions)</strong> مطابق با نمونه فیزیکی آزمایشگاه عمل می‌کنند.
        </p>

        <div class="section-title">۲. انطباق ابعاد واقعی فیزیکی در مدل سیستمی (Physical Real-Scale Fidelity)</div>
        <p style="margin: 2px 0 3px 0; font-size: 10.5pt;">
            کلیه متغیرها و اجزای فیزیکی شبیه‌سازها در مقیاس واقعی استاندارد مترولوژی پیاده‌سازی شده‌اند:
        </p>
        <ul style="font-size: 10pt;">
            <li><strong>ابعاد واقعی گونیومتر:</strong> دایره مدرج ۳۶۰ درجه اصلی با گام‌های ۳۰ دقیقه قوسی (۳۰ دقیقه یا ۰٫۵ درجه)، دو ورنیه مستقل با دقت خوانش ۱ دقیقه قوسی (۱ دقیقه یا ۱/۶۰ درجه)، فاصله کانونی کولیماتور و تلسکوپ ۱۷۸ میلی‌متر، و زاویه رأس منشور ۶۰ درجه.</li>
            <li><strong>ابعاد واقعی چیدمان دو شکاف:</strong> طول‌موج نور ۳۸۰ تا ۷۸۰ نانومتر، فاصله شکاف‌ها ۰٫۱ تا ۱ میلی‌متر، پهنای شکاف ۰٫۰۲ تا ۰٫۱ میلی‌متر، فاصله تا پرده ۰٫۵ تا ۳ متر، و ضخامت تیغه نوری ۰ تا ۵۰ میکرومتر.</li>
            <li><strong>ثابت‌های بنیادین جهانی:</strong> سرعت نور (<span class="math-formula">c</span>)، ثابت پلانک (<span class="math-formula">h</span>)، بار بنیادی (<span class="math-formula">e</span>) و ثابت ریدبرگ (<span class="math-formula">R<sub>H</sub></span>) منطبق بر مقادیر رسمی بین‌المللی CODATA 2018.</li>
        </ul>

        <div class="section-title">۳. نمای واقعی محیط نرم‌افزار لانچر مجتمع مرکزی (مدل سیستمی ناوبری)</div>
        <div class="figure-card">
            {"<img src='" + shot_launcher + "' class='figure-img' style='max-height: 65mm;'>" if shot_launcher else ""}
            <div class="figure-caption">تصویر شماره ۱: اسکرین‌شات واقعی از رابط کاربری لانچر مرکزی آزمایشگاه مجازی فیزیک (کارت‌های مدرن تیتانیومی، فیلترهای موضوعی و پیوند گیت‌هاب)</div>
        </div>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۶ تولید نمونه اولیه (مدل سیستمی) — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۱ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 2: اسکرین‌شات‌ها و تشریح مدل سیستمی اسپکترومتر اپتیکی                 -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش دوم: مدل سیستمی اسپکترومتر<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">شواهد تصویری و مشخصات مدل سیستمی اسپکترومتر اپتیکی</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۴. اسکرین‌شات‌های واقعی از محیط عملیاتی شبیه‌ساز اسپکترومتر</div>
        <div class="figure-card" style="margin-bottom: 4px;">
            <div style="display: flex; justify-content: space-between;">
                {"<img src='" + shot_spec + "' class='figure-img-half'>" if shot_spec else ""}
                {"<img src='" + shot_vernier + "' class='figure-img-half'>" if shot_vernier else ""}
            </div>
            <div class="figure-caption">تصاویر شماره ۲ و ۳: اسکرین‌شات‌های واقعی از چشمی تلسکوپ با خطوط طیفی جیوه (راست) و ذره‌بین ورنیه‌های دوطرفه با دقت ۱ دقیقه (چپ)</div>
        </div>

        <div class="section-title">۵. کالبدشناسی فنی زیرسیستم‌های مدل اسپکترومتر</div>
        <table class="data-table">
            <tr>
                <th style="width: 25%;">زیرسیستم مدل</th>
                <th style="width: 40%;">مشخصات مهندسی در ابعاد واقعی</th>
                <th style="width: 35%;">خروجی آزمایشگاهی</th>
            </tr>
            <tr>
                <td><strong>گونیومتر و ورنیه‌ها</strong></td>
                <td>دایره مدرج ۳۶۰°، ورنیه‌های ۱ و ۲ با تفکیک MSR و VSR</td>
                <td>قرائت زاویه با دقت ۱ دقیقه قوسی (<span class="math-formula">1'</span>)</td>
            </tr>
            <tr>
                <td><strong>کولیماتور و چشمی</strong></td>
                <td>تار رتیکل متقاطع، پیچ میکرومتری مماس &plusmn;۵ درجه و فوکوس</td>
                <td>شبیه‌سازی خطای تاری کانونی PSF</td>
            </tr>
            <tr>
                <td><strong>توری پراش و منشور</strong></td>
                <td>توری ۳۰۰، ۶۰۰ و ۱۲۰۰ شیار/میلی‌متر، منشور متساوی‌الاضلاع</td>
                <td>محاسبه کمینه انحراف و پاشندگی کوشی</td>
            </tr>
            <tr>
                <td><strong>بانک طیف نشری NIST</strong></td>
                <td>طول‌موج‌های اتمی دقیق جیوه، سدیم، هیدروژن، هلیوم و نئون</td>
                <td>تفکیک خطوط دوگانه سدیم با فاصله ۰٫۶ نانومتر</td>
            </tr>
        </table>

        <div class="section-title">۶. نوآوری‌های مهندسی مدل سیستمی اسپکترومتر</div>
        <ul>
            <li><strong>حذف خطای خروج از مرکز محور دوران:</strong> پیاده‌سازی فرمول میانگین‌گیری زاویه‌ای ورنیه ۱ و ۲ جهت تصحیح انحراف ساختاری محور گونیومتر.</li>
            <li><strong>تولید گزارش رسمی آزمایشگاه با معادلات OMML:</strong> صدور مستقیم فایل Word شامل جداول زوایا، محاسبات طول‌موج و خطای نسبی با فرمت رسمی.</li>
        </ul>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۶ تولید نمونه اولیه (مدل سیستمی) — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۲ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 3: اسکرین‌شات‌ها و تشریح مدل سیستمی دو شکاف یانگ و تأییدیه             -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش سوم: مدل سیستمی دو شکاف یانگ<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">شواهد تصویری مدل سیستمی دو شکاف و تأییدیه نهایی</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۷. اسکرین‌شات‌های واقعی از محیط عملیاتی شبیه‌ساز دو شکاف یانگ</div>
        <div class="figure-card" style="margin-bottom: 4px;">
            <div style="display: flex; justify-content: space-between;">
                {"<img src='" + shot_young + "' class='figure-img-half'>" if shot_young else ""}
                {"<img src='" + shot_young_3d + "' class='figure-img-half'>" if shot_young_3d else ""}
            </div>
            <div class="figure-caption">تصاویر شماره ۴ و ۵: اسکرین‌شات‌های واقعی از پرده آشکارساز دوبعدی و متریک‌ها (راست) و نمای سه‌بعدی چیدمان آزمایشگاهی با تیغه نوری (چپ)</div>
        </div>

        <div class="section-title">۸. کالبدشناسی فنی زیرسیستم‌های مدل دو شکاف یانگ</div>
        <table class="data-table">
            <tr>
                <th style="width: 25%;">زیرسیستم مدل</th>
                <th style="width: 40%;">مشخصات مهندسی در ابعاد واقعی</th>
                <th style="width: 35%;">خروجی آزمایشگاهی</th>
            </tr>
            <tr>
                <td><strong>اپتیک موجی کلاسیک</strong></td>
                <td>پراش فرانهوفر با چشمه تک‌شکاف <span class="math-formula">S<sub>0</sub></span> و تیغه شیشه‌ای فاز</td>
                <td>محاسبه فاصله فریزها با دقت میکرومتری</td>
            </tr>
            <tr>
                <td><strong>مکانیک کوانتومی</strong></td>
                <td>نمونه‌برداری مونت‌کارلو برای فوتون، الکترون و باکی‌بال <span class="math-formula">C<sub>60</sub></span></td>
                <td>ثبت تجمع دانه‌دانه ذرات با طول‌موج دوبروی</td>
            </tr>
            <tr>
                <td><strong>آشکارساز ناظر</strong></td>
                <td>سوئیچ Which-Way و مدل‌سازی ریاضی تخریب همدوسی</td>
                <td>نمایش عینی فروریزش تابع موج کوانتومی</td>
            </tr>
            <tr>
                <td><strong>خروجی‌های مهندسی</strong></td>
                <td>دیتاست علمی ۲۲ ستونه CSV، مدل سه‌بعدی OBJ و پکیج ZIP</td>
                <td>انتقال دیتا به متلب و نرم‌افزارهای تحلیل داده</td>
            </tr>
        </table>

        <div class="section-title">۹. تأییدیه آزمایشگاهی و بیانیه پدیدآورنده اثر</div>
        <p style="font-size: 10.5pt; margin-top: 3px;">
            بدین‌وسیله تأیید و گواهی می‌گردد که <strong>نمونه‌های اولیه (مدل سیستمی) سامانه «آزمایشگاه مجازی فیزیک»</strong> در ابعاد و مقیاس‌های فیزیکی واقعی ایجاد شده، تمامی زیرسیستم‌های آن به صورت یکپارچه مجتمع گردیده و عملکرد آن در شرایط آزمایشگاه دانشگاه فرهنگیان مورد تأیید کامل قرار گرفته است. تصاویر مندرج در این سند، اسکرین‌شات‌های زنده و مستقیم از اجرای واقعی نرم‌افزارهای کامپایل‌شده می‌باشند.
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
        <span>مستند ۴-۶ تولید نمونه اولیه (مدل سیستمی) — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۳ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

</body>
</html>
"""

    html_path = os.path.join(root_dir, "doc_sysmod_4_6.html")
    pdf_path = os.path.join(root_dir, "4-6  تولید نمونه اولیه (مدل سیستمی).pdf")

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

    print("[INFO] Rendering System Model Prototype PDF using Microsoft Edge...")
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
