import random
import telebot
from telebot import types

# BotFather'dan olgan API Tokeningizni shu yerga kiriting
TOKEN = '8840537284:AAEjM-RvGVtK13V_4dreHUiKXcMC0ygcy7E'
bot = telebot.TeleBot(TOKEN)

# 100 talik YHQ savollar kartotekasi (Baza to'g'ridan-to'g'ri kod ichida)
ALL_QUESTIONS = [
    {
        "id": 1,
        "question": "🚦 Qizil chiroq svetoforda nimani bildiradi?",
        "options": ["Harakatlanishni davom ettirish", "To'xtash (Harakatlanish taqiqlanadi)", "Tezlikni oshirish", "Diqqat bilan o'tish"],
        "correct": 1,
        "explanation": "Qizil chiroq harakatlanishni qat'iyan taqiqlaydi!"
    },
    {
        "id": 2,
        "question": "🚗 Regulyatorsiz teng ahamiyatli chorrahada kim birinchi o'tish huquqiga ega?",
        "options": ["O'ng tomondan kelayotgan transport vositasi", "Chap tomondan kelayotgan transport vositasi", "Katta mashina", "Har doim taksi"],
        "correct": 0,
        "explanation": "Teng ahamiyatli yo'llarda 'O'ng qo'l qoidasi' amal qiladi."
    },
    {
        "id": 3,
        "question": "🛑 'Stop' (Harakatlanmasdan to'xtash taqiqlanadi) belgisi ko'rinsa nima qilish kerak?",
        "options": ["Sekinlashib o'tib ketish", "Qat'iy to'xtab, yo'l bo'shligiga ishonch hosil qilib keyin yurish", "Piyodalarga yo'l bermaslik", "Chiroqni yoqish"],
        "correct": 1,
        "explanation": "STOP belgisi oldida transport vositasi kamida bir lahza to'liq to'xtashi shart."
    },
    {
        "id": 4,
        "question": "🔵 Ko'k rangli, oq strelkali to'g'ri ko'rsatuvchi belgi qaysi turkumga kiradi?",
        "options": ["Ogohlantiruvchi belgi", "Taqiqlovchi belgi", "Buyuruvchi belgi", "Imtiyoz belgisi"],
        "correct": 2,
        "explanation": "Buyuruvchi belgilar muayyan harakat yo'nalishlarini buyuradi."
    },
    {
        "id": 5,
        "question": "⚠️ Uchburchak shaklidagi qizil hoshiyali, ichida qora undov belgisi bor belgi nimani anglatadi?",
        "options": ["Boshqa xavfli vaziyat", "Asosiy yo'l", "Piyodalar o'tish joyi", "Kirish taqiqlangan"],
        "correct": 0,
        "explanation": "Bu 'Boshqa xavfli vaziyat' ogohlantiruvchi belgisidir."
    },
    {
        "id": 6,
        "question": "🛣 Aholi punktlaridan tashqari yo'llarda yengil avtomobillar uchun ruxsat etilgan maksimal tezlik qancha?",
        "options": ["70 km/soat", "90 km/soat", "100 km/soat", "110 km/soat"],
        "correct": 1,
        "explanation": "O'zbekiston YHQga ko'ra aholi punktidan tashqari yo'llarda yengil mashinalar 90 km/soat tezlikda harakatlanishi mumkin."
    },
    {
        "id": 7,
        "question": "🅿️ Ko'k fondagi 'P' harfi belgisi nimani bildiradi?",
        "options": ["To'xtash taqiqlangan joy", "To'xtab turish joyi (Avtoturargoh)", "Piyodalar zonasi", "Texxizmat ko'rsatish shoxobchasi"],
        "correct": 1,
        "explanation": "Bu belgi transport vositalarini to'xtab turish (parkovka) joyini bildiradi."
    },
    {
        "id": 8,
        "question": "🔄 Halqa shaklidagi chorrahada harakatlanayotganda kimga ustunlik beriladi?",
        "options": ["Halqaga kirib kelayotganlarga", "Halqa bo'ylab harakatlanayotgan transport vositalariga", "Faqat yuk mashinalariga", "Kim birinchi bo'lsa"],
        "correct": 1,
        "explanation": "Qoidaga ko'ra, halqa bo'ylab harakatlanayotgan transport vositalari asosiy yo'l hisoblanadi."
    },
    {
        "id": 9,
        "question": "🌙 Qorong'i vaqtda yo'lni yoritmaydigan qismlarida harakatlanganda qanday chiroqlarni yoqish shart?",
        "options": ["Faqat gabarit chiroqlarini", "Uzoqni yoki yaqinni yorituvchi chiroqlarni", "Faqat burilish chiroqlarini", "Chiroqlarni o'chirib yurish mumkin"],
        "correct": 1,
        "explanation": "Yoritilmagan yo'llarda uzoqni yoki yaqinni yorituvchi chiroqlar yoniq bo'lishi shart."
    },
    {
        "id": 10,
        "question": "👤 Piyodalar o'tish joyida (zebrada) piyodaga yo'l bermaslik qanday oqibatga olib keladi?",
        "options": ["Hech qanday chora ko'rilmaydi", "Jarima belgilanadi", "Faqat ogohlantirib qo'yiladi", "Rag'batlantiriladi"],
        "correct": 1,
        "explanation": "Piyodalarga yo'l bermaslik yo'l harakati qoidalarini buzish hisoblanib, jarimaga sabab bo'ladi."
    },
    {
        "id": 11,
        "question": "🟡 Sariq chiroq yonganda nima qilish kerak?",
        "options": ["Harakatni to'xtatish (agar xavf tug'dirmasa) yoki o'tishga tayyorgarlik ko'rish", "Tezlikni keskin oshirish", "Orqaga yurish", "Signal berish"],
        "correct": 0,
        "explanation": "Sariq chiroq taqiqlaydi va e'tiborga chaqiradi."
    },
    {
        "id": 12,
        "question": "🛞 Harakatlanish vaqtida g'ildirak yorilib ketsa haydovchi birinchi navbatda nima qilishi kerak?",
        "options": ["Keskin tormoz berish", "Rulni mahkam ushlab, gazni sekin olib, avtomobilni ushlab qolish", "Mashinadan sakrab tushish", "Rulni qattiq burish"],
        "correct": 1,
        "explanation": "Keskin tormozlash avariya keltirib chiqarishi mumkin, shuning uchun rulni mahkam ushlab boshqarish zarur."
    },
    {
        "id": 13,
        "question": "⛔️ 'Kirish taqiqlangan' (g'isht) belgisi qaysi transport vositalariga taalluqli emas?",
        "options": ["Yengil mashinalarga", "Yo'nalishdagi transport vositalariga (avtobus, yo'nalishli taksi)", "Yuk mashinalariga", "Motosikllarga"],
        "correct": 1,
        "explanation": "Belgilangan yo'nalishli transport vositalari bundan mustasno."
    },
    {
        "id": 14,
        "question": "📱 Haydovchi transport vositasini boshqarish vaqtida telefon ishlatishi mumkinmi?",
        "options": ["Faqat qizil chiroqda mumkin", "Mutlaqo taqiqlangan (qo'lni band qilmaydigan garnituralar bundan mustasno)", "Xohlagancha gaplashish mumkin", "Faqat shahar tashqarisida mumkin"],
        "correct": 1,
        "explanation": "Qoidaga ko'ra haydash paytida qo'lda telefon tutish taqiqlanadi."
    },
    {
        "id": 15,
        "question": "🦺 Sutkaning qorong'i vaqtida yo'l chetida piyoda harakatlanganda nima taqib olishi shart?",
        "options": ["Qora kiyim", "Nurlarni qaytaruvchi elementlari bor vest (nimcha)", "Quyosh ko'zoynigi", "Shlyapa"],
        "correct": 1,
        "explanation": "Ko'rinishni yaxshilash uchun nurlarni qaytaruvchi elementlar bo'lishi shart."
    },
    {
        "id": 16,
        "question": "🔙 Orqaga harakatlanish qaysi joylarda qat'iyan taqiqlangan?",
        "options": ["Piyodalar o'tish joylarida va ko'priklarda", "Keng ko'chalarda", "Hovli ichida", "To'xtash joylarida"],
        "correct": 0,
        "explanation": "Piyodalar o'tish joylari, ko'priklar, yo'l o'tkazgichlarda orqaga harakatlanish taqiqlanadi."
    },
    {
        "id": 17,
        "question": "🪪 Haydovchilik guvohnomasini olish uchun minimal yosh necha yoshdan etib belgilangan (B toifasi uchun)?",
        "options": ["16 yosh", "18 yosh", "20 yosh", "21 yosh"],
        "correct": 1,
        "explanation": "B va C toifasidagi transport vositalarini boshqarish uchun 18 yoshdan ruxsat etiladi."
    },
    {
        "id": 18,
        "question": "📉 Avtomagistralda harakatlanish tezligi minimal darajada qancha bo'lishi kerak (pastroq tezlikdagi mashinalar uchun)?",
        "options": ["40 km/soatdan kam bo'lmagan", "60 km/soat", "20 km/soat", "Cheklov yo'q"],
        "correct": 0,
        "explanation": "Avtomagistralda texnik holatiga ko'ra 40 km/soatdan past tezlikda harakatlanadigan transport vositalariga kirish taqiqlanadi."
    },
    {
        "id": 19,
        "question": "🧯 Har bir avtomobilda majburiy ravishda nima bo'lishi shart?",
        "options": ["Faqat magnitofon", "O't o'chirgich, tibbiy quti, ogohlantiruvchi uchburchak", "Zaxira rul", "Konditsioner"],
        "correct": 1,
        "explanation": "Xavfsizlik qoidalariga ko'ra ushbu uchta narsa har bir mashinada bo'lishi shart."
    },
    {
        "id": 20,
        "question": "⚠️ Avariya holatida to'xtash signali yonganda haydovchi nima qilishi kerak?",
        "options": ["Mashinani tashlab ketish", "Avariya to'xtash belgisini o'rnatish va signallarni yoqish", "Faqat signal berib turish", "Hech narsa qilmasa ham bo'ladi"],
        "correct": 1,
        "explanation": "Avariya vaqtida boshqalarni ogohlantirish uchun avariya belgisi qo'yiladi va chiroqlar yoqiladi."
    },
    {
        "id": 21,
        "question": "🛑 Temir yo'l kesishmasi oldida шлагбаум (to'siq) yopiq bo'lsa nima qilish kerak?",
        "options": ["Tezlikni oshirib o'tib ketish", "To'siq oldida to'xtash va ochilishini kutish", "Orqaga qaytib ketish", "Signol berib o'tishga urinish"],
        "correct": 1,
        "explanation": "To'siq yopiq yoki yopilayotgan paytda temir yo'l kesishmasiga kirish taqiqlanadi va to'xtash shart."
    },
    {
        "id": 22,
        "question": "🔵 Ko'k fondagi oq avtobus rasmi tushirilgan belgi nimani bildiradi?",
        "options": ["Avtobuslar to'xtash joyi", "Faqat avtobuslar harakatlanadigan yo'lak", "Yuk mashinalari yo'li", "Piyodalar yo'lagi"],
        "correct": 1,
        "explanation": "Bu belgi yo'nalishli transport vositalari uchun mo'ljallangan maxsus bo'lakni bildiradi."
    },
    {
        "id": 23,
        "question": "🚗 Harakatlanish qismida tirkama bilan harakatlanayotganda tezlik qanday tartibga solinadi?",
        "options": ["Oddiy mashinalar kabi", "Belgilangan tezlikdan 20 km/soat pastroq", "Istalgan tezlikda", "Faqat 40 km/soat"],
        "correct": 1,
        "explanation": "Tirkamali avtomobillar va yuk mashinalari uchun tezlik me'yorlari alohida belgilangan bo'ladi."
    },
    {
        "id": 24,
        "question": "🚸 Maktab yaqinida o'rnatiladigan odatda sariq fondagi bolalar rasmi bor belgi qaysi turkumga kiradi?",
        "options": ["Taqiqlovchi", "Ogohlantiruvchi", "Buyuruvchi", "Axborot-ko'rsatkich"],
        "correct": 1,
        "explanation": "Bolalar o'tish ehtimoli borligidan ogohlantiruvchi belgidir."
    },
    {
        "id": 25,
        "question": "🔄 Burilish vaqtida haydovchi kimga yo'l berishi shart?",
        "options": ["Faqat piyodalarga", "Qarshidan kelayotgan va o'ngga/chapga burilayotganda kesib o'tadigan piyoda va velosipedchilarga", "Hech kimga", "Faqat yuk mashinalariga"],
        "correct": 1,
        "explanation": "Burilishda yo'nalish kesib o'tadigan piyodalar va velosipedchilarga yo'l beriladi."
    },
    {
        "id": 26,
        "question": "⏱ Aholi punktlarida yengil avtomobillar uchun maksimal tezlik qancha etib belgilangan?",
        "options": ["50 km/soat", "60 km/soat", "70 km/soat", "90 km/soat"],
        "correct": 1,
        "explanation": "O'zbekiston Respublikasi YHQga ko'ra aholi punktlarida tezlik 60 km/soatdan oshmasligi kerak."
    },
    {
        "id": 27,
        "question": "🚫 Qizil hoshiyali doira ichida qora avtomobil va mototsikl yonma-yon tursa nimani bildiradi?",
        "options": ["Barcha transport vositalari harakati taqiqlangan", "Mexanik transport vositalari harakati taqiqlangan", "Faqat velosipedlar taqiqlangan", "Yuk mashinalari taqiqlangan"],
        "correct": 1,
        "explanation": "Bu belgi mexanik transport vositalarining harakatini taqiqlaydi."
    },
    {
        "id": 28,
        "question": "💡 Tumanli ob-havoda qaysi chiroqlardan foydalanish tavsiya etiladi?",
        "options": ["Faqat uzoqni yorituvchi chiroqlar", "Tuman chiroqlari va yaqinni yorituvchi chiroqlar", "Faqat gabarit", "Chiroqlarni o'chirib sekin yurish"],
        "correct": 1,
        "explanation": "Tuman va ko'rish darajasi yomon sharoitda tuman chiroqlari va yaqin chiroqlar yoqiladi."
    },
    {
        "id": 29,
        "question": "🅿️ Avtoturargohda mashinani qoldirganda nima qilish majburiy?",
        "options": ["Eshiklarni ochiq qoldirish", " стояночный тормоз (qo'l tormozi)ga qo'yish va dvigatelni o'chirish", "Musiqani baland qoldirish", "Kalitni qoldirish"],
        "correct": 1,
        "explanation": "Mashina o'z-o'zidan yurib ketmasligi uchun qo'l tormoziga qo'yiladi va o'chiriladi."
    },
    {
        "id": 30,
        "question": "🚧 Ta'mirlash ishlariga yaqinlashganda qanday chiroqlar yoki belgilar qo'yiladi?",
        "options": ["Faqat yashil bayroqchalar", "Qizil yoki sariq miltillovchi chiroqlar va ogohlantiruvchi belgilar", "Belgi qo'yilmaydi", "Faqat katta toshlar"],
        "correct": 1,
        "explanation": "Yo'l ta'mirlash ishlarida ogohlantiruvchi elementlar va miltillovchi chiroqlar ishlatiladi."
    },
    {
        "id": 31,
        "question": "🛑 Chorrahada tartibga soluvchining qo'li oldinga uzatilgan bo'lsa, o'ng tomondan kelayotgan mashina nima qilishi kerak?",
        "options": ["Harakatlanishni davom ettirish", "To'xtash", "Orqaga qaytish", "Tezlikni oshirish"],
        "correct": 0,
        "explanation": "Tartibga soluvchining ko'kragi va o'ng tomoni ko'rsatib turgan tomonga harakatlanish ruxsat etiladi."
    },
    {
        "id": 32,
        "question": "🚗 Qutqaruv va maxsus mashinalar (tez yordam, o't o'chiruvchi) маячок va tovush chiqarib kelsa nima qilish kerak?",
        "options": ["Yo'l berish va to'siqsiz o'tishini ta'minlash", "Oldiga o'tib olish", "Tezlikni bir xilda saqlash", "Orqasidan quvib yetish"],
        "correct": 0,
        "explanation": "Maxsus transport vositalariga mutlaqo ustunlik berilib, yo'l bo'shatib beriladi."
    },
    {
        "id": 33,
        "question": "📋 Haydovchilik guvohnomasiz mashina boshqarish qanday javobgarlikka sabab bo'ladi?",
        "options": ["Ogohlantirish", "Qonunchilikda belgilangan tartibda jarima va chora ko'riladi", "Hech qanday chora yo'q", "Mukofot beriladi"],
        "correct": 1,
        "explanation": "Huquqsiz boshqarish qonunbuzarlik hisoblanib, qattiq jarima va choralarga olib keladi."
    },
    {
        "id": 34,
        "question": "🚲 Velosipedchilar qaysi yoshdan boshlab qatnov qismida harakatlanishi mumkin?",
        "options": ["10 yoshdan", "14 yoshdan", "16 yoshdan", "18 yoshdan"],
        "correct": 1,
        "explanation": "Yo'lning qatnov qismida velosipedda harakatlanish 14 yoshdan ruxsat etiladi."
    },
    {
        "id": 35,
        "question": "🔄 Avtomagistralda orqaga qayrilib olish taqiqlanganmi?",
        "options": ["Ha, mutlaqo taqiqlangan", "Faqat tunda mumkin", "Istalgan joyda mumkin", "Faqat yo'l patrul xizmati ruxsati bilan"],
        "correct": 0,
        "explanation": "Avtomagistrallarda orqaga qayrilish va teskari harakatlanish qat'iyan taqiqlanadi."
    },
    {
        "id": 36,
        "question": "📉 Muzlagan yo'lda tormoz berganda mashina sirpanishining oldini olish uchun nima qilish kerak?",
        "options": ["Keskin tormoz berish", "Dvigatel yordamida tormozlash va silliq harakat qilish", "Rulni keskin burish", "Gazni oxirigacha bosish"],
        "correct": 1,
        "explanation": "Muzlamada keskin harakatlar mashinani boshqaruvdan chiqaradi, shuning uchun silliq boshqarish lozim."
    },
    {
        "id": 37,
        "question": "🛃 Yo'l chiziqlaridan uzluksiz oq chiziq nimani bildiradi?",
        "options": ["Uni kesib o'tish qat'iyan taqiqlanadi", "Istalgan payt kesib o'tish mumkin", "Faqat quvib o'tish uchun", "Piyodalar yo'lagi"],
        "correct": 0,
        "explanation": "Uzluksiz yagona oq chiziqni bosib o'tish yoki kesish taqiqlanadi."
    },
    {
        "id": 38,
        "question": "🚨 Mashinada o'rindiq kamarini taqish kim uchun majburiy?",
        "options": ["Faqat haydovchi uchun", "Faqat oldingi o'rindiqdagi yo'lovchi uchun", "Haydovchi va barcha yo'lovchilar uchun", "Majburiy emas"],
        "correct": 2,
        "explanation": "Xavfsizlik kamari haydovchi va barcha yo'lovchilar uchun taqilishi shart."
    },
    {
        "id": 39,
        "question": "🛑 Qizil hoshiyali doira ichida 50 raqami tursa nimani bildiradi?",
        "options": ["Minimal tezlik 50 km/soat", "Maksimal tezlik 50 km/soatdan oshmasligi kerak", "Masofa 50 metr", "50 ta mashina"],
        "correct": 1,
        "explanation": "Bu taqiqlovchi belgi bo'lib, eng yuqori tezlikni cheklaydi."
    },
    {
        "id": 40,
        "question": "🔦 Uzoqni yorituvchi chiroqlarni yaqinni yorituvchi chiroqlarga qachon o'tkazish kerak?",
        "options": ["Faqat kunduzi", "Qarama-qarshi kelayotgan transportgacha kamida 150 metr qolganda", "Hech qachon o'tkazilmaydi", "Faqat shahar ichida"],
        "correct": 1,
        "explanation": "Qarshidan kelayotgan haydovchilarni ko'r qilib qo'ymaslik uchun masofa saqlanib o'tkaziladi."
    },
    {
        "id": 41,
        "question": "🚗 Harakatlanish vaqtida motor qizib ketsa (temperatura ko'tarilib yuborsa) nima qilish kerak?",
        "options": ["Tezlikni oshirish", "To'xtash, dvigatelni o'chirish va sovishini kutish", "Suv purkab davom etish", "E'tibor bermasdan haydash"],
        "correct": 1,
        "explanation": "Qizib ketish jiddiy nosozlik keltirib chiqaradi, shuning uchun darhol to'xtash kerak."
    },
    {
        "id": 42,
        "question": "🅿️ Yo'l chetida to'xtab turish (parkovka) qaysi tomonda amalga oshiriladi?",
        "options": ["Faqat o'ng tomonda (yoki qoidaga ko'rsatilgan joyda)", "Chap tomonda", "Istalgan yo'l o'rtasida", "Faqat daraxt tagida"],
        "correct": 0,
        "explanation": "O'zbekistonda o'ng tomonda to'xtash va to'xtab turish qoidasi amal qiladi."
    },
    {
        "id": 43,
        "question": "🚏 Avtobus bekatlarida to'xtash yoki to'xtab turish qancha masofada taqiqlanadi?",
        "options": ["5 metrgacha bo'lgan masofada", "15 metrdan yaqin masofada", "Cheklov yo'q", "Faqat bekat ustida"],
        "correct": 1,
        "explanation": "Bekat va yo'nalishli transport to'xtash joylariga yaqin joyda to'xtash cheklanadi."
    },
    {
        "id": 44,
        "question": "⚠️ Ogohlantiruvchi belgilar odatda qanday shaklda bo'ladi?",
        "options": ["Doira shaklida", "Uchburchak shaklida (qizil hoshiyali)", "To'rtburchak", "Sakkizburchak"],
        "correct": 1,
        "explanation": "Ogohlantiruvchi belgilar asosan qizil hoshiyali oq uchburchak shaklida bo'ladi."
    },
    {
        "id": 45,
        "question": "🚙 Katta yuk mashinasini quvib o'tishdan oldin haydovchi nima qilishi shart?",
        "options": ["Ko'rinish yaxshiligiga va qarshidan mashina kelmayotganiga ishonch hosil qilish", "Ko'zni yumib o'tib ketish", "Faqat signal berish", "Tezlikni kamaytirish"],
        "correct": 0,
        "explanation": "Quvib o'tish xavfsizligini ta'minlash uchun yo'l ochiq bo'lishi shart."
    },
    {
        "id": 46,
        "question": "🚦 Svetoforning yashil miltillovchi chirog'i nimani bildiradi?",
        "options": ["Chiroq yonishi vaqty tugayotgani va harakat taqiqlanishiga o'tishini", "Harakatlanish taqiqlanganini", "Tezlikni oshirish kerakligini", "To'xtashni"],
        "correct": 0,
        "explanation": "Yashil miltillovchi chiroq vaqt tugayotganini bildiradi."
    },
    {
        "id": 47,
        "question": "🛑 Temir yo'l kesishmasidan o'tayotganda dvigatel o'chib qolsa va yurmasa nima qilish kerak?",
        "options": ["Mashinada o'tirish", "Darhol yo'lovchilarni tushirish, mashinani relsdan chiqarish chorasini ko'rish", "Signal berib kutish", "Uxlayverish"],
        "correct": 1,
        "explanation": "Xavfsizlikni ta'minlash uchun odamlarni uzoqlashtirib, mashinani tozalash chorasi ko'riladi."
    },
    {
        "id": 48,
        "question": "📜 Yo'l qoidalarini buzganlik uchun jarima ballari tizimi qanday maqsadga xizmat qiladi?",
        "options": ["Haydovchilarni intizomga o'rgatish va qoidabuzarliklarning oldini olish", "Faqat pul yig'ish", "Mashinani tortib olish", "Hech qanday ahamiyati yo'q"],
        "correct": 0,
        "explanation": "Jarima ballari haydovchilar mas'uliyatini oshirishga qaratilgan."
    },
    {
        "id": 49,
        "question": "🔍 Mashinaning oynalari (tirkama va orqa oynalardan tashqari) qoraytirilgan (тонировка) bo'lishi uchun nima kerak?",
        "options": ["Ruxsatnoma (litsenziya) bo'lishi shart", "Xohlagancha qoraytiraverish mumkin", "Faqat qora rangda qilish", "Ruxsat kerak emas"],
        "correct": 0,
        "explanation": "Oynalarni qoraytirish qonuniy belgilangan tartib va ruxsatnomaga ega bo'lishi kerak."
    },
    {
        "id": 50,
        "question": "🛣 Avtomagistralda o'quv mashinalarida haydashga ruxsat etiladimi?",
        "options": ["Ha, istalgan vaqtda", "Yo'q, avtomagistralda o'quv haydash taqiqlangan", "Faqat kechasi", "Faqat instruktor bilan"],
        "correct": 1,
        "explanation": "Avtomagistrallarda o'quv haydash qat'iyan taqiqlanadi."
    },
    {
        "id": 51,
        "question": "🚗 Burilish ko'rsatkichlari (povorotnik) qachon yoqilishi kerak?",
        "options": ["Burilishdan keyin", "Manevr boshlashdan oldin yetarli masofa qolganda", "Faqat tunda", "Kerak emas"],
        "correct": 1,
        "explanation": "Boshqa haydovchilarni o'z vaqtida ogohlantirish uchun manevrdan oldin yoqiladi."
    },
    {
        "id": 52,
        "question": "🛑 Ko'priklar va yo'l o'tkazgichlarda quvib o'tish ruxsat etiladimi?",
        "options": ["Ha, har doim", "Cheklangan joylarda va ko'priklarda quvib o'tish taqiqlanadi", "Faqat yuk mashinalariga mumkin", "Istalgan vaqtda"],
        "correct": 1,
        "explanation": "Ko'prik osti va ustida quvib o'tish qat'iy cheklangan yoki taqiqlangan."
    },
    {
        "id": 53,
        "question": "🚲 Velosiped yo'lakchasi bo'lgan joyda velosipedchi qayerda yurishi shart?",
        "options": ["Faqat velosiped yo'lakchasida", "Piyodalar yo'lida", "Mashina yo'lining o'rtasida", "Istalgan joyda"],
        "correct": 0,
        "explanation": "Maxsus yo'lak bo'lsa, velosipedchilar o'sha yerda harakatlanishi shart."
    },
    {
        "id": 54,
        "question": "⛽ Yoqilg'i quyish shoxobchasida (ZIS) qanday qoidalarga amal qilish kerak?",
        "options": ["Ochiq olovdan foydalanmaslik, dvigatelni o'chirish", "Sigaret chekish", "Tezlikni oshirish", "Signal berish"],
        "correct": 0,
        "explanation": "Yoqilg'i quyish shoxobchalarida yong'in xavfsizligi qoidalariga qat'iy amal qilinadi."
    },
    {
        "id": 55,
        "question": "👥 Avtomobilda bolalarni tashish uchun nima talab qilinadi?",
        "options": ["Maxsus bolalar o'rindiqli moslamasi (krelo)", "Quvvatlab o'tirish", "Faqat quchoqda olib yurish", "Hech narsa kerak emas"],
        "correct": 0,
        "explanation": "Kichik yoshdagi bolalarni maxsus bolalar o'rindiqlarida tashish xavfsizlik uchun majburiy."
    },
    {
        "id": 56,
        "question": "🛑 Tartibga solinmagan piyodalar o'tish joyida haydovchi nima qilishi kerak?",
        "options": ["Tezlikni oshirib o'tib ketish", "Piyodalarga yo'l berish uchun to'xtash yoki sekinlashish", "Signal berish", "Yo'lni davom ettirish"],
        "correct": 1,
        "explanation": "Piyodalarga yo'l o'tish joyida o'tishga ustunlik beriladi."
    },
    {
        "id": 57,
        "question": "🌧 Kuchli yomg'ir yoki qor yog'ayotganda haydovchi nima qilishi lozim?",
        "options": ["Tezlikni kamaytirish va masofani saqlash", "Tezlikni keskin oshirish", "Ko'zni yumib haydash", "To'xtab uxlash"],
        "correct": 0,
        "explanation": "Noqulay ob-havoda ehtiyotkorlik va masofa oshiriladi."
    },
    {
        "id": 58,
        "question": "🅿️ Nogironlar uchun ajratilgan parkovka joyiga boshqa mashinalar qo'ysa nima bo'ladi?",
        "options": ["Hech narsa bo'lmaydi", "Jarima belgilanadi va evakuator olib ketishi mumkin", "Rag'batlantiriladi", "Taqdirlanadi"],
        "correct": 1,
        "explanation": "Nogironlar joyiga ruxsatsiz turish qonunbuzarlik hisoblanadi."
    },
    {
        "id": 59,
        "question": "🚗 Orqaga yurish chiroqlari qanday rangda yonishi kerak?",
        "options": ["Qizil", "Oq", "Sariq", "Ko'k"],
        "correct": 1,
        "explanation": "Orqaga yurish chiroqlari oq rangda yonib, boshqalarni ogohlantiradi."
    },
    {
        "id": 60,
        "question": "🚥 Svetoforning qo'shimcha seksiyasi va asosiy yashil chiroq birga yonganda nima bildiradi?",
        "options": ["Faqat o'sha Seksiya ko'rsatgan yo'nalishga harakatlanishga ruxsat", "Harakat taqiqlangan", "Hamma yo'nalish yopiq", "To'xtash kerak"],
        "correct": 0,
        "explanation": "O'sha yo'nalishga ustun tarzda harakatlanish ruxsat etiladi."
    },
    {
        "id": 61,
        "question": "🛑 Yo'l chetidagi qattiq sariq chiziq nimani bildiradi?",
        "options": ["To'xtab turish (parkovka qilish) taqiqlangan joy", "Tez yurish joyi", "Piyodalar yo'li", "To'xtash ruxsat etilgan"],
        "correct": 0,
        "explanation": "Sariq uzluksiz chiziq o'sha joyda to'xtab turish taqiqlanganini bildiradi."
    },
    {
        "id": 62,
        "question": "🛞 Qishki shinalarga o'tish qaysi mavsumda yoki sharoitda tavsiya etiladi?",
        "options": ["Faqat yozda", "Havo harorati pasayganda va qor/muzli yo'llarda", "Faqat bayramlarda", "Kerak emas"],
        "correct": 1,
        "explanation": "Qishki shinalar xavfsiz harakatlanishni ta'minlaydi."
    },
    {
        "id": 63,
        "question": "🚗 Yo'lda ketayotganda oldingi mashina bilan qanday masofa (distan) saqlanishi kerak?",
        "options": ["To'qnashuvning oldini oluvchi yetarli masofa", "1 santimetr", "10 kilometr", "Farqi yo'q"],
        "correct": 0,
        "explanation": "Xavfsiz oraliq masofa tezlikka qarab tanlanadi."
    },
    {
        "id": 64,
        "question": "🪪 Haydovchi o'zi bilan qanday hujjatlarni olib yurishi shart?",
        "options": ["Guvohnoma, texnik pasport, sug'urta va boshqalar", "Faqat pasport", "Faqat pul", "Hech qanday hujjat shart emas"],
        "correct": 0,
        "explanation": "Haydovchida barcha asosiy qonuniy hujjatlar bo'lishi shart."
    },
    {
        "id": 65,
        "question": "🛑 Asosiy yo'l belgisi qanday shaklda bo'ladi?",
        "options": ["Aksincha yotqizilgan uchburchak", "Sariq romb shaklida", "Dumaloq", "To'rtburchak"],
        "correct": 1,
        "explanation": "Asosiy yo'l belgisi sariq romb ko'rinishida bo'ladi."
    },
    {
        "id": 66,
        "question": "🚲 Katta yo'lda velosiped haydashda qaysi qoidaga amal qilish kerak?",
        "options": ["Yo'lning o'ng chetidan iloji boricha o'ngda harakatlanish", "Yo'lning o'rtasida yurish", "Ters yo'nalishda yurish", "Tezlikni oshirish"],
        "correct": 0,
        "explanation": "Velosipedchilar imkon qadar o'ng chetda harakatlanishi kerak."
    },
    {
        "id": 67,
        "question": "🚨 Avtomashina tormoz tizimi ishdan chiqsa nima qilish kerak?",
        "options": ["Dvigatel yordamida tormozlash, qo'l tormozidan ehtiyotkorlik bilan foydalanish", "Mashinadan sakrash", "Ko'zni yumish", "Gazni bosish"],
        "correct": 0,
        "explanation": "Favqulodda vaziyatda dvigatel va qo'l tormozi yordamida sekinlashtiriladi."
    },
    {
        "id": 68,
        "question": "📉 Yo'lning nishab (tik pasayish) qismida harakatlanganda qanday tezlik qoidasi qo'llaniladi?",
        "options": ["Past uzatmada (peredacha) harakatlanish", "Neytralda tez tushish", "Dvigatelni o'chirish", "Keskin tormozda yurish"],
        "correct": 0,
        "explanation": "Tormoz qizib ketmasligi uchun past uzatmada tormozlanib tushiladi."
    },
    {
        "id": 69,
        "question": "🛑 Yo'l patrul xizmati xodimi qo'lini yuqoriga ko'tarsa nimani bildiradi?",
        "options": ["Hamma harakat taqiqlanadi (to'xtash kerak)", "Tezroq yurish", "Orqaga qaytish", "O'ngga yurish"],
        "correct": 0,
        "explanation": "Xodimning qo'li yuqoriga ko'tarilishi barcha transport va piyodalar uchun taqiqni bildiradi."
    },
    {
        "id": 70,
        "question": "🚗 Mashinaning akkumulyatori o'tirib qolsa nima qilish kerak?",
        "options": ["Boshqa mashinadan 'prkuravit' qilish yoki zaryadlash", "Mashinani tashlab yuborish", "Suv quyish", "Oyna tozalagichni yoqish"],
        "correct": 0,
        "explanation": "Akkumulyatorni zaryadlash yoki boshqa manba yordamida o't oldiriladi."
    },
    {
        "id": 71,
        "question": "🚸 Bolalar muassasalari yaqinida tezlik qanday bo'lishi kerak?",
        "options": ["Cheklangan va alohida e'tiborli", "Istalgancha", "100 km/soat", "Faqat tez"],
        "correct": 0,
        "explanation": "Bolalar xavfsizligi uchun tezlik maxsus cheklanadi."
    },
    {
        "id": 72,
        "question": "🛑 Qizil xoch tushirilgan tibbiy quti mashinada nima uchun kerak?",
        "options": ["Birinchi yordam ko'rsatish uchun", "Ovqat solish uchun", "Bezakt uchun", "Telefon saqlash uchun"],
        "correct": 0,
        "explanation": "Tibbiy quti jarohatlanganda birinchi yordam berishga mo'ljallangan."
    },
    {
        "id": 73,
        "question": "🚗 Harakatlanish vaqtida kapot ochilib ketsa haydovchi nima qilishi kerak?",
        "options": ["Rulni mahkam ushlab, sekin tormoz berib o'ngga to'xtash", "Oynadan bosh chiqarib qarash", "Tezlikni keskin oshirish", "Sakrab tushish"],
        "correct": 0,
        "explanation": "Ko'rinish yopilib qolganda xotirjamlik bilan mashina to'xtatiladi."
    },
    {
        "id": 74,
        "question": "🅿️ Tun vaqtida yoritilmagan yo'l chetiga to'xtaganda qaysi chiroqlar yoniq turishi kerak?",
        "options": ["Gabarit yoki to'xtash chiroqlari", "Faqat uzoqni yorituvchi", "Hech qanday chiroq kerak emas", "Faqat povorotnik"],
        "correct": 0,
        "explanation": "Boshqalar ko'rishi uchun gabarit chiroqlari yoqib qo'yiladi."
    },
    {
        "id": 75,
        "question": "🔄 Chorrahada chapga burilish vaqtida qarshidan kelayotgan to'g'ri borayotgan mashinaga nima qilish kerak?",
        "options": ["Yo'l berish shart", "Yo'l bermasdan o'tib ketish", "Signal berish", "Tezlikni oshirish"],
        "correct": 0,
        "explanation": "Chapga burilayotganda qarshidan to'g'ri kelayotganlarga yo'l beriladi."
    },
    {
        "id": 76,
        "question": "🛑 'Yo'l bering' belgisi qanday shaklda bo'ladi?",
        "options": ["Uchburchagi uchi pastga qaragan oq fonda qizil hoshiyali", "Romb", "Doira", "To'rtburchak"],
        "correct": 0,
        "explanation": "Bu belgi asosiy yo'ldagilarga yo'l berishni bildiradi."
    },
    {
        "id": 77,
        "question": "🚗 Avtomobilni mast holatda boshqarish qanday oqibatga olib keladi?",
        "options": ["Guvohnomadan mahrum qilish va og'ir jarima", "Mukofot", "Rag'bat", "Hech narsa"],
        "correct": 0,
        "explanation": "Mast holda mashina haydash qat'iyan taqiqlangan va huquqdan mahrum qiladi."
    },
    {
        "id": 78,
        "question": "🛣 Yo'l yuzidagi qirqilgan oq chiziqlar nimani bildiradi?",
        "options": ["Chiziqni kesib o'tish yoki qator o'zgartirish mumkin", "Mutlaqo taqiqlangan", "To'xtash taqiqlangan", "Faqat piyodalar yuradi"],
        "correct": 0,
        "explanation": "Uzviy bo'lmagan chiziqlar qatorni o'zgartirishga ruxsat beradi."
    },
    {
        "id": 79,
        "question": "🛑 Temir yo'l kesishmasidan o'tayotganda signal berib turgan qizil chiroq yonsa nima qilish kerak?",
        "options": ["Qat'iy to'xtash", "Tezroq o'tib ketish", "Orqaga yurish", "E'tibor bermaslik"],
        "correct": 0,
        "explanation": "Qizil chiroq yonib turganda kesishmadan o'tish taqiqlanadi va to'xtalish shart."
    },
    {
        "id": 80,
        "question": "🛞 G'ildirak bosimi belgilangan me'yordan past bo'lsa nima sodir bo'ladi?",
        "options": ["Yoqilg'i sarfi oshadi va boshqarish qiyinlashadi", "Mashina uchadi", "Tezlik oshadi", "Hech narsa o'zgarmaydi"],
        "correct": 0,
        "explanation": "Past bosim yoqilg'i sarfiga va shinalarning yeyilishiga salbiy ta'sir qiladi."
    },
    {
        "id": 81,
        "question": "🚗 Harakatlanish vaqtida eshiklardan biri yaxshi yopilmagani sezilsa nima qilish kerak?",
        "options": ["Xavfsiz joyga to'xtab, eshikni qaytadan to'liq yopish", "Harakatni davom ettirish", "Oynadan chiqib yopish", "E'tibor bermaslik"],
        "correct": 0,
        "explanation": "Xavfsizlik uchun eshiklar to'liq yopilgan bo'lishi shart."
    },
    {
        "id": 82,
        "question": "🛑 Piyodalar o'tish joyiga yaqinlashayotgan haydovchi nima qilishi kerak?",
        "options": ["Tezlikni kamaytirish va kerak bo'lsa to'xtab piyodalarga yo'l berish", "Tezlikni oshirish", "Signal berish", "O'tib ketish"],
        "correct": 0,
        "explanation": "Piyodalarga ustunlik berish qoidasi bajariladi."
    },
    {
        "id": 83,
        "question": "🌧 Yomg'irli kunda tormoz yo'li (тормозной путь) qanday o'zgaradi?",
        "options": ["Uzayadi (sürpanish hisobiga to'xtash qiyinlashadi)", "Qisqaradi", "O'zgarmaydi", "Umuman tormoz ishlamaydi"],
        "correct": 0,
        "explanation": "Nam yo'lda tormoz yo'li quruq yo'ldagiga qaraganda uzunroq bo'ladi."
    },
    {
        "id": 84,
        "question": "🅿️ Yo'l qatnov qismining chetida turgan mashinani chetlab o'tishda kimga yo'l beriladi?",
        "options": ["Qarshidan kelayotgan transportga", "Hech kimga", "Orqadagiga", "Piyodaga"],
        "correct": 0,
        "explanation": "O'z yo'nalishida to'siq bo'lsa, qarshi harakatga xalaqit bermaslik kerak."
    },
    {
        "id": 85,
        "question": "🚦 Svetofor ishlamay qolganda chorrahadan o'tish qanday tartibga solinadi?",
        "options": ["Imtiyozli yo'l belgilariga yoki qoidalarga amal qilinadi", "Hamma xohlagancha o'tadi", "Harakat taqiqlanadi", "Politsiya kelishini kutish"],
        "correct": 0,
        "explanation": "Tartibga solinmagan chorrahalar qoidalari qo'llaniladi."
    },
    {
        "id": 86,
        "question": "🚗 Qorong'i vaqtda qarshidan kelayotgan mashina sizni ko'r qilsa (ko'zni qamashtirsa) nima qilish kerak?",
        "options": ["Tezlikni pasaytirib, o'ng qatorga olib to'xtash", "Ko'zni yumib haydash", "Uzoqni yoqish", "Keskin burilish"],
        "correct": 0,
        "explanation": "Ko'r bo'lib qolganda avariya chiqarmaslik uchun sekinlashib to'xtash tavsiya etiladi."
    },
    {
        "id": 87,
        "question": "🛑 Qizil hoshiyali doira ichida 40 raqami tursa nimani bildiradi?",
        "options": ["Maksimal tezlik 40 km/soatdan oshmasligi kerak", "Minimal tezlik", "Masofa 40 metr", "Vaqt"],
        "correct": 0,
        "explanation": "Tezlikni 40 km/soatdan oshirmaslikni bildiruvchi belgi."
    },
    {
        "id": 88,
        "question": "🪪 Haydovchilik guvohnomasining amal qilish muddati tugasa nima qilish kerak?",
        "options": ["Uni belgilangan tartibda almashtirish", "Shunchaki haydab yuraverish", "Yirtib tashlash", "Yangi mashina olish"],
        "correct": 0,
        "explanation": "Muddati o'tgan guvohnoma huquqiy kuchga ega emas, uni yangilash kerak."
    },
    {
        "id": 89,
        "question": "🛣 Avtomagistralda eng past tezlik qancha bo'lishi kerak?",
        "options": ["Texnik imkoniyati 40 km/soatdan past bo'lmagan", "10 km/soat", "Cheklov yo'q", "80 km/soat"],
        "correct": 0,
        "explanation": "Avtomagistralda sekin yuradigan transportlar harakati cheklangan."
    },
    {
        "id": 90,
        "question": "🛑 Aholi punktlarida signal (sound signal) berish qachon ruxsat etiladi?",
        "options": ["Faqat avariyaning oldini olish maqsadida", "Doimiy ravishda", "Musiqa o'rnida", "Tanishlarni ko'rganda"],
        "correct": 0,
        "explanation": "Shahar ichida tovushli signaldan faqat avariya oldini olish uchun foydalaniladi."
    },
    {
        "id": 91,
        "question": "🚗 Harakatlanish vaqtida motor moyi bosimi chirog'i yonib qolsa nima qilish kerak?",
        "options": ["Darhol to'xtab, moy darajasini tekshirish", "E'tibor bermasdan yurish", "Gazni bosish", "Radio ovozini balandlatish"],
        "correct": 0,
        "explanation": "Moy bosimi yo'qolishi motorning buzilishiga olib keladi, darhol to'xtash shart."
    },
    {
        "id": 92,
        "question": "🛑 Yo'l chetidagi ko'k rangli to'rtburchak 'Bir tomonlama harakatlanish yo'li' belgisi nimani bildiradi?",
        "options": ["Barcha transport faqat bitta yo'nalishda harakatlanishini", "Ikki tomonlama harakatni", "To'xtash taqiqlanganini", "Piyodalar yo'lini"],
        "correct": 0,
        "explanation": "Bu yo'lda harakat faqat bitta tomonga amalga oshiriladi."
    },
    {
        "id": 93,
        "question": "🚲 Velosipedda ketayotganda burilish uchun qo'l bilan qanday ishora qilinadi?",
        "options": ["O'sha tomonga qo'l uzatiladi", "Qo'l ko'tariladi", "Hech qanday ishora shart emas", "Oyoq ko'rsatiladi"],
        "correct": 0,
        "explanation": "Burilmoqchi bo'lgan tomon qo'l bilan ko'rsatiladi."
    },
    {
        "id": 94,
        "question": "🛑 Temir yo'l kesishmasi oldida 'STOP' belgisi turganda haydovchi nima qilishi shart?",
        "options": ["To'liq to'xtab, poyezd yo'qligiga ishonch hosil qilib harakatlanish", "Sekinlashib o'tib ketish", "Tezlikni oshirish", "Signal berish"],
        "correct": 0,
        "explanation": "STOP belgisi ostida to'liq to'xtash majburiydir."
    },
    {
        "id": 95,
        "question": "🚗 Kuz faslida yaproqlar to'kilgan yo'lda harakatlanishda nimalarga e'tibor berish kerak?",
        "options": ["Yo'l silliq bo'lishi mumkinligi uchun ehtiyotkor bo'lish", "Tezlikni oshirish", "Faqat tunda yurish", "Hech narsaga"],
        "correct": 0,
        "explanation": "Ho'l yaproqlar yo'lni sirpanchiq કરી qo'yadi."
    },
    {
        "id": 96,
        "question": "🛑 Tartibga soluvchining qo'llari yon tomonga tushirilgan yoki yonga cho'zilgan bo'lsa, tramvay va retselsiz transport qayerga yurishi mumkin?",
        "options": ["Chapga va o'ngga ruxsat etiladi", "Faqat to'xtash", "Faqat orqaga", "Harakat taqiqlangan"],
        "correct": 0,
        "explanation": "Bu vaziyatda ko'krak va orqa tomonidan o'tish taqiqlanib, yon tomonlardan ruxsat etiladi."
    },
    {
        "id": 97,
        "question": "🅿️ Yo'l bo'yida turgan mashinadan tushishda qaysi tomondan tushish xavfsizroq?",
        "options": ["Yo'lning qatnov qismiga teskari, trotuar (yo'lak) tomonidan", "Orqa eshikdan", "Chap qatnov qismidan", "Farqi yo'q"],
        "correct": 0,
        "explanation": "Mashinalar oqimidan xavfsiz bo'lish uchun trotuar tomonidan tushiladi."
    },
    {
        "id": 98,
        "question": "🛑 Qizil hoshiyali doira ichida oq fonda qizil qiya chiziq bilan 50 raqami o'chirilgan bo'lsa nimani bildiradi?",
        "options": ["Maksimal tezlik cheklovining tugashi", "Tezlikni 50 qilish", "50 metr qoldi", "To'xtash"],
        "correct": 0,
        "explanation": "Bu belgi ilgari o'rnatilgan cheklovlarning amal qilish muddati tugaganini bildiradi."
    },
    {
        "id": 99,
        "question": "🚗 Harakatlanish vaqtida old oynaga yomg'ir suvlari to'plansa nima ishlatiladi?",
        "options": ["Oyna tozalagichlar ( дворники ) va suv purkagich", "Qo'l bilan artish", "Isitgich", "Konditsioner"],
        "correct": 0,
        "explanation": "Ko'rinishni tiklash uchun oyna tozalagichlar yoqiladi."
    },
    {
        "id": 100,
        "question": "🏆 Imtihon testini muvaffaqiyatli topshirish uchun nima qilish kerak?",
        "options": ["YHQ qoidalarini yaxshilab o'rganish va testlarni doimiy mashq qilish", "Faqat omadga tayanib qolish", "Tasodifiy bosish", "Kitobni yopib qo'yish"],
        "correct": 0,
        "explanation": "Imtihondan o'tish uchun puxta tayyorgarlik va qoidalarni bilish talab etiladi."
    }
]

