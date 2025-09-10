<!DOCTYPE html>
<html lang="fa">
<head>
  <meta charset="UTF-8">
  <title>درباره ما | ایده‌پرداز خلاق</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <header>
    <h1>درباره ما</h1>
    <p>با ما بیشتر آشنا شوید</p>
  </header>

  <nav>
    <a href="index.html">خانه</a>
    <a href="about.html">درباره ما</a>
    <a href="#">پروژه‌ها</a>
    <a href="#">تماس با ما</a>
  </nav>

  <section class="welcome">
    <h2>ایده‌پرداز خلاق کیست؟</h2>
    <p>
      ما یک تیم کوچک و پرانرژی هستیم که با عشق به طراحی، برنامه‌نویسی و آموزش، پروژه‌های خلاقانه تولید می‌کنیم.
      هدف ما ساخت محتوای آموزشی، طراحی سایت‌های شخصی و توسعه اپلیکیشن‌هایی با محوریت هوش مصنوعی است.
    </p>
  </section>

  <section class="projects">
    <h2>تخصص‌های ما</h2>
    <ul>
      <li>طراحی گرافیکی و انیمیشن آموزشی</li>
      <li>برنامه‌نویسی با Python و Flask</li>
      <li>ساخت سایت‌های HTML/CSS</li>
      <li>راه‌اندازی چت‌بات و سیستم‌های هوشمند</li>
    </ul>
  </section>

  <footer>
    <p>© 2025 ایده‌پرداز خلاق | طراحی توسط Hojat</p>
  </footer>

</body>
</html>
body {
  font-family: "Tahoma", sans-serif;
  direction: rtl;
  background-color: #f9f9f9;
  margin: 0;
  padding: 0;
}

header {
  background-color: #4caf50;
  color: white;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  height: 50px;
}

nav ul {
  list-style: none;
  display: flex;
  gap: 15px;
}

nav a {
  color: white;
  text-decoration: none;
}

main {
  padding: 20px;
}

footer {
  background-color: #eee;
  text-align: center;
  padding: 10px;
  margin-top: 20px;
}
<!DOCTYPE html>
<html lang="fa">
<head>
  <meta charset="UTF-8">
  <title>درباره ما | ایده‌پرداز خلاق</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <img src="images/logo.png" alt="لوگو" class="logo">
    <nav>
      <ul>
        <li><a href="index.html">صفحه اصلی</a></li>
        <li><a href="about.html">درباره ما</a></li>
        <li><a href="contact.html">تماس با ما</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <h1>درباره ایده‌پرداز خلاق</h1>
    <p>ما یک تیم کوچک و پرانرژی هستیم که با هدف تولید محتوای آموزشی خلاقانه برای کودکان و نوجوانان فعالیت می‌کنیم. تخصص ما ترکیب داستان‌سرایی، انیمیشن، و فناوری‌های نوین مثل هوش مصنوعی است.</p>
  </main>

  <footer>
    <p>© 2025 ایده‌پرداز خلاق</p>
  </footer>
</body>
</html>
<!DOCTYPE html>
<html lang="fa">
<head>
  <meta charset="UTF-8">
  <title>تماس با ما | ایده‌پرداز خلاق</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <img src="images/logo.png" alt="لوگو" class="logo">
    <nav>
      <ul>
        <li><a href="index.html">صفحه اصلی</a></li>
        <li><a href="about.html">درباره ما</a></li>
        <li><a href="contact.html">تماس با ما</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <h1>تماس با ما</h1>
    <p>برای ارتباط با ما می‌توانید از طریق فرم زیر یا ایمیل اقدام کنید:</p>

    <form>
      <label for="name">نام:</label><br>
      <input type="text" id="name" name="name"><br><br>

      <label for="email">ایمیل:</label><br>
      <input type="email" id="email" name="email"><br><br>

      <label for="message">پیام:</label><br>
      <textarea id="message" name="message" rows="5"></textarea><br><br>

      <button type="submit">ارسال پیام</button>
    </form>
  </main>

  <footer>
    <p>© 2025 ایده‌پرداز خلاق</p>
  </footer>
</body>
</html>
@media (max-width: 768px) {
  header {
    flex-direction: column;
    align-items: flex-start;
  }

  nav ul {
    flex-direction: column;
    gap: 10px;
    padding: 0;
  }

  .logo {
    margin-bottom: 10px;
  }

  main {
    padding: 10px;
  }
}
idepardaz-khalagh/
├── fonts/
│   └── vazir.woff2
@font-face {
  font-family: 'Vazir';
  src: url('../fonts/vazir.woff2') format('woff2');
}

body {
  font-family: 'Vazir', Tahoma, sans-serif;
}
<main>
  <section class="hero">
    <img src="images/baby-laptop.jpg" alt="کودک در حال یادگیری" class="hero-img">
    <div class="hero-text">
      <h1>به سایت ایده‌پرداز خلاق خوش آمدید</h1>
      <p>ما در زمینه تولید محتوای آموزشی و طراحی خلاقانه فعالیت می‌کنیم.</p>
    </div>
  </section>
</main>
.hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 20px;
  flex-wrap: wrap;
}

.hero-img {
  max-width: 300px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.hero-text {
  max-width: 600px;
}

@media (max-width: 768px) {
  .hero {
    flex-direction: column;
    text-align: center;
  }

  .hero-img {
    max-width: 100%;
  }
}
<a href="contact.html" class="btn">تماس با ما</a>
.btn {
  display: inline-block;
  background-color: #4caf50;
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.btn:hover {
  background-color: #388e3c;
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0,0,0,0.2);
}
<a href="contact.html" class="btn ripple">
  <span class="btn-icon">📩</span>
  <span class="btn-text">تماس با ما</span>
</a>
.btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background-color: #4caf50;
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
  overflow: hidden;
  transition: background-color 0.3s ease, transform 0.3s ease;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.btn:hover {
  background-color: #388e3c;
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0,0,0,0.2);
}

.btn-icon {
  font-size: 1.2em;
}

.btn-text::after {
  content: " 👋";
  opacity: 0;
  transition: opacity 0.3s ease;
}

.btn:hover .btn-text::after {
  opacity: 1;
}

/* افکت موجی */
.ripple::before {
  content: "";
  position: absolute;
  background: rgba(255, 255, 255, 0.4);
  border-radius: 50%;
  transform: scale(0);
  animation: ripple 0.6s linear;
  pointer-events: none;
}

@keyframes ripple {
  to {
    transform: scale(4);
    opacity: 0;
  }
}

.ripple:active::before {
  top: 50%;
  left: 50%;
  width: 100px;
  height: 100px;
  margin-left: -50px;
  margin-top: -50px;
}
.hero-img {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 1s ease forwards;
  animation-delay: 0.3s;
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"پیام جدید از {name} ({email}): {message}")
        return "پیام شما دریافت شد. ممنون!"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>idepardaz-khalagh/
├── index.html
├── style.css
└── images/
    ├── project1.jpg
    └── project2.jpg
