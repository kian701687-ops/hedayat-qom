# hedayat-qom
```html
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>پرورشی هدایت قم</title>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Tahoma, Arial, sans-serif;
    background: #f4fff6;
    color: #164b2b;
}

button {
    font-family: inherit;
    cursor: pointer;
}

header {
    background: linear-gradient(135deg, #087f3e, #20b866);
    color: white;
    padding: 18px 20px;
    text-align: center;
}

.logo {
    font-size: 48px;
    margin-bottom: 8px;
}

header h1 {
    font-size: clamp(20px, 4vw, 30px);
    line-height: 1.9;
}

header p {
    margin-top: 5px;
    color: #e7ffed;
    line-height: 2;
}

nav {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    padding: 15px;
    background: white;
    box-shadow: 0 3px 12px #0000000c;
}

nav button {
    border: none;
    border-radius: 12px;
    padding: 11px 17px;
    color: #087f3e;
    background: #e5f9e9;
    font-size: 14px;
    transition: 0.25s;
}

nav button:hover {
    background: #087f3e;
    color: white;
    transform: translateY(-2px);
}

.hero {
    max-width: 1000px;
    margin: 30px auto;
    padding: 30px 20px;
    text-align: center;
}

.book {
    font-size: 75px;
    animation: float 3s ease-in-out infinite;
}

.hero h2 {
    font-size: clamp(22px, 4vw, 32px);
    margin: 20px 0 12px;
    color: #087f3e;
}

.hero p {
    line-height: 2.2;
    color: #557461;
    max-width: 600px;
    margin: auto;
}

.flowers {
    font-size: 26px;
    margin: 20px;
}

.enter {
    background: #087f3e;
    color: white;
    border: none;
    padding: 14px 30px;
    border-radius: 14px;
    font-size: 16px;
    margin-top: 22px;
    transition: 0.3s;
}

.enter:hover {
    background: #20b866;
    transform: scale(1.04);
}

.container {
    max-width: 1050px;
    margin: auto;
    padding: 10px 20px 40px;
}

.section-title {
    text-align: center;
    margin: 20px 0;
    font-size: 24px;
    color: #087f3e;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 18px;
}

.card {
    background: white;
    border: 1px solid #d7efdc;
    border-radius: 20px;
    padding: 25px 18px;
    text-align: center;
    box-shadow: 0 5px 18px #087f3e0b;
    transition: 0.25s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 24px #087f3e18;
}

.card .icon {
    font-size: 42px;
    margin-bottom: 15px;
}

.card h3 {
    color: #087f3e;
    margin-bottom: 10px;
}

.card p {
    color: #6b8071;
    font-size: 14px;
    line-height: 2;
}

.card button {
    background: #e5f9e9;
    border: none;
    color: #087f3e;
    padding: 10px 18px;
    border-radius: 10px;
    margin-top: 15px;
}

.card button:hover {
    background: #087f3e;
    color: white;
}

footer {
    text-align: center;
    background: #087f3e;
    color: white;
    padding: 22px 12px;
    line-height: 2.2;
}

footer span {
    color: #c9f7d5;
}

.page {
    display: none;
    min-height: 60vh;
    padding: 35px 20px;
}

.page.active {
    display: block;
    animation: appear 0.4s ease;
}

.empty-message {
    text-align: center;
    padding: 50px 10px;
    line-height: 2.5;
    color: #63816c;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-9px); }
}

@keyframes appear {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 500px) {
    nav button {
        padding: 10px 12px;
        font-size: 12px;
    }

    .hero {
        margin: 15px auto;
    }
}
</style>
</head>

<body>

<header>
    <div class="logo">📚🌿</div>
    <h1>پرورشی مدرسه راهنمایی پسرانه غیردولتی هدایت قم</h1>
    <p>اینجا جای ایده‌های خوب و خاطرات قشنگه! 🌱</p>
</header>

<nav>
    <button onclick="showPage('home')">🏠 صفحه اصلی</button>
    <button onclick="showPage('programs')">🎯 برنامه‌ها</button>
    <button onclick="showPage('competitions')">🏆 مسابقات</button>
    <button onclick="showPage('news')">📢 اطلاعیه‌ها</button>
    <button onclick="showPage('gallery')">🖼️ گالری</button>
</nav>

<!-- صفحه اصلی -->
<main id="home" class="page active">

    <section class="hero">
        <div class="book">📖</div>
        <div class="flowers">🌿 🌼 🌸 🌼 🌿</div>

        <h2>به دنیای پرورشی هدایت خوش اومدی!</h2>

        <p>
            اینجا قراره از برنامه‌های مدرسه باخبر بشیم،
            توی مسابقات شرکت کنیم و کلی خاطره خوب بسازیم.
        </p>

        <button class="enter" onclick="showPage('programs')">
            بزن بریم! 🚀
        </button>

        <div class="flowers">🌸 🍃 🌼 🍃 🌸</div>
    </section>

    <div class="container">
        <h2 class="section-title">بخش‌های سایت 🌟</h2>

        <div class="cards">

            <div class="card">
                <div class="icon">🎯</div>
                <h3>برنامه‌های مدرسه</h3>
                <p>اردوها و فعالیت‌های پرورشی</p>
                <button onclick="showPage('programs')">مشاهده</button>
            </div>

            <div class="card">
                <div class="icon">🏆</div>
                <h3>مسابقات</h3>
                <p>مسابقات و چالش‌های دانش‌آموزی</p>
                <button onclick="showPage('competitions')">مشاهده</button>
            </div>

            <div class="card">
                <div class="icon">📢</div>
                <h3>اطلاعیه‌ها</h3>
                <p>خبرها و اطلاع‌رسانی‌های مدرسه</p>
                <button onclick="showPage('news')">مشاهده</button>
            </div>

            <div class="card">
                <div class="icon">🖼️</div>
                <h3>گالری تصاویر</h3>
                <p>جای عکس‌های برنامه‌های مدرسه</p>
                <button onclick="showPage('gallery')">مشاهده</button>
            </div>

        </div>
    </div>
</main>

<!-- بخش برنامه‌ها -->
<section id="programs" class="page">
    <h2 class="section-title">🎯 برنامه‌های مدرسه</h2>
    <div class="empty-message">
        <div style="font-size:55px">🌱</div>
        <p>هنوز برنامه‌ای اضافه نشده.</p>
        <p>بعداً برنامه‌های مدرسه رو اینجا قرار می‌دیم!</p>
    </div>
</section>

<!-- بخش مسابقات -->
<section id="competitions" class="page">
    <h2 class="section-title">🏆 مسابقات دانش‌آموزی</h2>
    <div class="empty-message">
        <div style="font-size:55px">🥇</div>
        <p>به‌زودی مسابقات اینجا قرار می‌گیرن!</p>
    </div>
</section>

<!-- بخش اطلاعیه‌ها -->
<section id="news" class="page">
    <h2 class="section-title">📢 اطلاعیه‌های مدرسه</h2>
    <div class="empty-message">
        <div style="font-size:55px">📬</div>
        <p>فعلاً اطلاعیه‌ای ثبت نشده.</p>
    </div>
</section>

<!-- بخش گالری -->
<section id="gallery" class="page">
    <h2 class="section-title">🖼️ گالری تصاویر</h2>
    <div class="empty-message">
        <div style="font-size:55px">📸</div>
        <p>جای عکس‌های مدرسه و اردوها اینجاست.</p>
    </div>
</section>

<footer>
    <p>💚 پرورشی مدرسه راهنمایی پسرانه غیردولتی هدایت قم</p>
    <p><span>با هم، برای روزهای بهتر 🌿</span></p>
</footer>

<script>
function showPage(pageId) {
    const pages = document.querySelectorAll('.page');

    pages.forEach(function(page) {
        page.classList.remove('active');
    });

    const selectedPage = document.getElementById(pageId);

    if (selectedPage) {
        selectedPage.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}
</script>

</body>
</html>
```
