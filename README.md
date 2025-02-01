Medical Telegram Bot
Medical Telegram Bot - bu foydalanuvchilarga tibbiyot sohasida yordam berish uchun mo'ljallangan Telegram bot. Bot foydalanuvchilarga tibbiy maslahatlar, dori-darmonlar haqida ma'lumot, tibbiy tashkilotlar va xizmatlar bilan bog'lanish imkoniyatini taqdim etadi.

Asosiy xususiyatlar
Tibbiy maslahatlar: Foydalanuvchilar o'zlarining simptomlari yoki tibbiy savollarini kiritib, tavsiyalar olishlari mumkin.
Dori-darmonlar ma'lumotlari: Dori-darmonlar haqida umumiy ma'lumot va tavsiyalar.
Yaqin tibbiy xizmatlar: Yaqin atrofdagi shifoxonalar, dorixonalar va klinikalar bilan bog'lanish imkoniyati.
Foydalanuvchi profili: Foydalanuvchilar o'zlarining tibbiy ma'lumotlarini saqlash va tibbiy tarixni kuzatish imkoniga ega bo'lishadi.
Tezkor javoblar: Foydalanuvchilarga tez va aniq javoblar taqdim etish uchun botning avtomatik javob tizimi.
Texnologiyalar
Python - Bot dasturlash tili.
Django - Backend uchun veb-ramka.
Aiogram - Telegram bot interfeysi uchun kutubxona.
SQLite/PostgreSQL - Ma'lumotlar bazasi.
Docker - Loyihani izolyatsiya qilish va oson tarqatish uchun.
O'rnatish
requirements.txt faylini oling va kerakli kutubxonalarni o'rnating:

bash
Copy
Edit
pip install -r requirements.txt
Django loyihasini sozlang va migratsiyalarni amalga oshiring:

bash
Copy
Edit
python manage.py migrate
Telegram bot uchun tokenni o'rnating va botni ishga tushiring:

bash
Copy
Edit
python manage.py runserver
Foydalanish
Telegram'da botni toping (Bot username yoki link).
Bot bilan muloqot qiling va kerakli ma'lumotlarni oling.
