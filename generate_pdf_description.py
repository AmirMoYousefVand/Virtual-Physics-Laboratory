# -*- coding: utf-8 -*-
"""
Script to generate the official 3-page Persian PDF description of achievements
and technical specifications for the Virtual Physics Laboratory Suite.
Uses B Titr for headings and B Nazanin for body text.
Updated based on user feedback.
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
<title>شرح اثر و دستاوردهای علمی-فناورانه آزمایشگاه مجازی فیزیک</title>
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
    margin: 12mm 15mm 15mm 15mm;
    @bottom-center {{
        content: counter(page);
    }}
}}

*, *:before, *:after {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}

body {{
    font-family: 'BNazanin', 'B Nazanin', 'Vazirmatn', Tahoma, sans-serif;
    font-size: 12pt;
    line-height: 1.6;
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
    margin-bottom: 6px;
    font-weight: bold;
}}

.page {{
    page-break-after: always;
    height: 270mm;
    max-height: 270mm;
    position: relative;
    overflow: hidden;
    padding-bottom: 10px;
}}
.page:last-child {{
    page-break-after: avoid;
}}

/* Header Banner */
.official-header {{
    border-bottom: 2px solid #0284c7;
    padding-bottom: 8px;
    margin-bottom: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}
.header-titles {{
    flex: 1;
    text-align: center;
}}
.header-titles .ministry {{
    font-size: 14pt;
    font-family: 'BTitr', sans-serif;
    color: #0f172a;
    margin-bottom: 4px;
}}
.header-titles .doc-title {{
    font-size: 14.5pt;
    font-family: 'BTitr', sans-serif;
    color: #0284c7;
}}
.header-logo {{
    width: 65px;
    height: 65px;
    object-fit: contain;
}}
.header-meta {{
    font-size: 10pt;
    color: #475569;
    text-align: left;
    direction: ltr;
    line-height: 1.4;
}}

/* Section Titles */
.section-title {{
    font-size: 13pt;
    background-color: #f1f5f9;
    border-right: 4px solid #0284c7;
    padding: 4px 12px;
    margin-top: 12px;
    margin-bottom: 8px;
    border-radius: 2px;
}}

/* Identity Table */
.info-grid {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 12px;
    font-size: 11pt;
}}
.info-grid td {{
    border: 1px solid #cbd5e1;
    padding: 5px 10px;
}}
.info-grid .label {{
    background-color: #f8fafc;
    font-family: 'BTitr', sans-serif;
    color: #334155;
    width: 20%;
    font-size: 10.5pt;
}}
.info-grid .value {{
    color: #0f172a;
    width: 30%;
}}

/* Cards and Callouts */
.feature-card {{
    border: 1px solid #e2e8f0;
    background-color: #f8fafc;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 10px;
}}
.feature-card h3 {{
    font-size: 12pt;
    color: #0369a1;
    margin-bottom: 4px;
}}

/* Technical Specs Table */
.spec-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
    margin-bottom: 10px;
    font-size: 10.5pt;
}}
.spec-table th {{
    background-color: #0f172a;
    color: #ffffff;
    font-family: 'BTitr', sans-serif;
    padding: 6px 10px;
    text-align: center;
    border: 1px solid #0f172a;
}}
.spec-table td {{
    border: 1px solid #cbd5e1;
    padding: 5px 10px;
    text-align: right;
}}
.spec-table tr:nth-child(even) {{
    background-color: #f8fafc;
}}

ul {{
    margin: 4px 0 8px 0;
    padding-right: 22px;
}}
li {{
    margin-bottom: 4px;
}}

.math-formula {{
    direction: ltr;
    display: inline-block;
    font-family: 'Space Grotesk', 'Consolas', 'Segoe UI', sans-serif;
    font-size: 10.5pt;
    color: #0369a1;
    font-weight: bold;
    padding: 0 4px;
}}

.footer-stamp {{
    position: absolute;
    bottom: 5px;
    left: 0;
    right: 0;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid #cbd5e1;
    padding-top: 6px;
    font-size: 9.5pt;
    color: #64748b;
}}

.badge {{
    display: inline-block;
    padding: 2px 7px;
    font-size: 9.5pt;
    background-color: #e0f2fe;
    color: #0369a1;
    border-radius: 4px;
    font-weight: bold;
}}
</style>
</head>
<body>

<!-- ======================================================================= -->
<!-- PAGE 1: شناسنامه اثر و مبانی توسعه و نوآوری معماری                       -->
<!-- ======================================================================= -->
<div class="page">
    <div class="official-header">
        <div class="header-meta">
            تاریخ: پاییز ۱۴۰۵<br>
            پیوست: شناسنامه اثر<br>
            نسخه: v1.0.0
        </div>
        <div class="header-titles">
            <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
            <div class="doc-title">شناسنامه علمی، شرح نوآوری و دستاوردهای اثر</div>
        </div>
        <div>
            {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
        </div>
    </div>

    <table class="info-grid">
        <tr>
            <td class="label">عنوان رسمی اثر:</td>
            <td class="value"><strong>آزمایشگاه مجازی فیزیک (Virtual Physics Laboratory)</strong></td>
            <td class="label">توسعه‌دهنده:</td>
            <td class="value"><strong>امیرمحمد یوسف‌وند</strong><br><small style="color: #475569;">دانشجومعلم رشته آموزش علوم تجربی</small></td>
        </tr>
        <tr>
            <td class="label">پردیس دانشگاهی:</td>
            <td class="value">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</td>
            <td class="label">دامنه کاربرد:</td>
            <td class="value">آموزش فیزیک دانشگاهی، فوتونیک و مدارس برتر</td>
        </tr>
        <tr>
            <td class="label">نوع محصول:</td>
            <td class="value">نرم‌افزار رایانه‌ای پرتابل بدون وابستگی</td>
            <td class="label">مخزن رسمی سورس:</td>
            <td class="value" style="direction: ltr; text-align: left; font-family: sans-serif; font-size: 8.5pt;">github.com/AmirMoYousefVand</td>
        </tr>
    </table>

    <div class="section-title">۱. بیان مسئله، مقدمه و ضرورت راهبردی طرح</div>
    <p>
        آموزش تجربی و آزمایشگاهی مباحث پیشرفته فیزیک در شاخه‌های اپتیک موجی، اسپکتروسکوپی و پدیده‌های نوین کوانتومی، همواره با چالش‌های ساختاری روبروست. دستگاه‌های گونیومتر اپتیکی، توری‌های پراش هولوگرافیک، منشورهای تحلیلی، لامپ‌های گسیل طیفی عناصر و چیدمان‌های آزمایشگاهی ثبت تک‌فوتون بسیار گران‌قیمت، حساس به ضربه و دارای استهلاک شدید هستند. در اکثریت مدارس و حتی پردیس‌های دانشگاه فرهنگیان و مراکز دانشگاهی، دسترسی همزمان و فردی تمامی دانشجویان به این ابزارها امکان‌پذیر نیست. علاوه بر این، درک پدیده‌هایی نظیر فروریزش تابع موج در آزمایش دو شکاف، رفتار آماری مونت‌کارلو در اصابت ذرات، و محاسبه کمینه انحراف و پاشندگی منشور، نیازمند ابزاری تجسم‌بخش، تعاملی و با دقت محاسباتی ریاضی-فیزیکی استاندارد است. پروژه «آزمایشگاه مجازی فیزیک» با هدف ایجاد یک زیرساخت یکپارچه، مستقل و قابل‌حمل پدید آمده تا عدالت آموزشی را در بالاترین سطح کیفی محقق سازد.
    </p>

    <div class="section-title">۲. معماری مهندسی و نوآوری‌های فنی لانچر مرکزی</div>
    <div class="feature-card">
        <h3>معماری مدولار، ایزولاسیون پردازه‌ها و توسعه‌پذیری پویا (Extensibility)</h3>
        <p>
            سامانه لانچر مرکزی بر پایه معماری ماژولار و مبتنی بر پیکربندی (Config-Driven Architecture) طراحی گردیده است:
        </p>
        <ul>
            <li><strong>مدیریت پردازش مستقل (Process Isolation):</strong> اجرای شبیه‌سازها در پوشه کاری (CWD) مجزا با استفاده از مکانیزم مستقل فرآیندی و تخصیص PID مجزا، که مانع از تداخل بارگذاری دارایی‌ها و داده‌ها می‌گردد.</li>
            <li><strong>جلوگیری از اجرای تکراری و فوکوس هوشمند (Bring-to-Front):</strong> پیاده‌سازی سرویس تعامل با Win32 API و فراخوانی توابع <code>SwitchToThisWindow</code> و <code>AttachThreadInput</code> جهت ممانعت از اسپم پنجره‌های تکراری و هدایت فوکوس ویندوز مستقیماً به شبیه‌ساز فعال.</li>
            <li><strong>قابلیت گسترش آنی بدون کامپایل:</strong> امکان ثبت و افزودن هر نوع شبیه‌ساز فیزیک دیگر (فایل‌های EXE یا اسکریپت پایتون) از طریق دیتابیس ساخت‌یافته <code>simulators.json</code> یا دیالوگ گرافیکی پیشرفته تعبیه‌شده در نرم‌افزار.</li>
        </ul>
    </div>

    <div class="footer-stamp">
        <span>سامانه آزمایشگاه مجازی فیزیک — دانشگاه فرهنگیان</span>
        <span>صفحه ۱ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 2: شرح فنی شبیه‌سازهای تخصصی و جدول مشخصات                           -->
<!-- ======================================================================= -->
<div class="page">
    <div class="official-header">
        <div class="header-meta">
            بخش دوم: مشخصات تخصصی<br>
            تاریخ: پاییز ۱۴۰۵
        </div>
        <div class="header-titles">
            <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
            <div class="doc-title">شرح تفصیلی شبیه‌سازهای تخصصی مجتمع در سامانه</div>
        </div>
        <div>
            {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
        </div>
    </div>

    <div class="section-title">۳. شبیه‌ساز اسپکترومتر اپتیکی و توری پراش (Optical Spectrometer)</div>
    <p>
        این شبیه‌ساز، مدل‌سازی جامع و فوق‌دقیق گونیومتر اسپکترومتری آزمایشگاهی است که امکان اندازه‌گیری تجربی طول‌موج‌های نور مرئی و پارامترهای پاشندگی را فراهم می‌آورد:
    </p>
    <ul>
        <li><strong>مکانیک دقیق ورنیه‌های دوطرفه:</strong> دایره مدرج ۳۶۰ درجه اصلی با گام‌های ۳۰ دقیقه قوسی (۰٫۵ درجه) همراه با دو ورنیه مستقل ۱ و ۲ با دقت خوانش ۱ دقیقه قوسی (معادل یک شصتم درجه) و مکانیزم تصحیح خطای خروج از مرکز محور دوران.</li>
        <li><strong>طیف‌های واقعی لامپ‌های تخلیه گازی:</strong> شبیه‌سازی طول‌موج‌های دقیق طیفی بر اساس استانداردهای NIST برای عناصر جیوه (Hg)، سدیم (خطوط دوگانه ۵۸۹٫۰ و ۵۸۹٫۶ نانومتر)، هیدروژن بالمر، هلیوم، نئون، نور سفید پیوسته و توری‌های پراش ۳۰۰، ۶۰۰ و ۱۲۰۰ شیار بر میلی‌متر.</li>
        <li><strong>مدل‌سازی پاشندگی منشور شیشه‌ای کوشی:</strong> محاسبه زاویه کمینه انحراف <span class="math-formula">D<sub>min</sub></span>، توان پاشندگی و ضریب شکست منشور متساوی‌الاضلاع (زاویه رأس ۶۰ درجه) بر پایه رابطه تجربی پاشندگی کوشی <span class="math-formula">n(&lambda;) = A + B / &lambda;<sup>2</sup></span>.</li>
        <li><strong>خطاهای سیستماتیک آزمایشگاهی:</strong> تاری کانونی و تابع گسترش نقطه (Defocus PSF)، انحراف تراز شوستر و محاسبه تجربی ثابت ریدبرگ (<span class="math-formula">R<sub>H</sub></span>) با خطای کمتر از ۰٫۰۳ درصد.</li>
    </ul>

    <div class="section-title">۴. شبیه‌ساز آزمایش دو شکاف تامس یانگ (Thomas Young Double-Slit)</div>
    <p>
        این ماژول، پدیده بنیادین تداخل و پراش نور را از دو جنبه کلاسیک موجی و مکانیک کوانتومی مدرن شبیه‌سازی می‌کند:
    </p>
    <ul>
        <li><strong>اپتیک موجی کلاسیک فرانهوفر:</strong> فرمول‌بندی تحلیلی کامل شدت نور حاصل از تداخل دو شکاف با پوش پراش فرانهوفر به صورت <span class="math-formula">I(&theta;) = I<sub>0</sub> cos<sup>2</sup>(&beta;) sinc<sup>2</sup>(&alpha;)</span>، چشمه همدوس اولیه تک‌شکاف (<span class="math-formula">S<sub>0</sub></span>) و اعمال تیغه شفاف نوری با ضریب شکست <span class="math-formula">n<sub>slab</sub></span> و ضخامت <span class="math-formula">t</span> با محاسبه زنده جابه‌جایی فریزها.</li>
        <li><strong>مکانیک کوانتومی و تجمع تک‌ذره (Monte Carlo Buildup):</strong> شبیه‌سازی شلیک و برخورد دانه‌دانه ذرات (فوتون، الکترون، و مولکول‌های باکی‌بال C<sub>60</sub>) با طول‌موج دوبروی واقعی و شبیه‌سازی آشکارساز ناظر (Which-Way) و نمایش عینی پدیده فروریزش تابع موج.</li>
    </ul>

    <div class="section-title">۵. ماتریس ویژگی‌های فنی و استانداردهای توسعه نرم‌افزار</div>
    <table class="spec-table">
        <tr>
            <th style="width: 28%;">شاخص فنی</th>
            <th style="width: 37%;">پیاده‌سازی در آزمایشگاه مجازی</th>
            <th style="width: 35%;">استاندارد / مرجع علمی</th>
        </tr>
        <tr>
            <td>زبان و کتابخانه‌های محاسباتی</td>
            <td>Python 3.11, NumPy, SciPy (وکتورایز شده)</td>
            <td>موتور عددی علمی استاندارد</td>
        </tr>
        <tr>
            <td>محیط گرافیکی و رابط کاربر</td>
            <td>CustomTkinter مدرن تیتانیومی با تم تاریک یکپارچه</td>
            <td>طراحی ارگونومیک، بدون ایموجی ناپایدار</td>
        </tr>
        <tr>
            <td>خروجی‌های آزمایشگاهی</td>
            <td>Word با فرمول‌های نیتیو OMML، CSV، مدل سه‌بعدی OBJ</td>
            <td>گزارش رسمی مطابق آیین‌نگارش علمی</td>
        </tr>
        <tr>
            <td>استقلال اجرایی (Portability)</td>
            <td>کامپایل با PyInstaller به صورت فایل پرتابل ویندوز</td>
            <td>عدم نیاز به نصب پایتون در رایانه مقصد</td>
        </tr>
    </table>

    <div class="footer-stamp">
        <span>سامانه آزمایشگاه مجازی فیزیک — دانشگاه فرهنگیان</span>
        <span>صفحه ۲ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 3: دستاوردها، اعتبارسنجی و بیانیه اصالت اثر                            -->
<!-- ======================================================================= -->
<div class="page">
    <div class="official-header">
        <div class="header-meta">
            بخش سوم: دستاوردها و اعتبارسنجی<br>
            تاریخ: پاییز ۱۴۰۵
        </div>
        <div class="header-titles">
            <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
            <div class="doc-title">دستاوردهای علمی، آموزشی، نتایج آزمون‌ها و اصالت اثر</div>
        </div>
        <div>
            {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
        </div>
    </div>

    <div class="section-title">۶. دستاوردهای علمی، آموزشی و تربیتی اثر</div>
    <ul>
        <li><strong>تعمیق یادگیری مفهومی در آموزش فیزیک:</strong> تبدیل مفاهیم انتزاعی نظیر دوگانگی موج-ذره، ناهمدوسی، طیف‌سنجی اتمی و محاسبه ضریب شکست به تجربه‌ای دیداری و تعاملی برای دانشجومعلمان و دانش‌آموزان.</li>
        <li><strong>صرفه‌جویی چشمگیر اقتصادی و عدالت آموزشی:</strong> فراهم‌سازی کارگاهی معادل تجهیزات آزمایشگاهی فیزیک به ارزش صدها میلیون تومان، بدون کوچک‌ترین خطر شکستگی منشور یا سوختن لیزر و لامپ‌های گازی.</li>
        <li><strong>تولید گزارش‌های استاندارد دانشگاهی:</strong> نخستین نرم‌افزار آموزشی فارسی که معادلات ریاضی گزارش کار را با ساختار استاندارد مایکروسافت آفیس (OMML) تولید و خروجی باکیفیت ارائه می‌دهد.</li>
        <li><strong>ترویج دسترسی آزاد به علم (Open Science):</strong> انتشار کامل مستندات، کدهای سورس و بسته‌های نصبی در گیت‌هاب با مجوز متن‌باز جهت بهره‌برداری آزاد اساتید، معلمان و پژوهشگران کشور.</li>
    </ul>

    <div class="section-title">۷. نتایج آزمون‌های صحه‌گذاری و اعتبارسنجی فیزیکی (Verification)</div>
    <div class="feature-card">
        <p style="margin-bottom: 4px;">
            کلیه توابع محاسباتی، معادلات فیزیکی و رفتارهای گرافیکی نرم‌افزار تحت آزمون‌های خودکار جامع (Unit & Integration Tests) سنجیده شده‌اند:
        </p>
        <ul>
            <li><strong>مجموعه تست شبیه‌ساز اسپکترومتر:</strong> شامل ۱۲ سوئیت آزمون اعتبارسنجی زاویه‌ای فرانهوفر، تفکیک سدیم با معیار ریلی، برازش ریدبرگ، انطباق ورنیه و پاشندگی کوشی — <span class="badge">۱۰۰٪ موفقیت (Pass)</span></li>
            <li><strong>مجموعه تست شبیه‌ساز دو شکاف یانگ:</strong> شامل ۳۸ آزمون جامع اپتیک، نمونه‌برداری مونت‌کارلو، تیغه شفاف، اثر ناظر و تبدیل فرمت‌ها — <span class="badge">۱۰۰٪ موفقیت (Pass)</span></li>
            <li><strong>آزمون چرخه حیات لانچر:</strong> اعتبارسنجی اجرای مستقل، فوکوس پنجره، سلامت بسته‌بندی و پایداری عملکرد در سیستم‌عامل ویندوز.</li>
        </ul>
    </div>

    <div class="section-title">۸. بیانیه اصالت و تعهد علمی</div>
    <p style="font-size: 11pt;">
        بدین‌وسیله تأیید می‌گردد کلیه الگوریتم‌های شبیه‌سازی فیزیکی، معماری نرم‌افزاری لانچر، کدهای رابط کاربری، استخراج گزارش‌ها و توسعه این بسته توسط <strong>امیرمحمد یوسف‌وند</strong> (دانشجومعلم رشته آموزش علوم تجربی در <strong>دانشگاه فرهنگیان پردیس شهید باهنر اراک</strong>) با استناد به مبانی معتبر فیزیک دانشگاهی طراحی، پیاده‌سازی و راستی‌آزمایی شده است و اثر فاقد هرگونه نمونه‌برداری غیرمجاز می‌باشد.
    </p>

    <div style="margin-top: 35px; text-align: center;">
        <div style="display: inline-block; border-top: 1px solid #94a3b8; padding-top: 8px; width: 260px;">
            <div style="font-family: 'BTitr', sans-serif; color: #0f172a; font-size: 11pt; margin-bottom: 4px;">پژوهشگر و توسعه‌دهنده اثر</div>
            <div style="font-size: 12pt; font-weight: bold; color: #0284c7;">امیرمحمد یوسف‌وند</div>
            <div style="font-size: 10pt; color: #475569; margin-top: 4px;">دانشجومعلم رشته آموزش علوم تجربی</div>
            <div style="font-size: 9.5pt; color: #64748b;">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
        </div>
    </div>

    <div class="footer-stamp">
        <span>سامانه آزمایشگاه مجازی فیزیک — دانشگاه فرهنگیان</span>
        <span>صفحه ۳ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

</body>
</html>
"""

    html_path = os.path.join(root_dir, "doc_description.html")
    pdf_path = os.path.join(root_dir, "توضیح_اثر_و_دستاوردها_آزمایشگاه_مجازی_فیزیک.pdf")

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

    print("[INFO] Rendering PDF using Microsoft Edge...")
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
