"""
Learnify - 6 ta Yo'nalish bo'yicha To'liq 10 talik Video Darslar O'quv Dasturi (Curriculum)
Har bir yo'nalish oson asoslardan boshlanib murakkab professional texnologiyalargacha ketma-ketlikda tuzilgan.
"""

CURRICULUM_DATA = {
    'python-backend': {
        'title': 'Python & Backend',
        'icon': 'server',
        'color': '#a855f7',
        'videos': [
            {
                "id": 1, "youtube_id": "nLRL_NcnK-4",
                "title": "1-Dars: Python Kirish, O'zgaruvchilar va Shart Operatorlari",
                "channel": "Programming with Mosh",
                "duration": "48:00", "completed": False, "active": True,
                "desc": "Python dasturlash tiliga kirish, o'rnatish, o'zgaruvchilar, ma'lumot turlari (str, int, float, bool) va if/elif/else shart operatorlari.",
                "homework": {
                    "title": "1-Dars Vazifasi: Shaxsiy Kalkulyator va Shart Operatorlari",
                    "objective": "Python o'zgaruvchilari, input(), arifmetik amallar va if/elif/else yordamida konsol dasturi yarating.",
                    "tasks": [
                        "Foydalanuvchining ismi va tug'ilgan yilini input() orqali qabul qilib, yoshini hisoblang.",
                        "Ikkita son va amal (+, -, *, /) kiritilganda natijani chiqaruvchi kalkulyator yozing.",
                        "Nolga bo'lish holatini (ZeroDivisionError) if/else orqali tekshiring.",
                        "Kodingizni toza va tushunarli izohlar bilan yozib yuboring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 2, "youtube_id": "kqtD5dpn9C8",
                "title": "2-Dars: Ma'lumotlar Tuzilmalari (List, Dict, Tuple, Set) va Sikllar",
                "channel": "Programming with Mosh",
                "duration": "55:00", "completed": False, "active": False,
                "desc": "Pythonda ro'yxatlar (List), lug'atlar (Dict), kortejlar (Tuple), to'plamlar (Set), for va while sikllari, hamda ro'yxat generatorlari.",
                "homework": {
                    "title": "2-Dars Vazifasi: O'quvchilar Baholari Tahlili Dasturi",
                    "objective": "Lug'at va ro'yxatlardan foydalanib o'quvchilar baholarini boshqaruvchi dastur tuzing.",
                    "tasks": [
                        "Talabalar ismlari va ularning fanlardan olgan baholarini saqlovchi dict tuzilmasini yarating.",
                        "Har bir talabaning o'rtacha ballini sikl orqali hisoblang.",
                        "Eng yuqori va eng past o'rtacha ball to'plagan talabalarni aniqlang.",
                        "Natijalarni konsolda chiroyli formatlangan jadval ko'rinishida chiqaring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 3, "youtube_id": "8ext9G7xspg",
                "title": "3-Dars: Funksiyalar, Modullar, Paketlar va Fayllar Bilan Ishlash",
                "channel": "freeCodeCamp.org",
                "duration": "1:05:00", "completed": False, "active": False,
                "desc": "Funksiyalar (def, *args, **kwargs, return), lambda ifodalari, modullarni import qilish, fayllarni o'qish/yozish (open, with) va try-except.",
                "homework": {
                    "title": "3-Dars Vazifasi: Matnli Fayllar Bilan Ishlovchi Modul",
                    "objective": "Matnli faylni o'qib, so'zlar sonini hisoblaydigan va xatolarni ushlovchi funksional modul yarating.",
                    "tasks": [
                        "Berilgan matnli faylni (.txt) xavfsiz (with open) usulda ochib o'qing.",
                        "Matndagi jami so'zlar soni va eng ko'p takrorlangan 5 ta so'zni aniqlang.",
                        "Fayl topilmagan holatda FileNotFoundError xatosini try-except bilan to'g'ri ushlang.",
                        "Tahlil natijalarini yangi 'hisobot.txt' fayliga yozib saqlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 4, "youtube_id": "JeznW_70ZVU",
                "title": "4-Dars: Obyektga Yo'naltirilgan Dasturlash (OOP) Asoslari",
                "channel": "Corey Schafer",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "OOP tamoyillari: Klasslar, Obyektlar, Konstruktor (__init__), Vorislik (Inheritance), Inkapsulyatsiya va Polimorfizm.",
                "homework": {
                    "title": "4-Dars Vazifasi: Bank Hisob Raqami Tizimi (OOP)",
                    "objective": "Klasslar va merosxo'rlik yordamida bank hisob raqamlari tizimini dasturlang.",
                    "tasks": [
                        "'BankAccount' klassini (balans, egasining ismi, depozit va pul yechish metodlari) yarating.",
                        "Balansdan ortiq pul yechishga urinilganda xabar beruvchi shart yozing.",
                        "'SavingsAccount' voris klassini yaratib, unga foiz qo'shish metodini qo'shing.",
                        "Kamida 2 ta obyekt yaratib, amallarni bajarib ko'rsating."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 5, "youtube_id": "qw--VYLpxG4",
                "title": "5-Dars: Relyatsion Ma'lumotlar Bazasi va SQL / PostgreSQL",
                "channel": "freeCodeCamp.org",
                "duration": "1:20:00", "completed": False, "active": False,
                "desc": "Relyatsion ma'lumotlar bazasi, SQL so'rovlar (SELECT, INSERT, UPDATE, DELETE), jadvallarni bog'lash (JOINs, Foreign Keys) va PostgreSQL.",
                "homework": {
                    "title": "5-Dars Vazifasi: SQL Jadvallar va Python Bilan Integratsiya",
                    "objective": "SQL jadvallarini loyihalash va Python sqlite3/psycopg2 orqali CRUD amallarini bajarish.",
                    "tasks": [
                        "'users' va 'orders' jadvallarini Foreign Key munosabati bilan yarating.",
                        "Kamida 5 ta foydalanuvchi va ularga tegishli buyurtmalarni SQL orqali qo'shing.",
                        "INNER JOIN yordamida har bir foydalanuvchi va uning buyurtmalarini chiqaruvchi so'rov yozing.",
                        "Pythonda ushbu bazaga ulanib ma'lumotlarni qabul qiluvchi skript yozing."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 6, "youtube_id": "rHux0gMZ3Eg",
                "title": "6-Dars: Django Web Framework Asoslari va MVT Arxitekturasi",
                "channel": "freeCodeCamp.org",
                "duration": "1:30:00", "completed": False, "active": False,
                "desc": "Django loyihasini yaratish, MVT (Model-View-Template) arxitekturasi, urls.py marshrutlash, views.py funksiyalari va HTML shablonlari.",
                "homework": {
                    "title": "6-Dars Vazifasi: Ilk Django Veb-Sahifasi va Routing",
                    "objective": "Django loyihasi va ilovasini yaratib, dinamik shablonlar bilan ishlovchi sahifalar tuzing.",
                    "tasks": [
                        "Yangi Django loyihasi va 'blog' nomli ilova yarating.",
                        "Bosh sahifa, 'Biz haqimizda' va 'Aloqa' sahifalari uchun view va url sozlang.",
                        "HTML shablonlarda Django Template Language (DTL) sikllari va shartlaridan foydalaning.",
                        "Statik fayllarni (CSS va rasmlar) shablonga to'g'ri ulang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 7, "youtube_id": "F5mRW0jo-U4",
                "title": "7-Dars: Django Modellar, ORM va Ma'lumotlar Bazasi Migratsiyalari",
                "channel": "Dennis Ivy",
                "duration": "1:10:00", "completed": False, "active": False,
                "desc": "Django ORM modellarini e'lon qilish, makemigrations va migrate, QuerySet so'rovlari (filter, exclude, get), Django Admin panel sozlamalari.",
                "homework": {
                    "title": "7-Dars Vazifasi: Blog Modeli va Admin Panel Boshqaruvi",
                    "objective": "Django ORM modeli yaratish, migratsiya qilish va ma'lumotlarni admin orqali boshqarish.",
                    "tasks": [
                        "Sarlavha, matn, muallif (ForeignKey), sana maydonlariga ega Post modelini yarating.",
                        "Migratsiyalarni muvaffaqiyatli bajaring va Django Admin panelga modelni ro'yxatdan o'tkazing.",
                        "Admin panelda qidiruv (search_fields) va filtrlash (list_filter) parametrlarini sozlang.",
                        "Veb-sahifada barcha postlarni bazadan olib dinamik ko'rsating."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 8, "youtube_id": "c708Nf0cDiM",
                "title": "8-Dars: Django REST Framework (DRF) va RESTful API Yaratish",
                "channel": "freeCodeCamp.org",
                "duration": "1:25:00", "completed": False, "active": False,
                "desc": "REST API tushunchasi, JSON formati, DRF Serializers, APIView, Generic Views, ModelViewSet va Routers yordamida to'liq CRUD API.",
                "homework": {
                    "title": "8-Dars Vazifasi: Mahsulotlar Katalogi uchun REST API",
                    "objective": "DRF yordamida to'liq CRUD amallarini bajaruvchi RESTful API endpointlarini quring.",
                    "tasks": [
                        "Mahsulot modeli uchun ModelSerializer klassini yozing.",
                        "GET (ro'yxat va detal), POST, PUT, DELETE operatsiyalari uchun endpointlar yarating.",
                        "Postman yoki Swagger orqali so'rovlar yuborib test qiling.",
                        "API javob kodlari (200, 201, 400, 404) to'g'ri qaytishini ta'minlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 9, "youtube_id": "PUzgZrS_piQ",
                "title": "9-Dars: API Xavfsizligi, JWT Autentifikatsiya va Ruxsatlar",
                "channel": "Tech With Tim",
                "duration": "1:00:00", "completed": False, "active": False,
                "desc": "API autentifikatsiyasi turlari, JSON Web Tokens (JWT: access va refresh tokenlar), djangorestframework-simplejwt, IsAuthenticated ruxsatlari.",
                "homework": {
                    "title": "9-Dars Vazifasi: JWT Token Bilan Himoyalangan API",
                    "objective": "Foydalanuvchini ro'yxatdan o'tkazish, login qilish va yopiq API larni token bilan himoyalash.",
                    "tasks": [
                        "Foydalanuvchi registratsiyasi va login qilib JWT token beruvchi API endpointlarni sozlang.",
                        "Mahsulotlarni o'chirish va yangilash API sini faqat IsAuthenticated foydalanuvchilarga oching.",
                        "Token yaroqlilik muddatini (Access token va Refresh token) sozlang.",
                        "Postman orqali 'Authorization: Bearer <token>' headeri bilan muvaffaqiyatli so'rov yuboring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 10, "youtube_id": "THxCy_k47oM",
                "title": "10-Dars: Asinxron Vazifalar (Celery & Redis), Testlash va Deploy Qilish",
                "channel": "Pretty Printed",
                "duration": "1:35:00", "completed": False, "active": False,
                "desc": "Backend tizimlarida fon vazifalari (Celery), xabarlar brokeri (Redis), Django Unit testlar yozish va loyihani ishlab chiqarishga deploy qilish.",
                "homework": {
                    "title": "10-Dars Vazifasi: Asinxron Vazifalar va Loyihani Deployga Tayyorlash",
                    "objective": "Celery orqali asinxron xabarlar yuborish vazifasini ulash va avtomatlashtirilgan testlar yozish.",
                    "tasks": [
                        "Celery va Redis brokerini Django loyihasiga sozlang.",
                        "Foydalanuvchi ro'yxatdan o'tganda xush kelibsiz xatini asinxron fonda yuboruvchi Celery vazifasi yozing.",
                        "API endpointlar uchun kamida 3 ta muvaffaqiyatli unit test yozing.",
                        "Loyihani ishlab chiqarish sozlamalarini (DEBUG=False, ALLOWED_HOSTS, SECRET_KEY) tayyorlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            }
        ]
    },
    'web-dasturlash': {
        'title': 'Web Dasturlash',
        'icon': 'code',
        'color': '#38bdf8',
        'videos': [
            {
                "id": 1, "youtube_id": "kUMe1FH4CHE",
                "title": "1-Dars: HTML5 Asoslari va Semantik Veb-Sahifa Tuzilmasi",
                "channel": "freeCodeCamp.org",
                "duration": "50:00", "completed": False, "active": True,
                "desc": "HTML5 tushunchasi, teglarning ishlashi, sarlavhalar, matnlar, havolalar, rasmlar, formalar, inputlar va semantik teglar (header, nav, main, footer).",
                "homework": {
                    "title": "1-Dars Vazifasi: Shaxsiy Rezume / Portfolio Veb-Sahifasi",
                    "objective": "Faqat toza semantik HTML5 teglaridan foydalanib shaxsiy rezyume sahifasini yarating.",
                    "tasks": [
                        "Semantik teglardan (<header>, <nav>, <section>, <article>, <footer>) to'g'ri foydalaning.",
                        "O'zingiz haqingizda ma'lumot, bilim darajasi va loyihalar ro'yxatini tuzing.",
                        "Bog'lanish uchun forma (ism, email, xabar va yuborish tugmasi) joylashtiring.",
                        "W3C validatoridan xatolarsiz o'tgan toza HTML kod yozing."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 2, "youtube_id": "1PnVor36_40",
                "title": "2-Dars: CSS3 Asoslari, Box Model va Zamonaviy Stillash",
                "channel": "freeCodeCamp.org",
                "duration": "1:05:00", "completed": False, "active": False,
                "desc": "CSS selektorlari, ranglar, shriftlar, CSS Box Model (margin, border, padding, content), box-sizing va kartochkalar dizayni.",
                "homework": {
                    "title": "2-Dars Vazifasi: Mahsulot Kartochkasi va Tugmalar Dizayni",
                    "objective": "CSS Box Model va stillash xususiyatlari yordamida zamonaviy interfeys komponentlarini chizing.",
                    "tasks": [
                        "HTML sahifadagi elementlarga CSS klasslar orqali chiroyli dizayn bering.",
                        "Soyalar (box-shadow), burchak yumaloqligi (border-radius) va gradientlardan foydalaning.",
                        "Tugmalar ustiga sichqoncha kelganda (hover, transition) silliq animatsiya qo'shing.",
                        "Box-sizing: border-box qoidasini to'g'ri qo'llang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 3, "youtube_id": "fYq5PXgSsbE",
                "title": "3-Dars: Flexbox, CSS Grid va Moslashuvchan (Responsive) Dizayn",
                "channel": "Traversy Media",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "Flexbox (justify-content, align-items, flex-direction), CSS Grid (grid-template-columns, gap), media queries (@media) va mobil moslashuv.",
                "homework": {
                    "title": "3-Dars Vazifasi: Moslashuvchan (Responsive) Landing Page",
                    "objective": "Flexbox va CSS Grid yordamida telefon, planshet va kompyuterga moslashuvchan maket tuzing.",
                    "tasks": [
                        "Navigatsiya panelini Flexbox orqali ikki tomonga yoying.",
                        "Xizmatlar yoki kurslar bo'limini CSS Grid yordamida 3 ustunli qilib terishingiz kerak.",
                        "@media queries yordamida 768px dan kichik ekranlarda bloklarni 1 ustunga o'tkazing.",
                        "Sayt gorizontal skroll (overflow-x) chiqarmasligini ta'minlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 4, "youtube_id": "W6NZfCO5SIk",
                "title": "4-Dars: JavaScript Asoslari: O'zgaruvchilar, Shartlar va Funksiyalar",
                "channel": "Programming with Mosh",
                "duration": "1:00:00", "completed": False, "active": False,
                "desc": "JavaScript sintaksisi, o'zgaruvchilar (let, const), ma'lumot turlari, arifmetik va mantiqiy operatorlar, if/else, for/while sikllari va funksiyalar.",
                "homework": {
                    "title": "4-Dars Vazifasi: Interaktiv Hisoblagich va Matematik Mashq",
                    "objective": "JavaScript shartlari va funksiyalari yordamida amaliy algoritmik vazifalarni yeching.",
                    "tasks": [
                        "Foydalanuvchi yoshiga qarab kirishga ruxsat beruvchi funksiya yozing.",
                        "1 dan 100 gacha bo'lgan juft sonlarni konsolga chiqaruvchi sikl tuzing.",
                        "Massivdagi eng katta va eng kichik sonni topuvchi funksiya yarating.",
                        "Kodingizni brauzer konsolida ishlatib tekshirib ko'ring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 5, "youtube_id": "y17RuWkWdn8",
                "title": "5-Dars: JavaScript DOM Bilan Ishlash va Interaktiv Hodisalar (Events)",
                "channel": "freeCodeCamp.org",
                "duration": "1:10:00", "completed": False, "active": False,
                "desc": "DOM daraxti, elementlarni tanlash (querySelector), addEventListener hodisalari (click, input, submit), elementlar yaratish va sinflarni boshqarish.",
                "homework": {
                    "title": "5-Dars Vazifasi: Interaktiv Todo List Ilovasi",
                    "objective": "DOM manipulyatsiyasi orqali vazifalar qo'shish, o'chirish va bajarilganini belgilash ilovasi.",
                    "tasks": [
                        "Inputga yozilgan vazifani tugma bosilganda yangi <li> elementi sifatida ro'yxatga qo'shing.",
                        "Har bir vazifa yonida 'O'chirish' tugmasini yarating va bosilganda o'chiring.",
                        "Vazifa ustiga bosilganda uning ustiga chizib bajarilgan deb belgilang.",
                        "Bo'sh matn kiritilishini ogohlantirish bilan taqiqlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 6, "youtube_id": "Oive66jrwBs",
                "title": "6-Dars: Zamonaviy JavaScript (ES6+), Asinxronlik va Fetch API",
                "channel": "freeCodeCamp.org",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "ES6 xususiyatlari: Arrow functions, Destructuring, Spread/Rest operatori, Promises, async/await va tashqi API dan fetch() orqali ma'lumot olish.",
                "homework": {
                    "title": "6-Dars Vazifasi: API Orqali Foydalanuvchilar Kartochkalari",
                    "objective": "Ochiq REST API ga fetch so'rovi yuborib, olingan JSON ma'lumotlarini veb-sahifaga chizing.",
                    "tasks": [
                        "jsonplaceholder.typicode.com/users API siga async/await orqali so'rov yuboring.",
                        "Kelgan ma'lumotlarni massiv map() metodi orqali aylanib chiqing.",
                        "Har bir foydalanuvchi uchun ism, email va kompaniyasi ko'rsatilgan kartochka yarating.",
                        "Yuklanish jarayonida (loading) spinneni va xatolik yuz berganda xabarni ko'rsating."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 7, "youtube_id": "bMknfKXIFA8",
                "title": "7-Dars: React.js Asoslari: Komponentlar, JSX va Props",
                "channel": "freeCodeCamp.org",
                "duration": "1:20:00", "completed": False, "active": False,
                "desc": "React kutubxonasiga kirish, Vite orqali loyiha ochish, Funksional komponentlar, JSX sintaksisi va Props orqali ma'lumot uzatish.",
                "homework": {
                    "title": "7-Dars Vazifasi: Qayta Ishlatiluvchi Komponentlar Vitrinasi",
                    "objective": "Reactda qayta ishlatiluvchi (reusable) komponentlar yaratib, ularga props uzating.",
                    "tasks": [
                        "Vite yordamida yangi toza React loyihasi ishga tushiring.",
                        "'ProductCard' nomli alohida komponent yarating va unga rasm, nom, narx propslarini uzating.",
                        "Massivdagi kamida 4 ta mahsulotni map() orqali ekranga chiqaring.",
                        "Har bir elementga unikal 'key' atributi qo'shing."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 8, "youtube_id": "4UZrsTqkcW4",
                "title": "8-Dars: React State va Hooks: useState hamda useEffect",
                "channel": "Web Dev Simplified",
                "duration": "1:10:00", "completed": False, "active": False,
                "desc": "Reactda holat boshqaruvi (useState), interaktiv amallar, komponent hayot sikli, serverdan ma'lumot yuklash va tozalash (useEffect).",
                "homework": {
                    "title": "8-Dars Vazifasi: Qidiruv va Filtratsiyali React Ilova",
                    "objective": "useState va useEffect yordamida dinamik qidiruv va filtratsiyaga ega ilova quring.",
                    "tasks": [
                        "Qidiruv inputi uchun alohida state (searchTerm) yarating.",
                        "useEffect orqali API dan ma'lumot yuklang va state ga saqlang.",
                        "Foydalanuvchi yozishi bilan ro'yxatni real vaqt rejimida filtrlang.",
                        "Yuklanish jarayoni va bo'sh natija holatlarini boshqaring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 9, "youtube_id": "Law7wfdg_ls",
                "title": "9-Dars: React Router va Global Holat Boshqaruvi (Context API)",
                "channel": "Traversy Media",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "react-router-dom yordamida ko'p sahifali SPA yaratish (Routes, Route, Link, useParams) va Context API orqali global holatni boshqarish.",
                "homework": {
                    "title": "9-Dars Vazifasi: Ko'p Sahifali Do'kon va Savatcha Tizimi",
                    "objective": "React Router navigatsiyasi va Context API yordamida xarid savatchasi tizimini tuzing.",
                    "tasks": [
                        "Bosh sahifa, Mahsulotlar va Savatcha sahifalari o'rtasida navigatsiya yarating.",
                        "CartContext yaratib, unga savatchadagi tovarlar ro'yxati va qo'shish/o'chirish funksiyalarini joylang.",
                        "Istalgan sahifadan savatchaga tovar qo'shilganda savatchadagi umumiy son dinamik yangilansin.",
                        "Savatcha sahifasida umumiy hisob-kitob summasini ko'rsating."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 10, "youtube_id": "8jj101D3knE",
                "title": "10-Dars: Fullstack Integratsiya, Optimizatsiya va Vercel-da Deploy",
                "channel": "freeCodeCamp.org",
                "duration": "1:30:00", "completed": False, "active": False,
                "desc": "React ilovasini Backend API bilan bog'lash, ishlab chiqarish uchun yig'ish (npm run build), Lighthouse auditi, SEO va Vercel/Netlify-da deploy.",
                "homework": {
                    "title": "10-Dars Vazifasi: Loyihani Production Deploy Qilish",
                    "objective": "Tayyor frontend ilovasini GitHub-ga yuklab, Vercel yoki Netlify orqali jonli internetga chiqaring.",
                    "tasks": [
                        "Loyiha kodlarini tozalab, ortiqcha console.log larni o'chiring va build qilib tekshiring.",
                        "Loyihani shaxsiy GitHub repozitoriyingizga push qiling.",
                        "Vercel yoki Netlify servisini repozitoriy bilan bog'lab jonli domenga deploy qiling.",
                        "Jonli ishlayotgan havola (Live link) va GitHub havolasini topshiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            }
        ]
    },
    'ai-data-science': {
        'title': "Sun'iy Intellekt & Data Science",
        'icon': 'brain',
        'color': '#ec4899',
        'videos': [
            {
                "id": 1, "youtube_id": "LHBE6Q9XlzI",
                "title": "1-Dars: Data Science uchun Python Asoslari va Matematik Tushunchalar",
                "channel": "freeCodeCamp.org",
                "duration": "55:00", "completed": False, "active": True,
                "desc": "Data Science sohasiga kirish, Pythonning ilmiy kutubxonalari, chiziqli algebra, ehtimollar nazariyasi va tavsifiy statistika asoslari.",
                "homework": {
                    "title": "1-Dars Vazifasi: Statistik Ko'rsatkichlarni Hisoblovchi Dastur",
                    "objective": "Pythonda sof matematik hisob-kitoblar va statistik funktsiyalarni yozish.",
                    "tasks": [
                        "Berilgan sonlar to'plami uchun o'rtacha arifmetik qiymatni (mean) hisoblang.",
                        "To'plamning medianasi (median) va modasini (mode) aniqlovchi funksiya yozing.",
                        "Dispersiya (variance) va standart og'ishni (std deviation) hisoblang.",
                        "Natijalarni formatlab chiroyli konsol hisoboti ko'rinishida chiqaring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 2, "youtube_id": "QUT1VHiLmmI",
                "title": "2-Dars: NumPy Kutubxonasi: Ko'p O'lchovli Massivlar va Vektorlar",
                "channel": "freeCodeCamp.org",
                "duration": "1:00:00", "completed": False, "active": False,
                "desc": "NumPy kutubxonasi, ndarray tuzilishi, massivlarni kesish (slicing), broadcasting, matritsalar ustida arifmetik amallar va tezkor hisoblashlar.",
                "homework": {
                    "title": "2-Dars Vazifasi: NumPy Bilan Matritsa Operatsiyalari",
                    "objective": "NumPy massivlari va chiziqli algebra amallarini dasturiy amalga oshirish.",
                    "tasks": [
                        "Tasodifiy sonlardan iborat 3x3 va 3x3 matritsalarni yarating.",
                        "Matritsalarni ko'paytirish (dot product) va transponirlash amallarini bajaring.",
                        "Matritsaning determinantini va teskari matritsasini (inv) hisoblang.",
                        "Oddiy Python sikllari bilan NumPy tezligini solishtiruvchi kichik test yozing."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 3, "youtube_id": "vmEHCJofslg",
                "title": "3-Dars: Pandas Kutubxonasi: Ma'lumotlarni Qayta Ishlash va Tozalash",
                "channel": "freeCodeCamp.org",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "Pandas Series va DataFrame, CSV va Excel fayllarni o'qish, bo'sh qiymatlarni (NaN) tozalash, filtrlash, guruhlash (groupby) va birlashtirish.",
                "homework": {
                    "title": "3-Dars Vazifasi: Real Datasetni Tozalash va Tahlil Qilish",
                    "objective": "Pandas yordamida real jadval ma'lumotlarini tozalab, biznes tahlil tayyorlash.",
                    "tasks": [
                        "CSV formatdagi datasetni (masalan savdo yoki kadrlar) DataFrame ga yuklang.",
                        "Mavjud bo'sh (null/NaN) qiymatlarni aniqlab, ularni to'ldiring yoki o'chiring.",
                        "Kategoriyalar bo'yicha guruhlab (groupby), o'rtacha ko'rsatkichlarni hisoblang.",
                        "Tozalangan yangi ma'lumotlarni 'tozalangan_dataset.csv' fayliga saqlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 4, "youtube_id": "3Xc3CA655Y4",
                "title": "4-Dars: Ma'lumotlarni Vizualizatsiya Qilish: Matplotlib va Seaborn",
                "channel": "freeCodeCamp.org",
                "duration": "1:10:00", "completed": False, "active": False,
                "desc": "Ma'lumotlar vizualizatsiyasi, Matplotlib (plot, bar, scatter, hist) va Seaborn kutubxonasida taqsimot grafiklari va issiqlik xaritalari (heatmap).",
                "homework": {
                    "title": "4-Dars Vazifasi: Grafik Tahlil va Korrelyatsiya Xaritasi",
                    "objective": "Ma'lumotlar to'plami bo'yicha tushunarli grafiklar va korrelyatsiya xaritasini chizish.",
                    "tasks": [
                        "Ma'lumotlarning taqsimot gistogrammasi va quti grafigini (boxplot) chizing.",
                        "Ikkita muhim ko'rsatkich o'rtasidagi bog'liqlikni nuqtali grafikda (scatterplot) ko'rsating.",
                        "Ustunlar o'rtasidagi korrelyatsiya matritsasini Seaborn heatmap bilan tasvirlang.",
                        "Grafiklarga sarlavha, o'q belgilari va tushuntirishlarni (legend) to'g'ri joylang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 5, "youtube_id": "i_LwzRVP7bg",
                "title": "5-Dars: Mashinali O'rganishga Kirish: Chiziqli Regressiya (Linear Regression)",
                "channel": "StatQuest with Josh Starmer",
                "duration": "1:05:00", "completed": False, "active": False,
                "desc": "Nazorat ostida o'rganish (Supervised Learning), Regressiya mohiyati, Xarajat funksiyasi (Cost Function), Train/Test bo'linishi va Scikit-Learn.",
                "homework": {
                    "title": "5-Dars Vazifasi: Narxni Bashorat Qiluvchi Regressiya Modeli",
                    "objective": "Scikit-Learn yordamida chiziqli regressiya modelini o'qitish va baholash.",
                    "tasks": [
                        "Ma'lumotlarni train (80%) va test (20%) qismlarga ajrating.",
                        "LinearRegression modelini o'qiting (model.fit).",
                        "Test to'plamidagi narxlarni bashorat qiling (model.predict).",
                        "Model sifatini MAE, MSE va R2-Score ko'rsatkichlari bilan baholang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 6, "youtube_id": "gKZq17_iFOU",
                "title": "6-Dars: Klassifikatsiya Modellari: Logistic Regression va Random Forest",
                "channel": "freeCodeCamp.org",
                "duration": "1:20:00", "completed": False, "active": False,
                "desc": "Klassifikatsiya vazifalari, Logistik regressiya, Qarorlar daraxti (Decision Trees), Random Forest va baholash metrikalari (Accuracy, F1-Score).",
                "homework": {
                    "title": "6-Dars Vazifasi: Mijozlar Harakatini Bashorat Qiluvchi Model",
                    "objective": "Klassifikatsiya modelini qurish va Confusion Matrix orqali baholash.",
                    "tasks": [
                        "Klassifikatsiya datasetini yuklab, xususiyatlar (X) va nishonni (y) ajrating.",
                        "LogisticRegression va RandomForestClassifier modellarini o'qiting.",
                        "Ikkala modelning aniqligini (Accuracy va F1-score) o'zaro solishtiring.",
                        "Confusion Matrix chizmasi orqali xatoliklarni tahlil qiling."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 7, "youtube_id": "4b5d3muPQmA",
                "title": "7-Dars: Nazoratsiz O'rganish: K-Means Klasterlash va PCA",
                "channel": "StatQuest with Josh Starmer",
                "duration": "1:00:00", "completed": False, "active": False,
                "desc": "Nazoratsiz o'rganish (Unsupervised Learning), K-Means algoritmi, Optimal klasterlar sonini topish (Elbow Method) va PCA o'lcham qisqartirish.",
                "homework": {
                    "title": "7-Dars Vazifasi: Mijozlarni Segmentlarga (Klasterlarga) Ajratish",
                    "objective": "K-Means orqali ma'lumotlarni o'xshash guruhlarga ajratish va xulosalar chiqarish.",
                    "tasks": [
                        "Datasetdagi sonli parametrlarni StandardScaler yordamida normallang.",
                        "Elbow metodidan foydalanib eng maqbul klasterlar sonini (k) aniqlang.",
                        "KMeans modelini o'qitib, har bir satrga klaster yorlig'ini bering.",
                        "Ajratilgan klasterlarni 2D tekislikda turli ranglarda vizualizatsiya qiling."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 8, "youtube_id": "aircAruvnKk",
                "title": "8-Dars: Sun'iy Neyron Tarmoqlari Asoslari va Chuqur O'rganish (Deep Learning)",
                "channel": "3Blue1Brown",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "Neyronlar arxitekturasi, Ko'p qatlamli perseptron (MLP), Faollashtirish funksiyalari (Sigmoid, ReLU, Softmax) va Gradient tushishi.",
                "homework": {
                    "title": "8-Dars Vazifasi: Oddiy Neyron Tarmog'ini Qurish",
                    "objective": "Neyron tarmog'ining ishlash mexanizmini tushunish va faollashtirish funksiyalarini yozish.",
                    "tasks": [
                        "Sigmoid va ReLU funksiyalarini hamda ularning hosilalarini Pythonda yozing.",
                        "Kichik 2 qatlamli neyron tarmog'i uchun oldinga uzatish (forward propagation) kodini yozing.",
                        "Xatolik (Loss) qanday hisoblanishini matematik misolda tushuntiring.",
                        "Kodingizni izohlar bilan .py formatida taqdim eting."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 9, "youtube_id": "tPYj3fFJGjk",
                "title": "9-Dars: TensorFlow va Keras: Tasvirlarni Tanish (CNN)",
                "channel": "freeCodeCamp.org",
                "duration": "1:30:00", "completed": False, "active": False,
                "desc": "TensorFlow va Keras freymvorki, Konvolyutsion neyron tarmoqlar (CNN), Qatlamlar (Conv2D, MaxPooling2D, Flatten, Dense) va MNIST tasvirlarni tanish.",
                "homework": {
                    "title": "9-Dars Vazifasi: Qo'lyozma Raqamlarni Taniydigan CNN Modeli",
                    "objective": "Keras yordamida CNN modelini qurish va 98%+ aniqlikda o'qitish.",
                    "tasks": [
                        "MNIST raqamlar datasetini yuklang va piksellar qiymatini 0-1 oralig'iga keltiring.",
                        "Conv2D, MaxPooling2D va Dense qatlamlaridan iborat CNN modelini tuzing.",
                        "Modelni kamida 5 ta davr (epochs) davomida o'qiting.",
                        "Test to'plamida model aniqligini (test accuracy) 98% dan yuqori natijaga chiqaring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 10, "youtube_id": "M9Itm95JzL0",
                "title": "10-Dars: NLP Asoslari, LLM lar va AI Modelni API Orqali Deploy Qilish",
                "channel": "freeCodeCamp.org",
                "duration": "1:35:00", "completed": False, "active": False,
                "desc": "Tabiiy tilni qayta ishlash (NLP), Tokenizatsiya, Katta til modellari (LLM) tushunchasi, FastAPI yordamida AI modelni veb-servis ko'rinishida deploy qilish.",
                "homework": {
                    "title": "10-Dars Vazifasi: FastAPI Yordamida AI API Servisini Yaratish",
                    "objective": "O'qitilgan ML/AI modelni FastAPI orqali REST API endpointga aylantirish va ishga tushirish.",
                    "tasks": [
                        "O'qitilgan modelni faylga saqlang (joblib yoki pickle orqali).",
                        "FastAPI da yangi POST /predict endpointini yarating.",
                        "JSON orqali kelgan kiruvchi parametrlarni modelga uzatib, natijani qaytaring.",
                        "Swagger UI (/docs) orqali so'rov yuborib model natijasini tekshiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            }
        ]
    },
    'mobile-dev': {
        'title': 'Mobil Dasturlash (Flutter)',
        'icon': 'mobile-screen',
        'color': '#10b981',
        'videos': [
            {
                "id": 1, "youtube_id": "Ej_PCr45644",
                "title": "1-Dars: Dart Dasturlash Tiliga Kirish va Sintaksis",
                "channel": "freeCodeCamp.org",
                "duration": "50:00", "completed": False, "active": True,
                "desc": "Dart tiliga kirish, DartPad bilan ishlash, o'zgaruvchilar (var, int, double, String, bool), shart operatorlari va asosiy funksiyalar.",
                "homework": {
                    "title": "1-Dars Vazifasi: Konsol Kalkulyatori va Konverter",
                    "objective": "Dart sintaksisi, tiplash va funksiyalardan foydalanib konsol dasturi tuzish.",
                    "tasks": [
                        "Valyuta konvertori (USD dan UZS ga) hisoblovchi funksiya yozing.",
                        "Ikki son ustida arifmetik amallarni bajaruvchi kalkulyator yozing.",
                        "Null-safety qoidalariga rioya qiling (String?, int?).",
                        "Natijalarni konsolda toza formatda chiqaring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 2, "youtube_id": "1ukSR1SXt6M",
                "title": "2-Dars: Dart Tilida Obyektga Yo'naltirilgan Dasturlash (OOP)",
                "channel": "freeCodeCamp.org",
                "duration": "1:00:00", "completed": False, "active": False,
                "desc": "Dart tilida klasslar, konstruktorlar (Named constructors), merosxo'rlik (extends), abstrakt klasslar (abstract), interfeyslar va mixinlar.",
                "homework": {
                    "title": "2-Dars Vazifasi: Bank Tizimi Klasslari (Dart OOP)",
                    "objective": "Dart klasslari, vorislik va konstruktorlar yordamida bank ilovasi modelini tuzish.",
                    "tasks": [
                        "'BankAccount' klassini (accountNumber, balance, owner) yarating.",
                        "Mablag' qo'shish (deposit) va yechish (withdraw) metodlarini xavfsiz shartlar bilan yozing.",
                        "'PremiumAccount' voris klassini yaratib, keshbek funksiyasini qo'shing.",
                        "Kamida 2 ta bank hisobini yaratib, natijalarni sinovdan o'tkazing."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 3, "youtube_id": "1gDhl4leEzA",
                "title": "3-Dars: Flutter Frameworkga Kirish va Loyiha Arxitekturasi",
                "channel": "freeCodeCamp.org",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "Flutter SDK, Android Studio va VS Code sozlamalari, Loyiha kataloglari, main.dart, MaterialApp, Scaffold va Hot Reload imkoniyatlari.",
                "homework": {
                    "title": "3-Dars Vazifasi: Shaxsiy Vizitka (Business Card) Mobil Ilovasi",
                    "objective": "MaterialApp va Scaffold vidjetlari yordamida ilk mobil interfeysni terish.",
                    "tasks": [
                        "Yangi Flutter loyihasi ishga tushiring va keraksiz koddarni tozalang.",
                        "Scaffold ichida AppBar, markaziy rasm (profil fotosi) va matnlarni joylang.",
                        "Shriftlar va ranglarni zamonaviy dizaynda sozlang.",
                        "Ilovani emulyator yoki real telefonda ishga tushirib skrinshot oling."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 4, "youtube_id": "pTJJsmejUOQ",
                "title": "4-Dars: Asosiy Vidjetlar: Row, Column, Container va Stack",
                "channel": "HeyFlutter",
                "duration": "1:05:00", "completed": False, "active": False,
                "desc": "Flutterda maketlar qurish: Row va Column parametrlari (mainAxisAlignment, crossAxisAlignment), Container, BoxDecoration, Padding va Stack/Positioned.",
                "homework": {
                    "title": "4-Dars Vazifasi: Zamonaviy Profil Sahifasi Maketi",
                    "objective": "Row, Column va Container vidjetlarini to'g'ri joylashtirib chiroyli profil ekrani tuzish.",
                    "tasks": [
                        "Profil rasmi, ism, kasb va statistika bloklarini (obunachilar, layklar) quring.",
                        "Container yordamida burchaklari yumaloq (borderRadius) va soyali (boxShadow) kartochka yarating.",
                        "Row yordamida statistik ko'rsatkichlarni teng masofada joylashtiring.",
                        "Turli ekran o'lchamlari uchun mos kelishini ta'minlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 5, "youtube_id": "GLSG_Wh_YWc",
                "title": "5-Dars: Stateless va Stateful Vidjetlar, Interaktivlik va Formalar",
                "channel": "freeCodeCamp.org",
                "duration": "1:10:00", "completed": False, "active": False,
                "desc": "Stateless va Stateful farqi, setState() mexanizmi, Tugmalar (ElevatedButton, IconButton), TextField, TextEditingController va forma validatsiyasi.",
                "homework": {
                    "title": "5-Dars Vazifasi: Interaktiv Ro'yxatdan O'tish Formasi",
                    "objective": "StatefulWidget va forma boshqaruvi orqali foydalanuvchi ma'lumotlarini qabul qilish.",
                    "tasks": [
                        "Ism, email va parol kiritish uchun TextField larni yarating.",
                        "Parolni ko'rish/yashirish uchun ko'zcha (IconButton) tugmasini setState orqali boshqaring.",
                        "Email formati to'g'riligini tekshiruvchi validatsiya qo'shing.",
                        "Tugma bosilganda kiritilgan ma'lumotlarni chiroyli dialog oynada ko'rsating."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 6, "youtube_id": "b_sQ9bMltmg",
                "title": "6-Dars: Ro'yxatlar Bilan Ishlash: ListView va GridView",
                "channel": "The Net Ninja",
                "duration": "1:05:00", "completed": False, "active": False,
                "desc": "Katta hajmdagi ma'lumotlarni ko'rsatish, ListView.builder xotira optimizatsiyasi, ListTile vidjeti, Card va GridView.builder orqali to'rsimon maketlar.",
                "homework": {
                    "title": "6-Dars Vazifasi: Mahsulotlar Katalogi Ro'yxati",
                    "objective": "ListView.builder va GridView yordamida dinamik katalog sahifasini qurish.",
                    "tasks": [
                        "Kamida 10 ta mahsulot ma'lumotlaridan iborat ro'yxat (List<Map>) tuzing.",
                        "ListView.builder yordamida ro'yxatni samarali (lazy loading) ko'rinishda chizing.",
                        "Har bir element uchun rasm, nom, narx va 'Xarid' tugmasini joylang.",
                        "GridView orqali 2 ustunli ko'rinishga o'tkazish imkonini qo'shing."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 7, "youtube_id": "2U_w-Jc_99c",
                "title": "7-Dars: Navigatsiya va Marshrutlash (Navigation & Routing)",
                "channel": "The Net Ninja",
                "duration": "1:00:00", "completed": False, "active": False,
                "desc": "Sahifalar o'rtasida o'tish (Navigator.push, Navigator.pop), Named Routes (nomlangan yo'llar), sahifadan sahifaga parametr va obyekt uzatish.",
                "homework": {
                    "title": "7-Dars Vazifasi: Ko'p Sahifali Ilova va Detal Ekranlari",
                    "objective": "Navigator yordamida ro'yxatdan detal sahifasiga o'tish va orqaga qaytishni tashkil qilish.",
                    "tasks": [
                        "Bosh sahifa va Mahsulot Detali sahifalarini yarating.",
                        "Ro'yxatdagi element bosilganda uning to'liq ma'lumotlarini detal ekraniga uzating.",
                        "Detal ekranida to'liq tavsif, katta rasm va orqaga qaytish tugmasini sozlang.",
                        "Navigator.pop orqali natija qaytarish mexanizmini qo'llang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 8, "youtube_id": "kG6Wz1gU8aA",
                "title": "8-Dars: REST API va JSON Bilan Ishlash (HTTP So'rovlar)",
                "channel": "Johannes Milke",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "Flutterda internet bilan ishlash, http paketi, Asinxron dasturlash (Future, async/await), JSON ma'lumotlarni modelga aylantirish (fromJson) va FutureBuilder.",
                "homework": {
                    "title": "8-Dars Vazifasi: Real Vaqt Yangiliklar yoki Ob-havo Ilovasi",
                    "objective": "Tashqi REST API dan ma'lumot yuklab, FutureBuilder yordamida mobil ekranda ko'rsatish.",
                    "tasks": [
                        "Ochiq API dan (masalan NewsAPI yoki JSONPlaceholder) ma'lumot olish funksiyasini yozing.",
                        "JSON ma'lumotlar uchun maxsus Dart model klassini (factory fromJson) yarating.",
                        "FutureBuilder yordamida yuklanish jarayonida CircularProgressIndicator ko'rsating.",
                        "Xatolik yuz berganda ekranga tushunarli xatolik xabarini chiqaring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 9, "youtube_id": "d_m5cSmep7A",
                "title": "9-Dars: Holat Boshqaruvi: Provider Arxitekturasi",
                "channel": "freeCodeCamp.org",
                "duration": "1:25:00", "completed": False, "active": False,
                "desc": "Global holat boshqaruvi zarurati, Provider kutubxonasi, ChangeNotifier, MultiProvider, Consumer va context.watch/read metodlari.",
                "homework": {
                    "title": "9-Dars Vazifasi: Do'kon Savatchasi Holatini Boshqarish",
                    "objective": "Provider yordamida xarid savatchasiga tovar qo'shish va hisob-kitobni global boshqarish.",
                    "tasks": [
                        "CartProvider nomli ChangeNotifier klassini yarating.",
                        "Savatchaga mahsulot qo'shish, sonini oshirish/kamaytirish va umumiy narxni hisoblash metodlarini yozing.",
                        "MultiProvider orqali ilova ildiziga provayderni ulang.",
                        "Consumer orqali savatchadagi tovarlar sonini istalgan ekranda real vaqtda ko'rsating."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 10, "youtube_id": "3a_mQZ4lV4w",
                "title": "10-Dars: Mahalliy Xotira (Hive/SharedPreferences) va Release APK Build",
                "channel": "HeyFlutter",
                "duration": "1:30:00", "completed": False, "active": False,
                "desc": "Ilova ma'lumotlarini telefonda saqlash (SharedPreferences / Hive), Ilova ikonkasini sozlash (flutter_launcher_icons) va Release APK/AAB kompilyatsiyasi.",
                "homework": {
                    "title": "10-Dars Vazifasi: Offline Todo Ilova va Release APK Chiqarish",
                    "objective": "Ma'lumotlari telefon xotirasida saqlanib qoluvchi ilovani tayyorlash va APK formatida yig'ish.",
                    "tasks": [
                        "SharedPreferences yoki Hive yordamida vazifalar ro'yxatini mahalliy xotirada saqlang.",
                        "Ilova yopilib qayta ochilganda saqlangan vazifalar avtomatik tiklansin.",
                        "Ilovaga chiroyli shaxsiy app icon o'rnating.",
                        "'flutter build apk --release' buyrug'i orqali tayyor o'rnatiluvchi APK faylini hosil qiling."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            }
        ]
    },
    'ui-ux-design': {
        'title': 'UI/UX Dizayn',
        'icon': 'palette',
        'color': '#f59e0b',
        'videos': [
            {
                "id": 1, "youtube_id": "c9Wg6Cb_YlU",
                "title": "1-Dars: UI/UX Dizaynga Kirish va Figma Asoslari",
                "channel": "freeCodeCamp.org",
                "duration": "55:00", "completed": False, "active": True,
                "desc": "UI (User Interface) va UX (User Experience) farqi, Figma interfeysi, Freymlar (Frames), Shakllar (Shapes), Matn vositalari va asosiy qoidalar.",
                "homework": {
                    "title": "1-Dars Vazifasi: Figma-da Ilk Mobil Ekran Eskizi",
                    "objective": "Figma vositalaridan foydalanib mobil ilovaning boshlang'ich vizual maketini yaratish.",
                    "tasks": [
                        "iPhone yoki Android o'lchamida yangi Freym (Frame) oching.",
                        "Asosiy geometrik shakllar yordamida rasm, sarlavha va tugma joylarini chizing.",
                        "Qatlamlar (Layers) panelida har bir elementni to'g'ri nomlang.",
                        "Figma faylingizning ommaviy ko'rish havolasini (view link) topshiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 2, "youtube_id": "i67h3VnU_v4",
                "title": "2-Dars: Tipografika va Ranglar Nazariyasi (Color Theory)",
                "channel": "Flux Academy",
                "duration": "1:00:00", "completed": False, "active": False,
                "desc": "Tipografik ierarxiya (H1-H6, Body), Shriftlar juftligi, Ranglar psixologiyasi, 60-30-10 qoidasi va kontrastlik standartlari (WCAG).",
                "homework": {
                    "title": "2-Dars Vazifasi: Ranglar Palitrasi va Tipografik Qo'llanma",
                    "objective": "Loyiha uchun uyg'un ranglar palitrasi va aniq tipografiya tizimini ishlab chiqish.",
                    "tasks": [
                        "Asosiy (Primary), ikkilamchi (Secondary) va neytral ranglardan iborat palitra tuzing.",
                        "WCAG kontrasti bo'yicha matn va fon o'rtasida kamida 4.5:1 kontrastni ta'minlang.",
                        "Sarlavhalar va asosiy matn uchun shrift o'lchamlari shkalasini (Typographic Scale) belgilang.",
                        "Palitraning Figma uslublarini (Color Styles) yarating."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 3, "youtube_id": "dFszhB_i2y0",
                "title": "3-Dars: Layout Grids, Spacing va 8pt Kompozitsiya Qoidalari",
                "channel": "Mizko",
                "duration": "1:05:00", "completed": False, "active": False,
                "desc": "Setkalar bilan ishlash (Layout Grids: 4-column, 12-column), 8pt spacing qoidasi, Oq bo'shliq (White space) va vizual muvozanat.",
                "homework": {
                    "title": "3-Dars Vazifasi: 8pt Setka Asosida Landing Page Bloki",
                    "objective": "8-pikselli setka tizimiga qat'iy amal qilib veb-sahifa bloklarini joylashtirish.",
                    "tasks": [
                        "12 ustunli veb setkani (Grid: 12 columns, gutter: 24px) sozlang.",
                        "Barcha oraliq masofalarni (padding, margin) 8 ning karralilari (8, 16, 24, 32, 48px) qilib belgilang.",
                        "Kartochkalar va matn bloklarini setka chiziqlari bo'yicha to'g'rilang.",
                        "Elementlar orasidagi havo (oq bo'shliq) qoidalariga rioya qiling."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 4, "youtube_id": "NrKX46DzkGQ",
                "title": "4-Dars: Figma Auto Layout va Moslashuvchan (Responsive) Dizayn",
                "channel": "DesignCourse",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "Figma Auto Layout imkoniyatlari (Shift+A), Direction (Vertical, Horizontal), Hug, Fill, Fixed, Padding va Gap parametrlari.",
                "homework": {
                    "title": "4-Dars Vazifasi: Dinamik Moslashuvchan Tugma va Kartochkalar",
                    "objective": "Auto Layout yordamida matn o'zgarganda hajmi avtomatik moslashuvchi komponentlar yaratish.",
                    "tasks": [
                        "Matn uzunligiga qarab avtomatik kengayuvchi Auto Layout tugmasini yarating.",
                        "Rasm, matn va tugmadan iborat kartochkani vertikal Auto Layout yordamida yiging.",
                        "Kartochka ichki elementlariga 'Fill container' xususiyatini bering.",
                        "Freym o'lchami cho'zilganda elementlar buzilmasdan moslashishini tekshiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 5, "youtube_id": "e_p_pMhD-eA",
                "title": "5-Dars: Komponentlar va Variantlar (Components & Variants)",
                "channel": "Figma",
                "duration": "1:10:00", "completed": False, "active": False,
                "desc": "Master komponentlar, Nusxalar (Instances), Variantlar yaratish, Component Properties (Boolean, Instance swap, Text) va dizayn tezligi.",
                "homework": {
                    "title": "5-Dars Vazifasi: To'liq Interaktiv Tugmalar To'plami (Button Set)",
                    "objective": "Variantlar va xususiyatlar (Component Properties) yordamida to'liq tugmalar komponentini tuzish.",
                    "tasks": [
                        "Bitta tugmadan Master Component hosil qiling.",
                        "Holatlar bo'yicha variantlarni (Default, Hover, Pressed, Disabled) yarating.",
                        "Hajmlar bo'yicha variantlarni (Small, Medium, Large) qo'shing.",
                        "Ikonkani yoqish/o'chirish uchun Boolean property qo'shing."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 6, "youtube_id": "zbL_Z7kLg3o",
                "title": "6-Dars: UX Tadqiqot, Foydalanuvchi Personasi va User Journey Map",
                "channel": "CareerFoundry",
                "duration": "1:05:00", "completed": False, "active": False,
                "desc": "UX tadqiqot usullari, Foydalanuvchi intervyulari, User Persona yaratish, Empathy Mapping va User Journey (Foydalanuvchi yo'li) xaritasi.",
                "homework": {
                    "title": "6-Dars Vazifasi: Yangi Ilova Uchun Foydalanuvchi Personasi",
                    "objective": "Maqsadli auditoriyani o'rganib, real ehtiyojlarga asoslangan Personani shakllantirish.",
                    "tasks": [
                        "Muayyan loyiha (masalan kitob do'koni ilovasi) uchun 1 ta to'liq User Persona tuzing.",
                        "Personaning maqsadlari, og'riqli nuqtalari (pain points) va texnik ko'nikmalarini yozing.",
                        "Foydalanuvchining ilovaga kirishidan mahsulot sotib olishigacha bo'lgan qadamlar xaritasini (User Journey) chizing.",
                        "Xulosa va dizayn tavsiyalarini matn ko'rinishida keltiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 7, "youtube_id": "2U5f2Q7F6uI",
                "title": "7-Dars: Axborot Arxitekturasi va Wireframing (Past/Yuqori Aniqlik)",
                "channel": "AJ&Smart",
                "duration": "1:10:00", "completed": False, "active": False,
                "desc": "Axborot arxitekturasi (Information Architecture), Sayt xaritasi (Sitemap), Low-fidelity (eskiz) va High-fidelity wireframelar yaratish.",
                "homework": {
                    "title": "7-Dars Vazifasi: Mobil Ilovaning 5 Ta Asosiy Wireframe Ekrani",
                    "objective": "Dizayn detallariga chalg'imasdan foydalanuvchi tajribasi tuzilmasini wireframeda ko'rsatish.",
                    "tasks": [
                        "Ilovaning 5 ta asosiy ekrani (Splash, Login, Home, Qidiruv, Profil) uchun wireframe chizing.",
                        "Faqat oq-qora va kulrang tonlardan foydalaning.",
                        "Navigatsiya ierarxiyasi va tugmalar joylashuvi qulayligiga e'tibor bering.",
                        "Ekranlar orasidagi o'zaro mantiqiy bog'liqlikni izohlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 8, "youtube_id": "aI8P65xYqgA",
                "title": "8-Dars: Dizayn Tizimlari (Design System) va UI Kitlar",
                "channel": "DesignCourse",
                "duration": "1:20:00", "completed": False, "active": False,
                "desc": "Design System tushunchasi, Dizayn tokenlari (Tokens), Ranglar va shriftlar kutubxonasi, Ikonkalar to'plami va UI Kit yaratish.",
                "homework": {
                    "title": "8-Dars Vazifasi: Mini Design System Hujjatlash",
                    "objective": "Loyiha uchun qayta ishlatiluvchi to'liq dizayn tizimini shakllantirish.",
                    "tasks": [
                        "Figma faylida alohida 'Design System' sahifasini oching.",
                        "Ranglar palitrasi, shrift stillari, burchak radiuslari va soyalarni tizimlashtiring.",
                        "Tugmalar, inputlar, yorliqlar (badges) va kartochkalar komponentlarini joylang.",
                        "Barcha stillarni Figma Style library sifatida saqlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 9, "youtube_id": "k16U5F7aI8M",
                "title": "9-Dars: Interaktiv Prototip Yaratish va Smart Animate",
                "channel": "Figma",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "Figma prototiplash vositalari, Triggers (On click, While hovering), Transitions (Instant, Dissolve, Smart Animate) va jonli taqdimot.",
                "homework": {
                    "title": "9-Dars Vazifasi: Jonli Bosiluvchi Mobil Prototip",
                    "objective": "Ekranlar o'rtasida real ilovadek ishlovchi interaktiv prototipni ulab chiqish.",
                    "tasks": [
                        "Kamida 4 ta ekranni prototip chiziqlari bilan o'zaro bog'lang.",
                        "Ochiluvchi menyu (modal yoki drawer) uchun 'Open Overlay' animatsiyasini qo'llang.",
                        "Smart Animate yordamida sahifalar o'rtasida silliq o'tish effektini bering.",
                        "Figma Mirror yoki prototip havolasi orqali to'liq ishlayotganini tekshiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 10, "youtube_id": "z_vH5oG3_6w",
                "title": "10-Dars: Usability Testing va Figma Dev Mode Bilan Ishlash",
                "channel": "Figma",
                "duration": "1:25:00", "completed": False, "active": False,
                "desc": "Foydalanish qulayligi testi (Usability Testing), Foydalanuvchi fikr-mulohazalari tahlili, Figma Dev Mode, CSS eksport va dasturchilarga topshirish.",
                "homework": {
                    "title": "10-Dars Vazifasi: Tayyor Dizayn Loyihasini Dasturchilarga Topshirish",
                    "objective": "Dizaynni ishlab chiqishga to'liq tayyorlab hujjatlashtirish va portfolio taqdimoti tuzish.",
                    "tasks": [
                        "Dev Mode orqali o'lchamlar, oraliq masofalar va shriftlarni dasturchi uchun tekshiring.",
                        "Barcha rasm va ikonkalar uchun SVG/PNG eksport parametrlarini sozlang.",
                        "Dizaynga qo'shimcha sharhlar (Developer Notes) yozib qoldiring.",
                        "Behance yoki Dribbble uchun chiroyli mokap (mockup) taqdimotini tayyorlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            }
        ]
    },
    'kiberxavfsizlik': {
        'title': 'Kiberxavfsizlik',
        'icon': 'shield-halved',
        'color': '#ef4444',
        'videos': [
            {
                "id": 1, "youtube_id": "z5nc9MDbvkw",
                "title": "1-Dars: Kiberxavfsizlikka Kirish va Axborot Xavfsizligi Asoslari",
                "channel": "freeCodeCamp.org",
                "duration": "55:00", "completed": False, "active": True,
                "desc": "Kiberxavfsizlik tushunchasi, CIA Triadasi (Maxfiylik, Butunlik, Foydalanishga ochiqlik), Xakerlik turlari (Oq, Qora, Kulrang) va tahdidlar.",
                "homework": {
                    "title": "1-Dars Vazifasi: CIA Triadasi va Xavfsizlik Siyosati Tahlili",
                    "objective": "Axborot xavfsizligining asosiy tamoyillarini o'rganib, tashkiliy xavfsizlik tahlilini tuzish.",
                    "tasks": [
                        "CIA Triadasining 3 ta ustuniga (Confidentiality, Integrity, Availability) real misollar keltiring.",
                        "Parol xavfsizligi qoidalari (uzunlik, murakkablik, 2FA) bo'yicha talablar yozing.",
                        "Tashkilot xodimlari uchun 5 ta asosiy kibergigiyena qoidalarini shakllantiring.",
                        "Tahlilni xulosa ko'rinishida topshiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 2, "youtube_id": "IPvYjXCsTg8",
                "title": "2-Dars: Kompyuter Tarmoqlari: TCP/IP, OSI Modeli va Protokollar",
                "channel": "freeCodeCamp.org",
                "duration": "1:10:00", "completed": False, "active": False,
                "desc": "Tarmoq arxitekturasi, OSI modelining 7 qatlami, TCP/IP steki, IP manzillash, Portlar, DNS, DHCP va xavfsiz protokollar (HTTPS, SSH).",
                "homework": {
                    "title": "2-Dars Vazifasi: Tarmoq Protokollari va Portlar Tahlili",
                    "objective": "Tarmoq qatlamlari va eng ko'p hujumga uchraydigan portlar xavfsizligini tekshirish.",
                    "tasks": [
                        "OSI modelining har bir qatlamini va unga mos protokollarni tavsiflang.",
                        "Eng mashhur 10 ta portni (21, 22, 25, 53, 80, 443 va h.k.) va ularning vazifasini yozing.",
                        "HTTP va HTTPS o'rtasidagi shifrlash farqini tushuntiring.",
                        "Wireshark orqali shifrlanmagan va shifrlangan paketlar ko'rinishini taqqoslang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 3, "youtube_id": "sWbUDq4S6Y8",
                "title": "3-Dars: Linux Operatsion Tizimi va Kiberxavfsizlikda Buyruqlar Satri",
                "channel": "NetworkChuck",
                "duration": "1:05:00", "completed": False, "active": False,
                "desc": "Linux (Kali / Ubuntu) muhiti, Fayl tizimi tuzilishi, Foydalanuvchi huquqlari (chmod, chown), Bash buyruqlari va xavfsizlik auditi skriptlari.",
                "homework": {
                    "title": "3-Dars Vazifasi: Linuxda Xavfsizlik Auditi Bash Skripti",
                    "objective": "Linux tizimida xavfsizlik tekshiruvlarini avtomatlashtiruvchi Bash skripti yozish.",
                    "tasks": [
                        "Tizimda root huquqiga ega foydalanuvchilar ro'yxatini chiqaruvchi buyruq yozing.",
                        "Tizimdagi barcha ochiq tarmoq ulanishlarini (netstat / ss) tekshiruvchi buyruqni qo'shing.",
                        "Fayl huquqlari 777 bo'lgan xavfli fayllarni qidiruvchi find buyrug'ini yozing.",
                        "Ushbu buyruqlarni bitta 'audit.sh' skriptiga jamlab, natijasini faylga saqlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 4, "youtube_id": "jhXCTbFnK8o",
                "title": "4-Dars: Kriptografiya Asoslari: Shifrlash, Xeshlar va Raqamli Imzolar",
                "channel": "freeCodeCamp.org",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "Simmetrik shifrlash (AES), Asimmetrik shifrlash (RSA), Xeshlash algoritmlari (SHA-256, MD5), Salt mexanizmi va Raqamli sertifikatlar (SSL/TLS).",
                "homework": {
                    "title": "4-Dars Vazifasi: Python Kriptografik Dasturi",
                    "objective": "Pythonda xeshlash va ma'lumotlarni shifrlash modullari bilan ishlash.",
                    "tasks": [
                        "Python hashlib kutubxonasi yordamida matnning SHA-256 xeshini hisoblang.",
                        "Parollarni saqlashda nima uchun salt kerakligini dasturiy misolda ko'rsating.",
                        "Fernet (kriptografiya) moduli orqali maxfiy matnni shifrlang va kalit bilan qayta oching.",
                        "Xeshning qaytmaslik (bir tomonlama) xususiyatini tushuntiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 5, "youtube_id": "1pDfx_3gQ6Q",
                "title": "5-Dars: Ochiq Manbalardan Qidiruv (OSINT) va Axborot To'plash",
                "channel": "freeCodeCamp.org",
                "duration": "1:00:00", "completed": False, "active": False,
                "desc": "OSINT (Open Source Intelligence) metodologiyasi, Footprinting, Google Dorking operatorlari, Whois, Shodan qidiruv tizimi va domen auditi.",
                "homework": {
                    "title": "5-Dars Vazifasi: Ochiq Manbalardan Xavfsizlik Auditi (OSINT)",
                    "objective": "Faqat qonuniy va ochiq manbalar orqali domen xavfsizligi bo'yicha tahliliy hisobot tayyorlash.",
                    "tasks": [
                        "Google Dorking operatorlaridan (site:, filetype:, inurl:) foydalanib ochiq hujjatlarni qidirish misolini keltiring.",
                        "Whois va DNS ma'lumotlarini (NS, MX, TXT yozuvlari) tekshirib tahlil qiling.",
                        "Shodan qidiruv tizimi imkoniyatlari va xavfli ochiq qurilmalarni qanday topishini tushuntiring.",
                        "Topilgan ma'lumotlarni umumlashtirib OSINT hisoboti shaklida topshiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 6, "youtube_id": "4t4kBkMsDbQ",
                "title": "6-Dars: Tarmoq Skanerlash (Nmap) va Zaifliklarni Aniqlash",
                "channel": "NetworkChuck",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "Tarmoq skanerlash tamoyillari, Nmap vositasi, SYN Scan, TCP Connect, Servislar va operatsion tizimni aniqlash (-sV, -O) hamda Nmap Scripting Engine (NSE).",
                "homework": {
                    "title": "6-Dars Vazifasi: Nmap Bilan Tarmoq Skanerlash Amaliyoti",
                    "objective": "Maxsus ruxsat etilgan test serverini (scanme.nmap.org) Nmap orqali skanerlash va natijalarni tahlil qilish.",
                    "tasks": [
                        "scanme.nmap.org serverida ochiq portlarni aniqlovchi nmap so'rovini bajaring.",
                        "Servis versiyalarini (-sV) va tizim turini (-O) aniqlovchi parametrlar bilan skanerlang.",
                        "Ochiq portlar va ularda ishlayotgan servislar ro'yxatini jadval qilib yozing.",
                        "Keraksiz ochiq portlarning tashkilot xavfsizligiga xavfini tushuntiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 7, "youtube_id": "2_lswM1S264",
                "title": "7-Dars: Veb Ilovalar Zaifliklari: OWASP Top 10 va Himoya Usullari",
                "channel": "freeCodeCamp.org",
                "duration": "1:25:00", "completed": False, "active": False,
                "desc": "OWASP Top 10 ro'yxati, SQL Injection (SQLi), Cross-Site Scripting (XSS), Broken Authentication, CSRF hujumlari va xavfsiz dasturlash qoidalari.",
                "homework": {
                    "title": "7-Dars Vazifasi: SQL Injection va XSS Hujumlari Tahlili",
                    "objective": "Zaif kod misollarini ko'rib chiqish va ularni xavfsiz kod bilan almashtirish.",
                    "tasks": [
                        "SQL inyeksiyasiga zaif bo'lgan SQL so'rovini misol qilib yozing.",
                        "Ushbu zaiflikni Parametrlangan so'rovlar (Prepared Statements) orqali to'g'irlang.",
                        "XSS (Cross-Site Scripting) qanday sodir bo'lishini va foydalanuvchi cookie ma'lumotlarini qanday o'g'irlashini tushuntiring.",
                        "HTML-escape va CSP (Content Security Policy) orqali XSS dan himoyalanishni ko'rsating."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 8, "youtube_id": "lc7scxvKQOo",
                "title": "8-Dars: Ijtimoiy Muhandislik (Social Engineering) va Fishing Hujumlari",
                "channel": "IBM Technology",
                "duration": "1:00:00", "completed": False, "active": False,
                "desc": "Inson omili va ijtimoiy muhandislik, Fishing (Phishing), Smishing, Vishing, Pretexting hujumlari va korxonalarda kiber-xabardorlikni oshirish.",
                "homework": {
                    "title": "8-Dars Vazifasi: Korxona Xodimlari Uchun Fishingdan Himoyalanish Yo'riqnomasi",
                    "objective": "Hujumkor fishing xatlarini tahlil qilish va xodimlar uchun yo'riqnoma tayyorlash.",
                    "tasks": [
                        "Haqiqiy fishing xatlarining 5 ta asosiy belgisini (soxta domen, shoshiltirish, shubhali birikma) tahlil qiling.",
                        "Domen nomlarini almashtirish (Typosquatting) usulini tushuntiring.",
                        "Korxona xodimlari fishing xatiga duch kelganda nima qilishi kerakligi bo'yicha bosqichma-bosqich reja yozing.",
                        "2FA / MFA texnologiyasining fishingdan himoyadagi rolini tushuntiring."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 9, "youtube_id": "F50G7K7k9Y4",
                "title": "9-Dars: Xavfsizlik Devorlari (Firewalls), IDS/IPS va Incident Response",
                "channel": "freeCodeCamp.org",
                "duration": "1:15:00", "completed": False, "active": False,
                "desc": "Xavfsizlik devorlari (Firewall iptables/ufw), Hujumlarni aniqlash va oldini olish tizimlari (IDS/IPS: Snort/Suricata), Loglar auditi va insidentlarni boshqarish.",
                "homework": {
                    "title": "9-Dars Vazifasi: Linux UFW / iptables Xavfsizlik Qoidalari",
                    "objective": "Linux serverida xavfsizlik devorini sozlash va shubhali so'rovlarni bloklash.",
                    "tasks": [
                        "UFW yordamida barcha kiruvchi ulanishlarni bloklab, faqat SSH (22) va HTTPS (443) ga ruxsat bering.",
                        "Muayyan shubhali IP manzilni butunlay bloklovchi qoidani qo'shing.",
                        "Server log fayllarini (/var/log/auth.log) tahlil qilib, muvaffaqiyatsiz login urinishlarini aniqlang.",
                        "Fail2Ban vositasining brute-force hujumlaridan himoya qilish tamoyilini yozing."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            },
            {
                "id": 10, "youtube_id": "3Kq1MIfTWCE",
                "title": "10-Dars: Axborot Xavfsizligi Auditi, Pentest Hisoboti va Sertifikatlar",
                "channel": "David Bombal",
                "duration": "1:30:00", "completed": False, "active": False,
                "desc": "Penetration testing metodologiyalari, Zaifliklarni baholash (CVSS ballari), Rasmiy audit va Pentest hisoboti tayyorlash, CEH va CompTIA Security+ sertifikatlari.",
                "homework": {
                    "title": "10-Dars Vazifasi: Rasmiy Penetration Testing Hisobotini Tayyorlash",
                    "objective": "Bajarilgan zaifliklar tahlili bo'yicha rahbariyat va dasturchilar uchun professional hisobot tuzish.",
                    "tasks": [
                        "Rahbariyat uchun qisqacha xulosa (Executive Summary) bo'limini yozing.",
                        "Topilgan kamida 2 ta zaiflikni (masalan SQLi va Zaif Parol) CVSS ballari bilan tavsiflang.",
                        "Har bir zaiflikni bartaraf etish bo'yicha dasturchilarga aniq texnik tavsiyalar (Remediation) bering.",
                        "Hisobotni professional PDF/Word hujjati ko'rinishida formatlang."
                    ],
                    "deadline": "3 kun",
                    "max_score": "10 ball"
                }
            }
        ]
    }
}
