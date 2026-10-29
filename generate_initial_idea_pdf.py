# -*- coding: utf-8 -*-
"""
Script to generate the official Persian PDF document for:
4-9 فناوری در سطح ایده اولیه (Technology Ideation, Conceptual Framework & Feasibility Study Report)
for Virtual Physics Laboratory Suite (آزمایشگاه مجازی فیزیک).
Uses B Titr for headings and B Nazanin for body text with strict vertical pacing.
"""

import os
import subprocess
import base64

def get_base64_png(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    logo_base64 = get_base64_png(os.path.join(root_dir, "assets", "branding", "icon.png"))

    html_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="fa">
<head>
<meta charset="utf-8">
<title>مستند فناوری در سطح ایده اولیه — آزمایشگاه مجازی فیزیک</title>
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

/* Feature & Concept Cards */
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
<!-- PAGE 1: شناسنامه ایده اولیه، خاستگاه مسئله و ضرورت علمی                     -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                کد سند: DOC-IDEA-0409<br>
                تاریخ: پاییز ۱۴۰۵<br>
                مرحله: تدوین ایده اولیه و مدل مفهومی
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">مستند فنی (۴-۹ فناوری در سطح ایده اولیه)</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <table class="info-grid">
            <tr>
                <td class="label">عنوان ایده فناورانه:</td>
                <td class="value"><strong>آزمایشگاه مجازی فیزیک (Virtual Physics Laboratory)</strong></td>
                <td class="label">ایده‌پرداز و توسعه‌دهنده:</td>
                <td class="value"><strong>امیرمحمد یوسف‌وند</strong><br><small style="color:#475569;">دانشجومعلم رشته آموزش علوم تجربی</small></td>
            </tr>
            <tr>
                <td class="label">سطح آمادگی مفهومی:</td>
                <td class="value"><span class="badge badge-success">TRL 1-2 (اصول بنیادین و تدوین مفهوم کاربردی)</span></td>
                <td class="label">پردیس دانشگاهی:</td>
                <td class="value">دانشگاه فرهنگیان پردیس شهید باهنر اراک</td>
            </tr>
            <tr>
                <td class="label">خاستگاه ایده اولیه:</td>
                <td class="value">چالش‌های آموزش تجربی فیزیک و فقدان تجهیزات</td>
                <td class="label">شاخص ارزیابی:</td>
                <td class="value">شاخص ۴-۹ فناوری در سطح ایده اولیه</td>
            </tr>
        </table>

        <div class="section-title">۱. خاستگاه ایده اولیه و جرقه آغازین شکل‌گیری طرح (Genesis of Ideation)</div>
        <p style="margin: 2px 0 4px 0;">
            آموزش فیزیک در سطوح دانشگاهی و مدارس برتر بدون تجربه آزمایشگاهی دست‌اول، ابتر و صرفاً مبتنی بر حفظ روابط ریاضی است. جرقه اولیه این طرح در جریان مشاهده چالش‌های واقعی دانشجویان در آزمایشگاه اپتیک دانشگاه فرهنگیان شکل گرفت: دستگاه‌های گونیومتر اسپکترومتری و تداخل‌سنجی نوری به شدت گران‌قیمت، مستهلک و دارای قطعات مکانیکی آسیب‌پذیر (نظیر توری‌های هولوگرافیک و منشورهای شیشه‌ای حساس به شکستن) هستند. ایده محوری این طرح بر این اصل استوار گردید: <strong>«آیا می‌توان یک محیط رایانه‌ای نرم‌افزاری، مستقل و بدون هزینه ایجاد کرد که رفتار مکانیکی، اپتیکی و آماری این دستگاه‌ها را در ابعاد ۱:۱ با دقت مترولوژی واقعی و محاسبات استاندارد فیزیک بازتولید نماید؟»</strong>
        </p>

        <div class="section-title">۲. مسئله‌شناسی و تحلیل شکاف موجود در فرآیند یاددهی-یادگیری (Problem Analysis)</div>
        <div class="feature-card">
            <h3>تحلیل تطبیقی: محدودیت‌های آزمایشگاه فیزیکی در برابر چشم‌انداز ایده اولیه</h3>
            <ul>
                <li><strong>کمبود شدید تجهیزات تخصصی در مراکز آموزشی:</strong> تهیه یک دستگاه اسپکترومتر گونیومتری و چیدمان لیزری دو شکاف نیازمند بودجه‌های چند ده میلیونی است که امکان تجهیز انفرادی همه کلاس‌ها را سلب می‌کند.</li>
                <li><strong>نامرئی بودن پدیده‌های کوانتومی:</strong> در آزمایش فیزیکی، دانشجو صرفاً الگوی نهایی نوارها را می‌بیند؛ اما مفهوم فروریزش تابع موج و اصابت دانه‌دانه ذرات (فوتون، الکترون، باکی‌بال) در آزمایشگاه فیزیکی قابل مشاهده شهودی نیست.</li>
                <li><strong>خطاهای اندازه‌گیری کنترل‌نشده و استهلاک قطعات:</strong> کثیف شدن شکاف‌ها، سوختن لامپ‌های گاز نادر هلیوم و نئون، و هرز شدن پیچ‌های میکرومتری تلسکوپ مانع از تمرکز دانشجو بر اصول علمی آزمایش می‌شود.</li>
            </ul>
        </div>

        <div class="section-title">۳. مبانی نظری، قوانین علمی حاکم و پیشینه پژوهشی ایده اولیه</div>
        <p style="margin: 2px 0 3px 0; font-size: 10.5pt;">
            ایده اولیه بر پایه چهارچوب نظری محکم از مراجع رسمی فیزیک دانشگاهی فرمول‌بندی شده است:
        </p>
        <ul style="font-size: 10pt;">
            <li><strong>پراش فرانهوفر و تداخل چندشیاری توری:</strong> رابطه توری پراش جوزف فرانهوفر (۱۸۲۱) به صورت <span class="math-formula">d sin(&theta;) = m &lambda;</span> و توزیع شدت نور <span class="math-formula">I(&theta;) = I<sub>0</sub> cos<sup>2</sup>(&beta;) sinc<sup>2</sup>(&alpha;)</span>.</li>
            <li><strong>پاشندگی شیشه و زاویه انحراف منشور:</strong> رابطه تجربی آگوستین کوشی (۱۸۳۶) به فرم <span class="math-formula">n(&lambda;) = A + B / &lambda;<sup>2</sup></span> و فرمول کمینه انحراف منشور متساوی‌الاضلاع.</li>
            <li><strong>امواج ماده و تداخل کوانتومی:</strong> رابطه دوبروی (۱۹۲۴) به صورت <span class="math-formula">&lambda; = h / p</span> و مدل‌سازی تخریب همدوسی کوانتومی منطبق بر آزمایش سال ۱۹۹۹ دانشگاه وین بر روی باکی‌بال‌های <span class="math-formula">C<sub>60</sub></span>.</li>
            <li><strong>داده‌های استاندارد اتمی:</strong> استخراج دقیق خطوط طیف نشری عناصر از داده‌های طیف‌سنجی پایگاه NIST و ثابت‌های CODATA 2018.</li>
        </ul>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۹ فناوری در سطح ایده اولیه — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۱ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 2: معماری مفهومی، ماتریس نیازسنجی و الزامات طراحی                     -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش دوم: ساختار مدل مفهومی<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">معماری نظری، مدل مفهومی و ماتریس الزامات طراحی اولیه</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۴. مدل مفهومی سه‌گانه سامانه در مرحله تدوین ایده (Conceptual Architecture)</div>
        <p style="margin: 2px 0 3px 0; font-size: 10.5pt;">
            در پیش‌نویس اولیه طرح، ساختار سیستم به صورت یک معماری ۳ لایه با تفکیک وظایف زیر تعریف شد:
        </p>
        <ul style="font-size: 10pt;">
            <li><strong>لایه اول — هسته راهبردی و لانچر مجتمع (Launcher Core):</strong> پلتفرم مرکزی برای مدیریت رجیستری داینامیک، ایزولاسیون پردازه‌ها، کنترل فوکوس پنجره‌ها و قابلیت افزودن بی‌نهایت شبیه‌ساز جدید بدون تغییر در کد.</li>
            <li><strong>لایه دوم — شبیه‌ساز تخصصی اسپکترومتر گونیومتری:</strong> مدل‌سازی دایره مدرج ۳۶۰ درجه، ذره‌بین ورنیه‌های دوطرفه با دقت ۱ دقیقه، خطوط طیف اتمی NIST، پاشندگی منشور کوشی و ماژول مسأله معکوس حدس عنصر مجهول.</li>
            <li><strong>لایه سوم — شبیه‌ساز تداخل دو شکاف یانگ و مکانیک کوانتومی:</strong> مدل‌سازی اپتیک موجی، چشمه همدوس <span class="math-formula">S<sub>0</sub></span>، تیغه فاز نوری، نمونه‌برداری آماری مونت‌کارلو برای فوتون/الکترون/باکی‌بال و کلید ناظر کوانتومی Which-Way.</li>
        </ul>

        <div class="section-title">۵. ماتریس نیازسنجی و الزامات طراحی مهندسی ایده اولیه</div>
        <table class="data-table">
            <tr>
                <th style="width: 20%;">بعد نیازمندی</th>
                <th style="width: 40%;">تعریف نیاز آموزشی / فنی در ایده اولیه</th>
                <th style="width: 40%;">راهکار فناورانه طراحی‌شده در مدل مفهومی</th>
            </tr>
            <tr>
                <td><strong>دقت ابزاری</strong></td>
                <td>قرائت زوایا در سطح گونیومترهای واقعی آزمایشگاه</td>
                <td>پیاده‌سازی ورنیه دوبل با تفکیک ۳۰ دقیقه MSR و ۱ دقیقه VSR</td>
            </tr>
            <tr>
                <td><strong>شهود کوانتومی</strong></td>
                <td>تجسم عینی فروریزش تابع موج و رفتار دانه‌دانه ذرات</td>
                <td>موتور نمونه‌برداری معکوس مونت‌کارلو با نرخ ۵۰۰۰ ذره در ۱۰ میلی‌ثانیه</td>
            </tr>
            <tr>
                <td><strong>سهولت استقرار</strong></td>
                <td>اجرا در مدارس با سیستم‌های ضعیف و بدون دسترسی ادمین</td>
                <td>بسته پرتابل تک‌فایلی بدون نیاز به نصب پایتون و ۱۰۰٪ آفلاین</td>
            </tr>
            <tr>
                <td><strong>ارزیابی رسمی</strong></td>
                <td>تولید گزارش کار دانشجویی با فرمول‌های ریاضی معتبر</td>
                <td>ماژول صدور مستقیم گزارش Word با ساختار معادلات استاندارد OMML</td>
            </tr>
            <tr>
                <td><strong>دسترس‌پذیری</strong></td>
                <td>نمایش بدون نقص روی مانیتورها و پروژکتورهای قدیمی</td>
                <td>طراحی ابعاد بهینه ۱۲۰۰x۶۵۰ و انطباق قطعی با رزولوشن‌های 720p و 4:3</td>
            </tr>
        </table>

        <div class="section-title">۶. انطباق ایده با اسناد بالادستی و سرفصل‌های دانشگاه فرهنگیان</div>
        <ul>
            <li><strong>سند تحول بنیادین آموزش و پرورش:</strong> انطباق با هدف عملیاتی شماره ۱۷ (ارتقای کیفیت یادگیری با بهره‌گیری از فناوری‌های نوین و ایجاد محیط‌های یادگیری چندگانه).</li>
            <li><strong>سرفصل دروس دانشگاهی:</strong> پوشش ۱۰۰ درصدی سرفصل دروس «آزمایشگاه فیزیک پایه ۳»، «اپتیک موجی» و «فیزیک جدید» رشته آموزش علوم تجربی و فیزیک دانشگاه فرهنگیان.</li>
        </ul>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۹ فناوری در سطح ایده اولیه — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۲ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

<!-- ======================================================================= -->
<!-- PAGE 3: امکان‌سنجی، نقشه راه تکامل و بیانیه تأیید ایده                      -->
<!-- ======================================================================= -->
<div class="page">
    <div class="page-body">
        <div class="official-header">
            <div class="header-meta">
                بخش سوم: امکان‌سنجی و نقشه راه<br>
                تاریخ: پاییز ۱۴۰۵
            </div>
            <div class="header-titles">
                <div class="ministry">دانشگاه فرهنگیان — پردیس شهید باهنر اراک</div>
                <div class="doc-title">امکان‌سنجی فنی-اقتصادی، نقشه راه تکامل ایده و تأییدیه</div>
            </div>
            <div>
                {"<img src='" + logo_base64 + "' class='header-logo'>" if logo_base64 else ""}
            </div>
        </div>

        <div class="section-title">۷. ارزیابی امکان‌سنجی سه‌گانه ایده اولیه (Feasibility Study)</div>
        <p style="margin: 2px 0 3px 0;">
            پیش از آغاز کدنویسی، امکان‌سنجی طرح در سه بعد اصلی مورد بررسی دقیق قرار گرفت:
        </p>
        <ul style="font-size: 10pt;">
            <li><strong>امکان‌سنجی الگوریتمی و ریاضی:</strong> بررسی توانایی پردازنده‌های استاندارد در محاسبه پیوسته توابع مثلثاتی و انتگرال پراش در ۶۰ فریم بر ثانیه؛ با به‌کارگیری محاسبات برداری NumPy امکان‌پذیری با موفقیت تأیید شد.</li>
            <li><strong>امکان‌سنجی نرم‌افزاری و گرافیکی:</strong> امکان ایجاد بوم‌های رسم پویا و پنجره‌های تعاملی در زبان پایتون با فریمورک مدرن CustomTkinter بررسی و انتخاب گردید.</li>
            <li><strong>امکان‌سنجی اقتصادی و عملیاتی:</strong> ارزیابی ارزش اقتصادی جایگزینی نرم‌افزار با تجهیزات آزمایشگاهی فیزیکی که نشان‌دهنده صرفه‌جویی ۱۰۰ درصدی در هزینه‌های خرید، تعمیر و استهلاک قطعات بود.</li>
        </ul>

        <div class="section-title">۸. نقشه راه تکامل ایده اولیه تا محصول نهایی (Ideation to Deployment Roadmap)</div>
        <table class="data-table">
            <tr>
                <th style="width: 18%;">فاز تکامل</th>
                <th style="width: 25%;">اقدام کلیدی</th>
                <th style="width: 37%;">خروجی حاصل در نقشه راه</th>
                <th style="width: 20%;">سطح بلوغ</th>
            </tr>
            <tr>
                <td>فاز ۱ (ایده و فرمول)</td>
                <td>تدوین ایده و مدل ریاضی</td>
                <td>استخراج روابط تداخل فرانهوفر و کوشی در متلب/پایتون</td>
                <td><span class="badge">TRL 1-2 (ایده)</span></td>
            </tr>
            <tr>
                <td>فاز ۲ (اثبات مفهوم)</td>
                <td>پیاده‌سازی هسته عددی</td>
                <td>اسکریپت محاسباتی تحلیلی و شبیه‌سازی مونت‌کارلو</td>
                <td><span class="badge">TRL 3-4 (آزمایشگاه)</span></td>
            </tr>
            <tr>
                <td>فاز ۳ (توسعه مدل)</td>
                <td>طراحی واسط کاربر و ورنیه</td>
                <td>توسعه GUI تعاملی، رتیکل متقاطع و ورنیه دوطرفه</td>
                <td><span class="badge">TRL 5-6 (پروتوتایپ)</span></td>
            </tr>
            <tr>
                <td>فاز ۴ (محصول کامل)</td>
                <td>پکیج نهایی و استقرار</td>
                <td>لانچر مجتمع، بسته پرتابل مستقل، انتشار ریلیز گیت‌هاب</td>
                <td><span class="badge badge-success">TRL 8-9 (استقرار)</span></td>
            </tr>
        </table>

        <div class="section-title">۹. بیانیه اصالت، تعهد علمی و تأییدیه تدوین ایده اولیه</div>
        <p style="font-size: 10.5pt; margin-top: 3px;">
            بدین‌وسیله رسماً تأیید می‌گردد که <strong>ایده اولیه، مبانی نظری، صورت‌بندی مسئله، مدل مفهومی و نقشه راه تکامل سامانه «آزمایشگاه مجازی فیزیک»</strong> توسط <strong>امیرمحمد یوسف‌وند</strong> (دانشجومعلم رشته آموزش علوم تجربی در <strong>دانشگاه فرهنگیان پردیس شهید باهنر اراک</strong>) با هدف تحول در آموزش علوم پایه و رفع تنگناهای تجهیزات آزمایشگاهی تدوین شده و به عنوان خاستگاه بنیادین این دستاورد فناورانه گواهی می‌گردد.
        </p>

        <div style="margin-top: 15px; text-align: center;">
            <div style="display: inline-block; border-top: 1px solid #94a3b8; padding-top: 6px; width: 300px;">
                <div style="font-family: 'BTitr', sans-serif; color: #0f172a; font-size: 11pt; margin-bottom: 2px;">ایده‌پرداز و توسعه‌دهنده طرح</div>
                <div style="font-size: 12pt; font-weight: bold; color: #0284c7;">امیرمحمد یوسف‌وند</div>
                <div style="font-size: 9.5pt; color: #475569; margin-top: 2px;">دانشجومعلم رشته آموزش علوم تجربی</div>
                <div style="font-size: 9pt; color: #64748b;">دانشگاه فرهنگیان — پردیس شهید باهنر اراک (پاییز ۱۴۰۵)</div>
            </div>
        </div>
    </div>

    <div class="footer-stamp">
        <span>مستند ۴-۹ فناوری در سطح ایده اولیه — سامانه آزمایشگاه مجازی فیزیک</span>
        <span>صفحه ۳ از ۳</span>
        <span>پردیس شهید باهنر اراک</span>
    </div>
</div>

</body>
</html>
"""

    html_path = os.path.join(root_dir, "doc_idea_4_9.html")
    pdf_path = os.path.join(root_dir, "4-9 فناوری در سطح ایده اولیه.pdf")

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

    print("[INFO] Rendering Initial Idea PDF using Microsoft Edge...")
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
