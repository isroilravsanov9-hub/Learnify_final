"""
Learnify - Yakuniy Test Savollari Banki (30 ta savoldan iborat)
Yo'nalishlar bo'yicha 30 talik test savollari to'plami.
"""

FINAL_TEST_QUESTIONS = {
    'python-backend': [
        {
            "id": 1,
            "question": "Python dasturlash tilida o'zgarmas (immutable) ma'lumot turlariga qaysilar kiradi?",
            "options": ["list, dict, set", "int, float, str, tuple", "list, tuple, str", "dict, set, tuple"],
            "correct": 1
        },
        {
            "id": 2,
            "question": "Django arxitekturasi qaysi naqsh (pattern) asosida ishlaydi?",
            "options": ["MVC (Model-View-Controller)", "MVT (Model-View-Template)", "MVVM (Model-View-ViewModel)", "Flux"],
            "correct": 1
        },
        {
            "id": 3,
            "question": "Python-da ro'yxatning oxiriga yangi element qo'shish uchun qaysi metod ishlatiladi?",
            "options": ["add()", "push()", "append()", "insert()"],
            "correct": 2
        },
        {
            "id": 4,
            "question": "Django-da ma'lumotlar bazasi jadvallarini Python kodida yaratish uchun qaysi moduldan foydalaniladi?",
            "options": ["django.views", "django.urls", "django.db.models", "django.shortcuts"],
            "correct": 2
        },
        {
            "id": 5,
            "question": "Python funksiyasida cheksiz miqdordagi pozitsion argumentlarni qabul qilish qanday yoziladi?",
            "options": ["*args", "**kwargs", "&args", "$args"],
            "correct": 0
        },
        {
            "id": 6,
            "question": "Django-da yangi migratsiya fayllarini yaratish buyrug'i qaysi?",
            "options": ["python manage.py migrate", "python manage.py makemigrations", "python manage.py create_db", "python manage.py sqlmigrate"],
            "correct": 1
        },
        {
            "id": 7,
            "question": "RESTful API arxitekturasida ma'lumotlarni o'zgartirish (yangilash) uchun qaysi HTTP metod ishlatiladi?",
            "options": ["GET", "POST", "PUT / PATCH", "DELETE"],
            "correct": 2
        },
        {
            "id": 8,
            "question": "Python-da lug'atdan (dict) kalit bo'yicha qiymat olish va agar kalit bo'lmasa xato bermaslik usuli qaysi?",
            "options": ["dict[key]", "dict.get(key, default)", "dict.find(key)", "dict.value(key)"],
            "correct": 1
        },
        {
            "id": 9,
            "question": "Django ORM-da bir nechta shartlarni 'OR' mantiqiy amali orqali birlashtirish uchun nima ishlatiladi?",
            "options": ["django.db.models.Q", "django.db.models.F", "django.db.models.OR", "django.db.models.Case"],
            "correct": 0
        },
        {
            "id": 10,
            "question": "Python-da generator funksiya yaratish uchun qaysi kalit so'z ishlatiladi?",
            "options": ["return", "yield", "generate", "next"],
            "correct": 1
        },
        {
            "id": 11,
            "question": "Django-da CSRF himoyasi nima uchun xizmat qiladi?",
            "options": ["SQL inyeksiya oldini olish uchun", "Saytlararo soxta so'rovlar (Cross-Site Request Forgery) oldini olish uchun", "XSS hujumlaridan himoya qilish uchun", "DDoS hujumlaridan saqlash uchun"],
            "correct": 1
        },
        {
            "id": 12,
            "question": "PostgreSQL-da birlamchi kalit (Primary Key) vazifasi nima?",
            "options": ["Jadvaldagi yozuvlarni saralash", "Jadvaldagi har bir satrni yagona va takrorlanmas qilib belgilash", "Satrlarni shifrlash", "Foreign key yaratish"],
            "correct": 1
        },
        {
            "id": 13,
            "question": "Django REST Framework (DRF) da model ma'lumotlarini JSON formatiga o'tkazuvchi asosiy komponent nima?",
            "options": ["View", "Router", "Serializer", "Middleware"],
            "correct": 2
        },
        {
            "id": 14,
            "question": "Python-da 'lambda' nima?",
            "options": ["Nomsiz, bir qatordan iborat anonim funksiya", "Maxsus xatolik turi", "Modul import qilish buyrug'i", "Klass konstruktori"],
            "correct": 0
        },
        {
            "id": 15,
            "question": "Django loyihasida Middleware qachon ishga tushadi?",
            "options": ["Faqat foydalanuvchi tizimga kirganda", "Har bir so'rov (request) kelganda va javob (response) qaytayotganda", "Faqat ma'lumotlar bazasiga so'rov yuborilganda", "Faqat server ishga tushganda"],
            "correct": 1
        },
        {
            "id": 16,
            "question": "Python-da kontekst menejeri yaratish uchun qaysi dunder metodlar kerak?",
            "options": ["__init__ va __del__", "__enter__ va __exit__", "__start__ va __stop__", "__open__ va __close__"],
            "correct": 1
        },
        {
            "id": 17,
            "question": "Django ORM-da `User.objects.filter(age__gte=18)` so'rovi qanday ma'no bildiradi?",
            "options": ["Yoshi 18 dan kichik bo'lganlar", "Yoshi 18 ga teng yoki undan katta bo'lganlar", "Yoshi aynan 18 bo'lganlar", "Yoshi 18 dan katta bo'lganlar"],
            "correct": 1
        },
        {
            "id": 18,
            "question": "Python-da dekorator (decorator) nima?",
            "options": ["HTML dizaynini o'zgartiruvchi funksiya", "Boshqa funksiya yoki metodning xatti-harakatini o'zgartirmasdan kengaytiruvchi funksiya", "Klassning xususiy xususiyati", "Modul o'rnatuvchi vosita"],
            "correct": 1
        },
        {
            "id": 19,
            "question": "Django-da ko'pdan-ko'pga (Many-to-Many) munosabatini ifodalash uchun qaysi maydon ishlatiladi?",
            "options": ["ForeignKey", "OneToOneField", "ManyToManyField", "ArrayField"],
            "correct": 2
        },
        {
            "id": 20,
            "question": "HTTP 401 status kodi nimani bildiradi?",
            "options": ["Bad Request", "Unauthorized (Avtorizatsiyadan o'tmagan)", "Forbidden", "Not Found"],
            "correct": 1
        },
        {
            "id": 21,
            "question": "Python-da `is` va `==` operatorlarining asosiy farqi nimada?",
            "options": ["Hech qanday farqi yo'q", "`==` qiymatlarni solishtiradi, `is` xotiradagi ob'ekt identifikatorini (id) solishtiradi", "`is` faqat satrlar uchun ishlatiladi", "`==` faqat raqamlar uchun ishlatiladi"],
            "correct": 1
        },
        {
            "id": 22,
            "question": "Django ORM-da 'N+1 muammosi'ni hal qilish uchun qaysi metodlar ishlatiladi?",
            "options": ["filter() va exclude()", "select_related() va prefetch_related()", "order_by() va distinct()", "values() va values_list()"],
            "correct": 1
        },
        {
            "id": 23,
            "question": "Python-da xatoliklarni ushlash va qayta ishlash uchun qaysi blok ishlatiladi?",
            "options": ["try - except - finally", "try - catch - throw", "if - else - error", "catch - handle"],
            "correct": 0
        },
        {
            "id": 24,
            "question": "Git-da yangi filial (branch) ochish va unga o'tish buyrug'i qaysi?",
            "options": ["git branch create <nom>", "git checkout -b <nom>", "git switch new <nom>", "git fork <nom>"],
            "correct": 1
        },
        {
            "id": 25,
            "question": "Django-da foydalanuvchi parolini xavfsiz saqlashda qaysi mexanizmdan foydalaniladi?",
            "options": ["Ochiq matn ko'rinishida", "Base64 kodlash", "PBKDF2 SHA-256 xeshlash algoritmi", "MD5 xesh"],
            "correct": 2
        },
        {
            "id": 26,
            "question": "Python-da ro'yxatni o'sish tartibida saralash uchun qaysi metod ishlatiladi?",
            "options": ["list.order()", "list.sort()", "list.arrange()", "list.reverse()"],
            "correct": 1
        },
        {
            "id": 27,
            "question": "Celery va Redis nima uchun Django loyihalarida ishlatiladi?",
            "options": ["CSS uslublarini kompilyatsiya qilish uchun", "Asinxron fon vazifalarini va xabarlar navbatini bajarish uchun", "Ma'lumotlar bazasi zaxirasini olish uchun", "Foydalanuvchi interfeysini chizish uchun"],
            "correct": 1
        },
        {
            "id": 28,
            "question": "RESTful API-da ma'lumotlar qaysi formatda almashinilishi eng ommabop hisoblanadi?",
            "options": ["XML", "JSON", "CSV", "YAML"],
            "correct": 1
        },
        {
            "id": 29,
            "question": "Python dasturida `__name__ == '__main__'` sharti nima maqsadda yoziladi?",
            "options": ["Fayl bevosita ishga tushirilgandagina blok ichidagi kodni bajarish uchun", "Klass nomini aniqlash uchun", "Python versiyasini tekshirish uchun", "Global o'zgaruvchilarni tozalash uchun"],
            "correct": 0
        },
        {
            "id": 30,
            "question": "Django-da statik fayllarni (CSS, JS, rasmlar) ishlab chiqarish serveriga yig'ish buyrug'i qaysi?",
            "options": ["python manage.py runserver", "python manage.py collectstatic", "python manage.py build_static", "python manage.py compileassets"],
            "correct": 1
        }
    ],
    'web-dasturlash': [
        {
            "id": 1,
            "question": "HTML-da veb-sahifaning asosiy sarlavhasi (eng yuqori darajadagi) qaysi teg bilan yoziladi?",
            "options": ["<head>", "<h6>", "<h1>", "<header>"],
            "correct": 2
        },
        {
            "id": 2,
            "question": "CSS-da elementlarni moslashuvchan (flexible) joylashtirish uchun qaysi xususiyat ishlatiladi?",
            "options": ["display: flex;", "float: left;", "position: absolute;", "align: center;"],
            "correct": 0
        },
        {
            "id": 3,
            "question": "JavaScript-da o'zgarmas o'zgaruvchi e'lon qilish uchun qaysi kalit so'z ishlatiladi?",
            "options": ["var", "let", "const", "def"],
            "correct": 2
        },
        {
            "id": 4,
            "question": "DOM (Document Object Model) nima?",
            "options": ["CSS kutubxonasi", "HTML hujjatining ob'ektli daraxtsimon tuzilishi", "Brauzer ma'lumotlar bazasi", "JavaScript versiyasi"],
            "correct": 1
        },
        {
            "id": 5,
            "question": "React-da komponent holatini (state) saqlash uchun qaysi Hook ishlatiladi?",
            "options": ["useEffect", "useMemo", "useState", "useRef"],
            "correct": 2
        },
        {
            "id": 6,
            "question": "CSS Box Model tarkibiga qaysi qismlar kiradi?",
            "options": ["content, padding, border, margin", "header, main, footer", "top, bottom, left, right", "width, height, radius"],
            "correct": 0
        },
        {
            "id": 7,
            "question": "JavaScript-da `===` va `==` operatorlarining farqi nimada?",
            "options": ["Farqi yo'q", "`===` qiymat bilan birga ma'lumot turini (type) ham tekshiradi", "`==` qat'iyroq tekshiradi", "`===` faqat matnlar uchun"],
            "correct": 1
        },
        {
            "id": 8,
            "question": "HTML5 semantik teglariga qaysilar kiradi?",
            "options": ["<div>, <span>, <b>", "<header>, <nav>, <article>, <footer>", "<table>, <tr>, <td>", "<font>, <center>, <u>"],
            "correct": 1
        },
        {
            "id": 9,
            "question": "CSS Grid-da ustunlarni 3 ta teng qismga bo'lish qanday yoziladi?",
            "options": ["grid-template-columns: 1fr 1fr 1fr;", "columns: 3;", "grid-split: 3;", "display: grid 3;"],
            "correct": 0
        },
        {
            "id": 10,
            "question": "JavaScript-da asinxron operatsiyalar bilan ishlash uchun qaysi konstruksiya eng zamonaviy hisoblanadi?",
            "options": ["callbacks", "threads", "async / await", "goto"],
            "correct": 2
        },
        {
            "id": 11,
            "question": "React-da yon ta'sirlarni (side effects, masalan ma'lumot yuklash) boshqarish uchun qaysi Hook ishlatiladi?",
            "options": ["useState", "useEffect", "useCallback", "useContext"],
            "correct": 1
        },
        {
            "id": 12,
            "question": "Veb-brauzerda ma'lumotlarni sessiya yopilgandan keyin ham saqlab qoluvchi ombor qaysi?",
            "options": ["sessionStorage", "cookies faqat", "localStorage", "RAM cache"],
            "correct": 2
        },
        {
            "id": 13,
            "question": "CSS-da `z-index` xususiyati ishlashi uchun elementda qaysi shart bajarilishi kerak?",
            "options": ["display: none bo'lishi", "position qiymati static bo'lmasligi (masalan: relative, absolute, fixed)", "kengligi 100% bo'lishi", "margin auto bo'lishi"],
            "correct": 1
        },
        {
            "id": 14,
            "question": "JavaScript-da massiv elementlarini yangi formatga o'tkazib yangi massiv hosil qiluvchi metod qaysi?",
            "options": ["forEach()", "map()", "filter()", "push()"],
            "correct": 1
        },
        {
            "id": 15,
            "question": "React-da JSX nima?",
            "options": ["JavaScript kutubxonasi", "JavaScript sintaksisi kengaytmasi bo'lib, JS ichida HTML ko'rinishida yozish imkonini beradi", "CSS preprotsessori", "JSON ma'lumotlar turi"],
            "correct": 1
        },
        {
            "id": 16,
            "question": "HTTP so'rovida serverdan ma'lumot olish uchun qaysi metod ishlatiladi?",
            "options": ["POST", "PUT", "GET", "DELETE"],
            "correct": 2
        },
        {
            "id": 17,
            "question": "JavaScript-da Closure (yopilish) nima?",
            "options": ["Dasturni yopuvchi funksiya", "Ichki funksiyaning o'zidan tashqaridagi funksiya doirasidagi o'zgaruvchilarga kirish imkoniyati", "Xatolikni yopish usuli", "Modulni yopish"],
            "correct": 1
        },
        {
            "id": 18,
            "question": "CSS-da media queries `@media (max-width: 768px)` nima uchun ishlatiladi?",
            "options": ["Rasmlar sifatini oshirish uchun", "Moslashuvchan (Responsive) dizayn yaratish va planshet/mobil ekranlarga moslash uchun", "Ranglarni o'zgartirish uchun", "Shriftlarni yuklash uchun"],
            "correct": 1
        },
        {
            "id": 19,
            "question": "React-da Props nima?",
            "options": ["Komponent ichki holati", "Ota komponentdan bola komponentga uzatiladigan ma'lumotlar", "HTML atributlari", "Server konfiguratsiyasi"],
            "correct": 1
        },
        {
            "id": 20,
            "question": "JavaScript Event Loop mexanizmining vazifasi nima?",
            "options": ["Massivlarni aylantirish", "Kallback va asinxron vazifalar navbatini kuzatib, Call Stack bo'shaganda ularni bajarish", "Animatsiyalar yaratish", "Sahifani yangilash"],
            "correct": 1
        },
        {
            "id": 21,
            "question": "HTML-da forma ma'lumotlarini serverga yuborish uchun qaysi atribut ishlatiladi?",
            "options": ["action va method", "src va href", "type va rel", "target va class"],
            "correct": 0
        },
        {
            "id": 22,
            "question": "CSS-da `rem` va `em` o'lchov birliklarining farqi nima?",
            "options": ["rem ota elementga, em root elementga bog'liq", "rem sahifa ildiz (root `<html>`) shrift hajmiga, em esa ota element shrift hajmiga asoslanadi", "Ikkalasi ham piksellarga teng", "rem faqat balandlik uchun ishlatiladi"],
            "correct": 1
        },
        {
            "id": 23,
            "question": "JavaScript-da Promise qanday holatlarga (states) ega bo'lishi mumkin?",
            "options": ["pending, fulfilled, rejected", "start, pause, stop", "true, false, null", "open, close, wait"],
            "correct": 0
        },
        {
            "id": 24,
            "question": "SPA (Single Page Application) nimani anglatadi?",
            "options": ["Bir nechta sahifali veb-sayt", "Sahifani qayta yuklamasdan dinamik kontent yangilanuvchi bitta sahifali ilova", "Faqat bitta rasm saqlovchi sayt", "Mobil ilova turi"],
            "correct": 1
        },
        {
            "id": 25,
            "question": "CSS-da elementni markazga joylashtirishning (Flexbox orqali) eng to'g'ri yo'li qaysi?",
            "options": ["justify-content: center; align-items: center;", "text-align: middle;", "float: center;", "margin: auto middle;"],
            "correct": 0
        },
        {
            "id": 26,
            "question": "JavaScript `fetch()` funksiyasi qanday natija qaytaradi?",
            "options": ["String", "HTML element", "Promise", "Boolean"],
            "correct": 2
        },
        {
            "id": 27,
            "question": "React-da Virtual DOM nima uchun ishlatiladi?",
            "options": ["Ma'lumotlar bazasini saqlash uchun", "Haqiqiy DOM ga o'zgarishlarni tezkor va samarali kiritish orqali unumdorlikni oshirish uchun", "Xavfsizlikni kuchaytirish uchun", "Rasm hajmini qisqartirish uchun"],
            "correct": 1
        },
        {
            "id": 28,
            "question": "Git-da o'zgarishlarni serverga (masalan GitHub) yuborish buyrug'i qaysi?",
            "options": ["git pull", "git push", "git commit", "git add"],
            "correct": 1
        },
        {
            "id": 29,
            "question": "HTML-da qidiruv tizimlari (SEO) uchun tavsif yozishda qaysi meta teg ishlatiladi?",
            "options": ["<meta name='viewport'>", "<meta name='description' content='...'>", "<meta charset='UTF-8'>", "<meta name='keywords'>"],
            "correct": 1
        },
        {
            "id": 30,
            "question": "JavaScript-da obyekt xususiyatlarini oson ajratib olish (destructuring) qanday yoziladi?",
            "options": ["const { name, age } = user;", "const [name, age] = user;", "const user = extract(name, age);", "const name = user->name;"],
            "correct": 0
        },
    'ai-data-science': [
        {
            "id": 1,
            "question": "Data Scienceda o'rtacha qiymat (Mean) va Mediana o'rtasidagi asosiy farq nimada?",
            "options": ["Farqi yo'q", "Mediana keskin anomal qiymatlarga (outliers) chidamliroq", "Mean faqat matnlar uchun", "Mediana har doim 0 ga teng"],
            "correct": 1
        },
        {
            "id": 2,
            "question": "NumPy da 2 o'lchovli massiv o'lchamini (qator va ustunlar soni) bilish uchun qaysi atribut ishlatiladi?",
            "options": ["arr.size", "arr.shape", "arr.dim", "arr.length"],
            "correct": 1
        },
        {
            "id": 3,
            "question": "Pandas kutubxonasida CSV faylni o'qish uchun qaysi funksiya ishlatiladi?",
            "options": ["pd.read_csv()", "pd.open_csv()", "pd.load_csv()", "pd.get_csv()"],
            "correct": 0
        },
        {
            "id": 4,
            "question": "Pandas DataFrame da bo'sh (null/NaN) qiymatlarni tekshirish funksiyasi qaysi?",
            "options": ["df.isna() yoki df.isnull()", "df.empty()", "df.has_none()", "df.check_null()"],
            "correct": 0
        },
        {
            "id": 5,
            "question": "Matplotlib da ikki o'zgaruvchi o'rtasidagi bog'liqlikni nuqtalar orqali ifodalash grafigi qaysi?",
            "options": ["plt.bar()", "plt.hist()", "plt.scatter()", "plt.pie()"],
            "correct": 2
        },
        {
            "id": 6,
            "question": "Seaborn kutubxonasida ustunlararo korrelyatsiya matritsasini rangli issiqlik xaritasi bilan chizish metodi qaysi?",
            "options": ["sns.heatmap()", "sns.colormap()", "sns.corrplot()", "sns.matrix()"],
            "correct": 0
        },
        {
            "id": 7,
            "question": "Mashinali o'rganishda Chiziqli Regressiya (Linear Regression) qanday turdagi vazifalarni yechish uchun mo'ljallangan?",
            "options": ["Klasterlash", "Uzluksiz sonli qiymatlarni bashorat qilish", "Matnlarni tarjima qilish", "Rasmlarni siqish"],
            "correct": 1
        },
        {
            "id": 8,
            "question": "Scikit-Learn da ma'lumotlarni o'qitish (train) va testlash (test) to'plamlariga ajratish funksiyasi qaysi?",
            "options": ["train_test_split()", "split_data()", "data_divider()", "cross_split()"],
            "correct": 0
        },
        {
            "id": 9,
            "question": "Regressiya modellarining xatoligini o'lchovchi MSE nimani anglatadi?",
            "options": ["Maximum Square Error", "Mean Squared Error (O'rtacha kvadratik xato)", "Minimum Standard Error", "Model Sample Error"],
            "correct": 1
        },
        {
            "id": 10,
            "question": "Klassifikatsiya vazifasida ehtimollikni 0 va 1 oralig'iga keltiruvchi faollashtirish funksiyasi qaysi?",
            "options": ["ReLU", "Sigmoid", "Linear", "Step"],
            "correct": 1
        },
        {
            "id": 11,
            "question": "Qarorlar daraxti (Decision Tree) ansambli asosida qurilgan eng mashhur klassifikatsiya algoritmi qaysi?",
            "options": ["K-Means", "Random Forest", "Linear Regression", "PCA"],
            "correct": 1
        },
        {
            "id": 12,
            "question": "Klassifikatsiyada model aniqligini (Precision, Recall) tahlil qilish uchun qanday jadval tuziladi?",
            "options": ["Pivot Table", "Confusion Matrix (Xatoliklar matritsasi)", "Lookup Table", "Hash Matrix"],
            "correct": 1
        },
        {
            "id": 13,
            "question": "Nazoratsiz o'rganishda (Unsupervised Learning) ma'lumotlar qanday bo'ladi?",
            "options": ["Har bir satrda to'g'ri javob (yorliq/label) bo'lmaydi", "Barcha javoblar oldindan ma'lum bo'ladi", "Faqat matnli ma'lumotlar bo'ladi", "Faqat rasmlar bo'ladi"],
            "correct": 0
        },
        {
            "id": 14,
            "question": "K-Means algoritmining asosiy maqsadi nima?",
            "options": ["Ma'lumotlarni o'xshashlik bo'yicha 'k' ta klasterga (guruhga) ajratish", "Sonlarni saralash", "Matnlarni qisqartirish", "Parollarni shifrlash"],
            "correct": 0
        },
        {
            "id": 15,
            "question": "K-Means algoritmi uchun eng maqbul klasterlar sonini topish usuli qanday nomlanadi?",
            "options": ["Elbow Method (Tirsak usuli)", "Grid Method", "Gradient Descent", "Random Search"],
            "correct": 0
        },
        {
            "id": 16,
            "question": "PCA (Principal Component Analysis) algoritmining asosiy vazifasi nima?",
            "options": ["Ma'lumotlar o'lchamini (ustunlar sonini) asosiy axborotni saqlagan holda qisqartirish", "Baza hajmini kattalashtirish", "Xotirani tozalash", "Rasm rangini o'zgartirish"],
            "correct": 0
        },
        {
            "id": 17,
            "question": "Neyron tarmoqlarda ReLU (Rectified Linear Unit) faollashtirish funksiyasi qanday ishlaydi?",
            "options": ["f(x) = max(0, x)", "f(x) = x^2", "f(x) = 1 / (1 + e^-x)", "f(x) = sin(x)"],
            "correct": 0
        },
        {
            "id": 18,
            "question": "Neyron tarmog'ida vaznlarni (weights) xatolik hosilasi bo'yicha orqaga yangilash algoritmi nima deyiladi?",
            "options": ["Forward propagation", "Backpropagation (Xatolikni orqaga tarqatish)", "Data augmentation", "Batch normalization"],
            "correct": 1
        },
        {
            "id": 19,
            "question": "Deep Learningda tasvirlar (rasmlar) bilan ishlashda eng samarali neyron tarmoq arxitekturasi qaysi?",
            "options": ["RNN", "CNN (Convolutional Neural Networks)", "Linear Regression", "Decision Tree"],
            "correct": 1
        },
        {
            "id": 20,
            "question": "CNN arxitekturasida tasvir hajmini kichraytirib, asosiy xususiyatlarni saqlovchi qatlam qaysi?",
            "options": ["MaxPooling2D", "Dense", "Flatten", "Dropout"],
            "correct": 0
        },
        {
            "id": 21,
            "question": "Neyron tarmoqni haddan tashqari moslashib ketishidan (Overfitting) himoyalash uchun qaysi qatlam tasodifiy neyronlarni o'chiradi?",
            "options": ["Dropout", "InputLayer", "Softmax", "Reshape"],
            "correct": 0
        },
        {
            "id": 22,
            "question": "Keras kutubxonasida qatlamlarni ketma-ket joylashtirib model quruvchi klass qaysi?",
            "options": ["Sequential", "LinearChain", "LayerStack", "NetworkModel"],
            "correct": 0
        },
        {
            "id": 23,
            "question": "NLP (Natural Language Processing) da matnni so'zlar yoki belgilar bo'laklariga ajratish jarayoni nima deyiladi?",
            "options": ["Tokenization", "Encoding", "Vectorization", "Stemming"],
            "correct": 0
        },
        {
            "id": 24,
            "question": "LLM qisqartmasi nimani anglatadi?",
            "options": ["Large Language Model (Katta Til Modeli)", "Low Level Memory", "Logical Linear Method", "Linked Learning Module"],
            "correct": 0
        },
        {
            "id": 25,
            "question": "FastAPI freymvorki mashinali o'rganish modellarini deploy qilishda nima uchun afzal ko'riladi?",
            "options": ["Juda tezkor asinxron ishlashi va avtomatik Swagger hujjatlash mavjudligi uchun", "Faqat rasmlar bilan ishlagani uchun", "Ma'lumotlar bazasisiz ishlagani uchun", "Python talab qilmagani uchun"],
            "correct": 0
        },
        {
            "id": 26,
            "question": "Pandas da `df.describe()` metodi qanday natija beradi?",
            "options": ["Barcha sonli ustunlarning umumiy statistik ko'rsatkichlarini (count, mean, std, min, max)", "Faqat birinchi 5 qatorni", "Faqat ustunlar nomini", "Bazada xatoliklar sonini"],
            "correct": 0
        },
        {
            "id": 27,
            "question": "Overfitting (qayta moslashish) holati nimani anglatadi?",
            "options": ["Model o'qitish ma'lumotlarida a'lo natija ko'rsatib, yangi test ma'lumotlarida past aniqlik berishi", "Model umuman o'rgana olmasligi", "Ma'lumotlar juda kamligi", "Kompyuter xotirasi to'lib qolishi"],
            "correct": 0
        },
        {
            "id": 28,
            "question": "Scikit-Learn da barcha ustunlarni 0 va 1 oralig'iga keltiruvchi masshtablashtiruvchi vosita qaysi?",
            "options": ["MinMaxScaler", "StandardScaler", "Normalizer", "RobustScaler"],
            "correct": 0
        },
        {
            "id": 29,
            "question": "Neyron tarmoqda o'rganish tezligini (qadam kattaligini) belgilovchi giperparametr qaysi?",
            "options": ["Learning Rate", "Epoch", "Batch Size", "Momentum"],
            "correct": 0
        },
        {
            "id": 30,
            "question": "Mashinali o'rganish modelini ishlab chiqarishga saqlash va yuklash uchun qaysi kutubxona ishlatiladi?",
            "options": ["joblib yoki pickle", "csv", "json", "os"],
            "correct": 0
        }
    ],
    'mobile-dev': [
        {
            "id": 1,
            "question": "Dart dasturlash tilida qiymati keyinchalik o'zgarmaydigan konstantalar qaysi kalit so'z bilan e'lon qilinadi?",
            "options": ["const yoki final", "var", "dynamic", "static"],
            "correct": 0
        },
        {
            "id": 2,
            "question": "Dart tilida o'zgaruvchi null qiymat qabul qilishi mumkinligini bildirish uchun qaysi belgi ishlatiladi?",
            "options": ["?", "!", "*", "&"],
            "correct": 0
        },
        {
            "id": 3,
            "question": "Flutter arxitekturasida 'Everything is a...' tamoyili nimani ifodalaydi?",
            "options": ["Widget (Vidjet)", "Class", "Function", "Module"],
            "correct": 0
        },
        {
            "id": 4,
            "question": "Flutter dasturining kirish nuqtasi bo'lgan asosiy funksiya qaysi?",
            "options": ["void main() { runApp(...); }", "void startApp()", "void init()", "void execute()"],
            "correct": 0
        },
        {
            "id": 5,
            "question": "Material dizayn standartlariga mos asosiy ekran tuzilmasini (AppBar, Body, FloatingActionButton) taqdim etuvchi vidjet qaysi?",
            "options": ["Scaffold", "MaterialApp", "Container", "Column"],
            "correct": 0
        },
        {
            "id": 6,
            "question": "Flutterda elementlarni vertikal ravishda (ustma-ust) joylashtirish uchun qaysi vidjet ishlatiladi?",
            "options": ["Column", "Row", "Stack", "Wrap"],
            "correct": 0
        },
        {
            "id": 7,
            "question": "Flutterda elementlarni gorizontal ravishda (yonma-yon) joylashtirish uchun qaysi vidjet ishlatiladi?",
            "options": ["Row", "Column", "Align", "Center"],
            "correct": 0
        },
        {
            "id": 8,
            "question": "Elementlarni bir-birining ustiga (qatlam-qatlam) joylashtirish uchun qaysi vidjet ishlatiladi?",
            "options": ["Stack", "Layer", "Over", "Position"],
            "correct": 0
        },
        {
            "id": 9,
            "question": "StatelessWidget va StatefulWidget o'rtasidagi asosiy farq nimada?",
            "options": ["StatefulWidget o'zgaruvchan ichki holatga (state) ega va qayta chizilishi mumkin", "StatelessWidget tezroq", "Farqi yo'q", "StatefulWidget faqat animatsiyalar uchun"],
            "correct": 0
        },
        {
            "id": 10,
            "question": "StatefulWidget da ekranni yangi ma'lumotlar bilan qayta chizish uchun qaysi metod chaqiriladi?",
            "options": ["setState(() {})", "refresh()", "rebuild()", "update()"],
            "correct": 0
        },
        {
            "id": 11,
            "question": "Katta hajmdagi ro'yxat elementlarini faqat ekranda ko'ringandagina xotiraga yuklab chizuvchi optimallashgan vidjet qaysi?",
            "options": ["ListView.builder", "SingleChildScrollView", "Column", "Row"],
            "correct": 0
        },
        {
            "id": 12,
            "question": "Foydalanuvchi matn kiritishi uchun Flutterda qaysi vidjet ishlatiladi?",
            "options": ["TextField yoki TextFormField", "TextInput", "InputField", "TextEdit"],
            "correct": 0
        },
        {
            "id": 13,
            "question": "TextField ga kiritilgan matnni o'qish va boshqarish uchun qaysi klass obyekti ishlatiladi?",
            "options": ["TextEditingController", "TextReader", "FieldManager", "StringController"],
            "correct": 0
        },
        {
            "id": 14,
            "question": "Flutterda bir ekrandan ikkinchi ekranga o'tish uchun qaysi mexanizm ishlatiladi?",
            "options": ["Navigator.push(context, ...)", "Screen.open()", "Router.goto()", "Page.next()"],
            "correct": 0
        },
        {
            "id": 15,
            "question": "Ochiq ekranni yopib oldingi ekranga qaytish uchun qaysi buyruq yoziladi?",
            "options": ["Navigator.pop(context)", "Navigator.back()", "Screen.close()", "Page.destroy()"],
            "correct": 0
        },
        {
            "id": 16,
            "question": "Flutterda serverga HTTP so'rovlar (GET, POST) yuborish uchun eng ommabop rasmiy paket qaysi?",
            "options": ["http", "net", "web_request", "socket_io"],
            "correct": 0
        },
        {
            "id": 17,
            "question": "Asinxron server so'rovlari natijasini kutib, yuklanayotgan paytda spinner chiqaruvchi vidjet qaysi?",
            "options": ["FutureBuilder", "AsyncWidget", "WaitBuilder", "StreamColumn"],
            "correct": 0
        },
        {
            "id": 18,
            "question": "Dart tilida JSON qatorini (String) Map obyektiga o'tkazuvchi funksiya qaysi?",
            "options": ["jsonDecode()", "jsonParse()", "jsonToMap()", "stringToJson()"],
            "correct": 0
        },
        {
            "id": 19,
            "question": "Flutterda Provider orqali global holat o'zgarganda barcha tinglovchilarni ogohlantiruvchi miksin qaysi?",
            "options": ["ChangeNotifier", "StateNotifier", "EventBus", "Observable"],
            "correct": 0
        },
        {
            "id": 20,
            "question": "Provider holatidagi ma'lumotlarni o'qish va tinglash uchun vidjet daraxtida qaysi komponent ishlatiladi?",
            "options": ["Consumer", "Listener", "Watcher", "Observer"],
            "correct": 0
        },
        {
            "id": 21,
            "question": "Ilova yopilganda ham kichik ma'lumotlarni (masalan: dark mode yoki token) saqlab qoluvchi kutubxona qaysi?",
            "options": ["shared_preferences", "local_ram", "device_cache", "temp_db"],
            "correct": 0
        },
        {
            "id": 22,
            "question": "Flutterda vidjet atrofida bo'sh joy qoldirish uchun qaysi vidjetdan foydalaniladi?",
            "options": ["Padding", "Margin", "Spacer faqat", "Border"],
            "correct": 0
        },
        {
            "id": 23,
            "question": "Vidjetni ekranning o'rtasiga joylashtiruvchi qulay maxsus vidjet qaysi?",
            "options": ["Center", "Middle", "Align.middle", "CenterBox"],
            "correct": 0
        },
        {
            "id": 24,
            "question": "Container vidjetiga rang, burchak yumaloqligi (borderRadius) va soya berish uchun qaysi xususiyat ishlatiladi?",
            "options": ["decoration: BoxDecoration(...)", "style: ContainerStyle(...)", "border: Border(...)", "paint: Paint(...)"],
            "correct": 0
        },
        {
            "id": 25,
            "question": "Flutter kodiga o'zgartirish kiritilganda ilovani qayta o'rnatmasdan sekund ichida yangilash xususiyati nima?",
            "options": ["Hot Reload", "Quick Compile", "Live Sync", "Fast Refresh"],
            "correct": 0
        },
        {
            "id": 26,
            "question": "Mobil ilovaning rasmiy release APK faylini yaratish uchun terminalda qaysi buyruq beriladi?",
            "options": ["flutter build apk --release", "flutter compile apk", "flutter make release", "flutter export android"],
            "correct": 0
        },
        {
            "id": 27,
            "question": "Flutterda pubspec.yaml fayli nima uchun xizmat qiladi?",
            "options": ["Loyiha bog'liqliklari (dependencies), versiya, rasmlar va shriftlarni sozlash uchun", "Faqat Android manifesti uchun", "CSS kodlari uchun", "Ma'lumotlar bazasi jadvallari uchun"],
            "correct": 0
        },
        {
            "id": 28,
            "question": "Vidjetga bosish hodisasini (onTap, onDoubleTap, onLongPress) qo'shish uchun qaysi vidjet bilan o'rash mumkin?",
            "options": ["GestureDetector yoki InkWell", "TouchArea", "ClickListener", "ButtonWrapper"],
            "correct": 0
        },
        {
            "id": 29,
            "question": "Flutterda to'rsimon (2 yoki 3 ustunli kafel) maket yaratish uchun qaysi vidjet eng mos keladi?",
            "options": ["GridView", "TableLayout", "BoxGrid", "MatrixView"],
            "correct": 0
        },
        {
            "id": 30,
            "question": "Flutterda ilovaning orqa fon rangi, asosiy shrifti va temalarini butun ilova bo'ylab belgilovchi obyekt qaysi?",
            "options": ["ThemeData", "AppStyle", "GlobalDesign", "ColorPalette"],
            "correct": 0
        }
    ],
    'ui-ux-design': [
        {
            "id": 1,
            "question": "UI (User Interface) va UX (User Experience) o'rtasidagi asosiy farq nimada?",
            "options": ["UI vizual ko'rinish va elementlar dizayni, UX esa foydalanish qulayligi va tizim mantiqi", "UI va UX bir xil narsa", "UI faqat kod yozish, UX rasm chizish", "UX faqat ranglar tanlash"],
            "correct": 0
        },
        {
            "id": 2,
            "question": "Figma dasturida ekranni yoki ishchi maydonni yaratish uchun qaysi asosiy vosita (shortcut 'F') ishlatiladi?",
            "options": ["Frame", "Rectangle", "Canvas", "Artboard"],
            "correct": 0
        },
        {
            "id": 3,
            "question": "UI dizaynda 60-30-10 ranglar qoidasi qanday taqsimlanadi?",
            "options": ["60% dominant fon rangi, 30% ikkilamchi rang, 10% diqqatni tortuvchi (aktsent) rang", "60% qora, 30% oq, 10% kulrang", "60% aktsent, 30% fon, 10% matn", "Teng 33% dan"],
            "correct": 0
        },
        {
            "id": 4,
            "question": "WCAG standartiga ko'ra oddiy matn va uning foni o'rtasidagi minimal kontrast nisbati qancha bo'lishi kerak?",
            "options": ["Kamida 4.5:1", "1:1", "2:1", "100:1"],
            "correct": 0
        },
        {
            "id": 5,
            "question": "UI dizaynda nima uchun 8-pikselli setka tizimi (8pt Grid System) keng qo'llaniladi?",
            "options": ["Aksariyat zamonaviy ekran o'lchamlari 8 ga bo'lingani va tartibli mutanosiblik ta'minlangani uchun", "8 raqami omadli bo'lgani uchun", "Faqat Apple talabi bo'lgani uchun", "CSS faqat 8px ni tanigani uchun"],
            "correct": 0
        },
        {
            "id": 6,
            "question": "Figmada elementlarga Auto Layout qo'shish uchun qaysi klavishlar birikmasi bosiladi?",
            "options": ["Shift + A", "Ctrl + L", "Alt + A", "Ctrl + G"],
            "correct": 0
        },
        {
            "id": 7,
            "question": "Figma Auto Layout parametrlarida 'Hug contents' nimani anglatadi?",
            "options": ["Freym hajmi ichidagi elementlar hajmi bo'yicha avtomatik torayib quchoqlab oladi", "Freym butun ekranni egallaydi", "Freym o'lchami muzlatiladi", "Elementlar o'chib ketadi"],
            "correct": 0
        },
        {
            "id": 8,
            "question": "Figmada master komponentdan olingan nusxa nima deb ataladi?",
            "options": ["Instance", "Copy", "Duplicate", "Child"],
            "correct": 0
        },
        {
            "id": 9,
            "question": "Tugmaning turli holatlarini (Default, Hover, Active, Disabled) bitta komponentda boshqarish uchun nima yaratiladi?",
            "options": ["Variants (Variantlar)", "Frames", "Groups", "Layers"],
            "correct": 0
        },
        {
            "id": 10,
            "question": "UX tadqiqotida 'User Persona' nima?",
            "options": ["Maqsadli foydalanuvchilar guruhining ehtiyojlari va xulq-atvorini ifodalovchi to'qima umumlashtirilgan profil", "Dizaynerning shaxsiy rezyumesi", "Kompaniya rahbari surati", "Foydalanuvchi paroli"],
            "correct": 0
        },
        {
            "id": 11,
            "question": "Foydalanuvchining muammoni hal qilish yo'lidagi qadamlari va his-tuyg'ulari aks etgan xarita nima deb ataladi?",
            "options": ["User Journey Map (Foydalanuvchi yo'li xaritasi)", "Sitemap", "Roadmap", "Wireframe"],
            "correct": 0
        },
        {
            "id": 12,
            "question": "Dizaynning eng dastlabki, rangsiz va tafsilotsiz oq-qora eskiz ko'rinishi nima deyiladi?",
            "options": ["Low-fidelity Wireframe", "High-fidelity Prototype", "Mockup", "Design System"],
            "correct": 0
        },
        {
            "id": 13,
            "question": "Dizayn Tizimi (Design System) tarkibiga qaysi elementlar kiradi?",
            "options": ["Ranglar, tipografiya, oraliqlar (spacing), UI komponentlar va foydalanish qoidalari", "Faqat logotip", "Faqat shrift fayllari", "Dastur server sozlamalari"],
            "correct": 0
        },
        {
            "id": 14,
            "question": "Figmada komponentlar bir-biri bilan silliq o'zgarishi va animatsiya bo'lishi uchun qaysi o'tish effekti ishlatiladi?",
            "options": ["Smart Animate", "Dissolve", "Instant", "Move Out"],
            "correct": 0
        },
        {
            "id": 15,
            "question": "Foydalanuvchining interfeysdagi biror harakatiga javoban beriladigan kichik vizual fikr-mulohaza (masalan: layk bosganda yurakchani sakrashi) nima deyiladi?",
            "options": ["Micro-interaction (Mikro-o'zaro ta'sir)", "Macro-animation", "Hover-effect", "Trigger"],
            "correct": 0
        },
        {
            "id": 16,
            "question": "Figma Dev Mode nima uchun xizmat qiladi?",
            "options": ["Dasturchilar dizayn o'lchamlarini, CSS kodlarini va assetlarni oson ko'rib olishlari uchun", "Figma ichida Java yozish uchun", "Saytni internetga yuklash uchun", "Rasm hajmini kichraytirish uchun"],
            "correct": 0
        },
        {
            "id": 17,
            "question": "Tipografiyada matn qatorlari orasidagi masofa qanday ataladi?",
            "options": ["Line height (Leading)", "Tracking", "Kerning", "Letter spacing"],
            "correct": 0
        },
        {
            "id": 18,
            "question": "UI elementlarda ko'zni charchatmaslik va o'qishni osonlashtirish uchun elementlar atrofidagi bo'sh joy nima deyiladi?",
            "options": ["White space (Negative space)", "Empty space", "Zero zone", "Dead area"],
            "correct": 0
        },
        {
            "id": 19,
            "question": "Mobil interfeyslarda 'Thumb Zone' tushunchasi nimani bildiradi?",
            "options": ["Telefonni bir qo'lda ushlaganda bosh barmoq eng oson yetib boradigan qulay hudud", "Ekran yorug'ligi", "Klaviatura maydoni", "Barmoq izi skaneri joyi"],
            "correct": 0
        },
        {
            "id": 20,
            "question": "Foydalanish qulayligini tekshirish uchun real foydalanuvchilar bilan o'tkaziladigan sinov jarayoni nima deyiladi?",
            "options": ["Usability Testing", "Unit Testing", "Stress Testing", "Beta Coding"],
            "correct": 0
        },
        {
            "id": 21,
            "question": "Figma-da bir xil elementlar guruhini (masalan: 3 ta kartochkani) tekis teng oraliqda taqsimlash buyrug'i qaysi?",
            "options": ["Tidy Up", "Pack Horizontal", "Spread", "Balance"],
            "correct": 0
        },
        {
            "id": 22,
            "question": "UI dizaynda 'Affordance' atamasi nimani anglatadi?",
            "options": ["Elementning ko'rinishidan uning qanday vazifa bajarishi darhol anglashilishi (masalan: tugmaning bosiluvchan ko'rinishi)", "Dizayn narxi", "Dastur tezligi", "Rasm formati"],
            "correct": 0
        },
        {
            "id": 23,
            "question": "Figmada SVG formatidagi vektor ikonkalar nima uchun PNG ga nisbatan afzal ko'riladi?",
            "options": ["Sifati yo'qolmasdan istalgancha kattalashishi va hajmi juda yengilligi uchun", "Faqat qora rangda bo'lgani uchun", "Eksport qilib bo'lmagani uchun", "Faqat Apple qurilmalarida ishlagani uchun"],
            "correct": 0
        },
        {
            "id": 24,
            "question": "Web dizaynda standart asosiy matn (Body text) shrift o'lchami qancha bo'lishi tavsiya etiladi?",
            "options": ["16px (1rem)", "8px", "32px", "6px"],
            "correct": 0
        },
        {
            "id": 25,
            "question": "Figmada bitta uslubdagi rang yoki shriftni bir vaqtning o'zida butun loyihada yangilash uchun nima ishlatiladi?",
            "options": ["Local Styles (Stillashtirish kutubxonasi)", "Find & Replace", "Layer reorder", "Export settings"],
            "correct": 0
        },
        {
            "id": 26,
            "question": "Fitts qonuni (Fitts's Law) bo'yicha interfeysdagi muhim tugmalar qanday bo'lishi kerak?",
            "options": ["Yetarlicha katta va foydalanuvchi barmoq/kursori uchun oson yetadigan joyda", "Iloji boricha kichik", "Ekran burchagiga yashirilgan", "Faqat qora fonda"],
            "correct": 0
        },
        {
            "id": 27,
            "question": "Mobil ilovalarda pastki asosiy navigatsiya paneli nima deb ataladi?",
            "options": ["Bottom Navigation Bar", "Top Header", "Drawer", "Footer"],
            "correct": 0
        },
        {
            "id": 28,
            "question": "Figma faylini boshqa dizaynerlar yoki buyurtmachi bilan birga real vaqtda tahrirlash imkoniyati nima deyiladi?",
            "options": ["Real-time Collaboration", "Single Mode", "Offline Editing", "Local Sync"],
            "correct": 0
        },
        {
            "id": 29,
            "question": "Interfeysda muvaffaqiyat xabarlari uchun asosan qaysi rang xalqaro psixologik standart hisoblanadi?",
            "options": ["Yashil (Green)", "Qizil", "Sariq", "Qora"],
            "correct": 0
        },
        {
            "id": 30,
            "question": "UX dizaynda 'A/B Testing' nima?",
            "options": ["Dizaynning ikki xil variantini turli foydalanuvchilarga ko'rsatib, qaysi biri samaraliroq ekanini solishtirish", "Alifbo bo'yicha saralash", "Ranglarni tekshirish", "Xatoliklarni o'chirish"],
            "correct": 0
        }
    ],
    'kiberxavfsizlik': [
        {
            "id": 1,
            "question": "Axborot xavfsizligining oltin uchburchagi (CIA Triadasi) tarkibiga qaysi tamoyillar kiradi?",
            "options": ["Confidentiality (Maxfiylik), Integrity (Butunlik), Availability (Foydalanishga ochiqlik)", "Control, Inspect, Attack", "Cloud, Internet, Access", "Crypto, IP, Auth"],
            "correct": 0
        },
        {
            "id": 2,
            "question": "OSI modelining qaysi qatlamida IP manzillash va marshrutlash (routing) amalga oshiriladi?",
            "options": ["Network Layer (3-qatlam)", "Data Link (2-qatlam)", "Transport (4-qatlam)", "Application (7-qatlam)"],
            "correct": 0
        },
        {
            "id": 3,
            "question": "Xavfsiz veb-ulanishni ta'minlovchi HTTPS protokoli sukut bo'yicha (default) qaysi portdan foydalanadi?",
            "options": ["443", "80", "22", "8080"],
            "correct": 0
        },
        {
            "id": 4,
            "question": "Masofaviy xavfsiz boshqaruvni ta'minlovchi SSH (Secure Shell) protokoli qaysi port orqali ishlaydi?",
            "options": ["22", "21", "23", "25"],
            "correct": 0
        },
        {
            "id": 5,
            "question": "Linux operatsion tizimida fayl huquqlarini o'zgartirish uchun qaysi buyruq ishlatiladi?",
            "options": ["chmod", "chown", "ls -l", "passwd"],
            "correct": 0
        },
        {
            "id": 6,
            "question": "Linuxda barcha ochiq portlar va faol tarmoq ulanishlarini ko'rish uchun qaysi buyruq ishlatiladi?",
            "options": ["netstat yoki ss", "ping", "traceroute", "ifconfig"],
            "correct": 0
        },
        {
            "id": 7,
            "question": "Kriptografiyada bir xil maxfiy kalit ham shifrlash, ham qayta ochish uchun ishlatiladigan tizim nima deyiladi?",
            "options": ["Simmetrik shifrlash (masalan: AES)", "Asimmetrik shifrlash (RSA)", "Bir tomonlama xesh", "Ochiq kalitli tizim"],
            "correct": 0
        },
        {
            "id": 8,
            "question": "Asimmetrik shifrlashda (masalan: RSA) ma'lumotni shifrlash uchun qaysi kalit ishlatiladi?",
            "options": ["Public Key (Ochiq kalit)", "Private Key (Yopiq kalit)", "Session Key", "Secret Hash"],
            "correct": 0
        },
        {
            "id": 9,
            "question": "Xeshlash (Hashing) algoritmlarining (masalan: SHA-256) shifrlashdan asosiy farqi nimada?",
            "options": ["Xesh bir tomonlama bo'lib, uni asl holatiga qaytarib (dekodlab) bo'lmaydi", "Xesh faqat qisqa so'zlar uchun", "Xesh sekin ishlaydi", "Farqi yo'q"],
            "correct": 0
        },
        {
            "id": 10,
            "question": "Bazada saqlanayotgan parollarni 'Rainbow table' hujumlaridan himoyalash uchun parollarga nima qo'shiladi?",
            "options": ["Salt (Tasodifiy belgilar qatori)", "Pepper", "Sugar", "Secret Token"],
            "correct": 0
        },
        {
            "id": 11,
            "question": "OSINT (Open Source Intelligence) nimani anglatadi?",
            "options": ["Ochiq va qonuniy ommaviy manbalardan ma'lumot to'plash razvedkasi", "DDoS hujumi", "Yopiq bazalarni buzish", "Virus yaratish"],
            "correct": 0
        },
        {
            "id": 12,
            "question": "Google qidiruv tizimida maxsus operatorlar yordamida yashirin yoki zaif fayllarni topish usuli nima deyiladi?",
            "options": ["Google Dorking", "Google Phishing", "Deep Search", "Web Crawling"],
            "correct": 0
        },
        {
            "id": 13,
            "question": "Internetga ulangan qurilmalar, serverlar va ochiq portlarni qidiruvchi mashhur qidiruv tizimi qaysi?",
            "options": ["Shodan", "Yahoo", "Baidu", "DuckDuckGo"],
            "correct": 0
        },
        {
            "id": 14,
            "question": "Tarmoq xavfsizligini skanerlash va ochiq portlarni aniqlashda eng mashhur vosita qaysi?",
            "options": ["Nmap", "Wireshark", "Burp Suite", "Metasploit"],
            "correct": 0
        },
        {
            "id": 15,
            "question": "Nmap-da to'liq ulanish o'rnatmasdan yashirincha skanerlash qiluvchi 'SYN Stealth Scan' parametri qaysi?",
            "options": ["-sS", "-sT", "-sU", "-sV"],
            "correct": 0
        },
        {
            "id": 16,
            "question": "Veb-ilovalar xavfsizligi bo'yicha dunyodagi eng nufuzli xalqaro tashkilot qaysi?",
            "options": ["OWASP (Open Web Application Security Project)", "IEEE", "ISO", "W3C"],
            "correct": 0
        },
        {
            "id": 17,
            "question": "Hujumchi veb-forma orqali ma'lumotlar bazasiga g'arazli so'rov kiritib bazani o'g'irlashi qanday zaiflik?",
            "options": ["SQL Injection (SQLi)", "Cross-Site Scripting (XSS)", "Brute Force", "Buffer Overflow"],
            "correct": 0
        },
        {
            "id": 18,
            "question": "SQL Injection hujumlaridan himoyalanishning eng ishonchli dasturiy usuli qaysi?",
            "options": ["Parametrlangan so'rovlar (Prepared Statements / ORM)", "Foydalanuvchi parolini tekshirish", "HTTPS ishlatish", "Portni yopish"],
            "correct": 0
        },
        {
            "id": 19,
            "question": "Hujumchi veb-sahifaga g'arazli JavaScript kodini kiritib, boshqa foydalanuvchilar sessiyasini o'g'irlashi nima deyiladi?",
            "options": ["Cross-Site Scripting (XSS)", "CSRF", "DDoS", "MITM"],
            "correct": 0
        },
        {
            "id": 20,
            "question": "XSS hujumlarida o'g'irlanadigan cookie fayllarini JavaScript o'qiy olmasligi uchun unga qaysi bayroq (flag) qo'yiladi?",
            "options": ["HttpOnly", "Secure", "SameSite", "ReadOnly"],
            "correct": 0
        },
        {
            "id": 21,
            "question": "Foydalanuvchini aldamchilik yo'li bilan soxta saytga kiritib login va parolini o'g'irlash usuli nima?",
            "options": ["Phishing (Fishing)", "Pharming", "Ransomware", "Trojan"],
            "correct": 0
        },
        {
            "id": 22,
            "question": "Ikki bosqichli autentifikatsiya (2FA) nima uchun xavfsizlikni bir necha barobar oshiradi?",
            "options": ["Parol o'g'irlanganda ham ikkinchi faktor (telefon kodi yoki TOTP) talab qilingani uchun", "Parolni eslab qolish shart bo'lmagani uchun", "Internet tezlashgani uchun", "Sayt tez yuklangani uchun"],
            "correct": 0
        },
        {
            "id": 23,
            "question": "Tarmoq trafigini kuzatib, ruxsatsiz yoki xavfli paketlarni bloklovchi himoya devori nima?",
            "options": ["Firewall (Xavfsizlik devori)", "Router", "Switch", "Hub"],
            "correct": 0
        },
        {
            "id": 24,
            "question": "Tarmoqdagi hujumlarni aniqlash tizimi qisqartmasi qanday ataladi?",
            "options": ["IDS (Intrusion Detection System)", "IPS faqat", "DNS", "NAT"],
            "correct": 0
        },
        {
            "id": 25,
            "question": "Serverga millionlab soxta so'rovlar yuborib uni ishdan chiqarish hujumi nima deb ataladi?",
            "options": ["DDoS (Distributed Denial of Service)", "Man in the Middle", "Zero Day", "Phishing"],
            "correct": 0
        },
        {
            "id": 26,
            "question": "Foydalanuvchi kompyuteridagi fayllarni shifrlab qo'yib, ochish uchun to'lov talab qiluvchi zararli dastur turi qaysi?",
            "options": ["Ransomware (Tovlamachi dastur)", "Spyware", "Adware", "Rootkit"],
            "correct": 0
        },
        {
            "id": 27,
            "question": "Zaiflik hali dastur ishlab chiqaruvchisiga ma'lum bo'lmasdan turib hujum qilish holati nima deyiladi?",
            "options": ["Zero-Day Vulnerability", "One-Day Bug", "Known Exploit", "Patch Alert"],
            "correct": 0
        },
        {
            "id": 28,
            "question": "Qonuniy ruxsat asosida tizim zaifliklarini sinash va hisobot berish jarayoni nima?",
            "options": ["Penetration Testing (Pentest)", "Cracking", "Blackhat Hack", "Malware analysis"],
            "correct": 0
        },
        {
            "id": 29,
            "question": "Tarmoq paketlarini ushlab olib (sniffing) tahlil qiluvchi eng mashhur vosita qaysi?",
            "options": ["Wireshark", "Postman", "FileZilla", "Putty"],
            "correct": 0
        },
        {
            "id": 30,
            "question": "Zaifliklarning xavflilik darajasini 0 dan 10 gacha ball bilan baholovchi xalqaro standart qaysi?",
            "options": ["CVSS (Common Vulnerability Scoring System)", "ISO 27001", "OWASP Score", "RiskRank"],
            "correct": 0
        }
    ]
    ]
}

def get_final_test_for_slug(slug):
    slug_lower = (slug or '').lower()
    if 'python' in slug_lower or 'backend' in slug_lower:
        return FINAL_TEST_QUESTIONS['python-backend']
    elif 'web' in slug_lower or 'frontend' in slug_lower:
        return FINAL_TEST_QUESTIONS['web-dasturlash']
    elif 'ai' in slug_lower or 'data' in slug_lower:
        return FINAL_TEST_QUESTIONS['ai-data-science']
    elif 'mobil' in slug_lower or 'flutter' in slug_lower or 'dart' in slug_lower:
        return FINAL_TEST_QUESTIONS['mobile-dev']
    elif 'ui' in slug_lower or 'ux' in slug_lower or 'design' in slug_lower:
        return FINAL_TEST_QUESTIONS['ui-ux-design']
    elif 'kiber' in slug_lower or 'cyber' in slug_lower:
        return FINAL_TEST_QUESTIONS['kiberxavfsizlik']
    return FINAL_TEST_QUESTIONS.get(slug_lower, FINAL_TEST_QUESTIONS['python-backend'])