# Foydalanuvchilar ma'lumotlarini saqlash
user_data = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.chat.id
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_btn = types.KeyboardButton("🚀 Testni boshlash (20 ta savol)")
    markup.add(start_btn)
    
    bot.send_message(
        user_id, 
        f"Assalomu alaykum, {message.from_user.first_name}!\n\n"
        f"🚗 **Prava AI Imtihon Simulyatoriga xush kelibsiz!**\n"
        f"• Bazadagi jami savollar: **{len(ALL_QUESTIONS)} ta**\n"
        f"• Har bir testda bazadan **20 tadan tasodifiy savol** tushadi.\n"
        f"• Har bir savol uchun vaqt: **30 soniya** (Telegram Quiz rejimi).\n\n"
        f"Imtihonga tayyor bo'lsangiz, tugmani bosing:",
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda message: message.text == "🚀 Testni boshlash (20 ta savol)")
def start_quiz(message):
    user_id = message.chat.id
    
    # 100 talik bazadan 20 tasini tasodifiy tanlab olamiz
    shuffled_questions = random.sample(ALL_QUESTIONS, 20)
    
    user_data[user_id] = {
        'questions': shuffled_questions,
        'score': 0,
        'current_q': 0
    }
    send_question(user_id)

def send_question(user_id):
    user_session = user_data.get(user_id)
    if not user_session:
        return

    q_index = user_session['current_q']
    questions = user_session['questions']
    
    # Savollar tugasa natijani chiqarish
    if q_index >= len(questions):
        score = user_session['score']
        total = len(questions)
        
        result_text = f"🎉 **Imtihon yakunlandi!**\n\n" \
                      f"📊 Siz **{total}** ta savoldan **{score}** tasiga to'g'ri javob berdingiz.\n"
        
        if score >= 18:  # 20 tadan 18 tasi o'tish bali (90%)
            result_text += "🏆 A'lo natija! Imtihondan o'tdingiz (Muvaffaqiyatli)!"
        else:
            result_text += "⚠️ Afsuski, imtihondan o'ta olmadingiz. Yana tayyorlanib ko'ring."

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        restart_btn = types.KeyboardButton("🚀 Testni boshlash (20 ta savol)")
        markup.add(restart_btn)
        
        bot.send_message(user_id, result_text, reply_markup=markup, parse_mode="Markdown")
        return

    q = questions[q_index]
    
    # Viktorina rejimida 30 soniyali taymer bilan yuborish
    bot.send_poll(
        chat_id=user_id,
        question=f"[{q_index + 1}/{len(questions)}] {q['question']}",
        options=q['options'],
        type='quiz',
        correct_option_id=q['correct'],
        explanation=q['explanation'],
        is_anonymous=False,
        open_period=30
    )

@bot.poll_answer_handler()
def handle_poll_answer(poll_answer):
    user_id = poll_answer.user.id
    
    if poll_answer.option_ids and user_id in user_data:
        selected_option = poll_answer.option_ids[0]
        user_session = user_data[user_id]
        
        q_index = user_session['current_q']
        correct_option = user_session['questions'][q_index]['correct']
        
        if selected_option == correct_option:
            user_session['score'] += 1
            
        user_session['current_q'] += 1
        send_question(user_id)

print("Bot 100 talik ichki baza va 30 soniyali taymer bilan ishga tushdi...")
bot.polling(non_stop=True)
