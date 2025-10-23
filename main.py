""" Shart operatorlari mavzusidan masalalar! """

""" 1. 🛒 Onlayn xarid chegirmasi """

# pul = int(input("Xarid qilgan barcha maxsulotlarningizning narxini kiriting: "))
#
# if pul > 0:
#     if pul < 50_000:
#         print("Chegirma yoq!")
#     elif pul < 100_000:
#         print("Chegirma 5%")
#     elif pul < 200_000:
#         print("Chegirma 10%")
#     elif pul > 200_000:
#         print("Chegirma 15%")
# else:
#     print("Qimat notogri qayta kiriting 0 dan katta bolsin !")


""" 2. 🚦 Yo‘l harakati chirog‘i maslahati """

# rang = input("Sivitafor rangini kiriting! \nMisol: (Qizil, sariq, yashil): ").lower()
# yol = input("Yolni holatini kiritng! \nMisol: (Bosh, Band): ").lower()
#
# if rang == "qizil":
#     print("To‘xtang")
# elif rang == "sariq":
#     print("Tayyorlaning")
# elif rang == "yashil":
#     if yol == "bosh":
#         print("Yuring")
#     elif yol == "band":
#         print("Kuting")
#     else:
#         print("Qimat xato kiritgansiz!")
# else:
#     print("Qimat xato kiritgansiz!")

""" 3. 💊 Dori ichish vaqti """

# soat = int(input("Soatni kiiriting: "))
#
# if 0 <= soat <= 23:
#     if 6 <= soat < 12:
#         print("Ertalabgi dori")
#     elif 12 <= soat < 18:
#         print("Kunduzgi dori")
#     elif 18 <= soat <= 23:
#         print("Kechki dori")
#     elif 0 <= soat < 6:
#         print("Hozir dori ichish kerak emas")
# else:
#     print("Qimat xato kiritgansiz!")

""" 4. 🌡️ Haroratga qarab kiyim tanlas """

# harorat = int(input("Haroratni kiriting C': "))
#
# if harorat < 0:
#     print("Qalin palto, qo‘lqop kiying” deb chiqaring")
# elif harorat < 15:
#     print("Jaket kiying")
# elif harorat < 25:
#     print("Futbolka yetarli")
# else:
#     print("Yengil kiyim, soyabon oling")

""" 5. 🎒 Maktab sumkasi og‘irligi """

# o_sinf = int(input("Sinfni kiriting: "))
# s_ogirligi = float(input("Sumka og‘irligini kiriting: "))
#
# if 1 <= o_sinf <= 4:
#     if s_ogirligi < 2:
#         print("Og‘ir, kamaytiring!")
#     else:
#         print("Normal")
# elif 5 <= o_sinf <= 9:
#     if s_ogirligi < 4:
#         print("Og‘ir, kamaytiring!")
#     else:
#         print("Normal")
# else:
#     print("Qimat xato kiritgansiz!")

""" 6. 🏥 Bemor navbatini belgilash """

# yosh = int(input("Yoshingizni kirting: "))
# holat = input("Holatingiz qanaqa (“oddiy” yoki “ogir”): ").lower()
#
# if holat == "ogir":
#     print("Zudlik bilan")
# elif yosh < 10 or yosh > 70:
#     print("1-soat ichida")
# else:
#     print("3-soat ichida")

""" 7. 🚕 Taksi narxi (dam olish kuni) """

# kun = input("Kun nomini kiriting (masalan: Dushanba, Seshanba...): ").lower()
# masofa = float(input("Masofani kiriting (km): "))
#
# ish_kuni = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma']
# dam_kuni = ['shanba', 'yakshanba']
#
# if kun in dam_kuni:
#     if masofa > 10:
#         print("Bugun dam olish kuni!")
#         print(f"Summa: {(3600 * masofa) * 0.9} Sizga masofa 10 kmdan oshganligi sababli 10% chegirma beriladi.")
#     else:
#         print("Bugun dam olish kuni!")
#         print(f"Summa: {3600 * masofa} so'm.")
# elif kun in ish_kuni:
#     if masofa > 10:
#         print("Bugun ish kuni!")
#         print(f"Summa: {(3000 * masofa) * 0.9} so'm. Sizga masofa 10 kmdan oshganligi sababli 10% chegirma beriladi.")
#     else:
#         print("Bugun ish kuni!")
#         print(f"Summa: {3000 * masofa} so'm.")
# else:
#     print("Qiymat xato kiritildi!")

""" 8. 🌦️ Ob-havo bo‘yicha sayr tavsiyasi """

# h = int(input("Haroratni kiriting: "))
# y = int(input("Yomg'ir yog'ish % zini kiriting: "))
#
# if y > 0:
#     if y >= 70:
#         print("Uyda qoling")
#     else:
#         print("Ajoyib kun, sayrga boring!")
# elif h == int(h):
#     if h < 5:
#         print("Juda sovuq, sayr qilish tavsiya etilmaydi")
#     else:
#         print("Ajoyib kun, sayrga boring!")
# else:
#     print("Ikkala qiymatdan 1 tasi yo ikkalasi ham xato kiritldi!")

""" 9. 💰 Oylik byudjet nazorati """

# oylik = int(input("Oylik maoshni kiriting: "))
# xarajat = int(input("Oylik harajatlarni kiriting: "))
#
# if 0 <= oylik and 0 <= xarajat:
#     if xarajat > oylik:
#         print("Xavfli! Xarajatlarni kamaytiring")
#     elif xarajat == oylik:
#         print("Aynan yetarli")
#     else:
#         print("Ajoyib! Tejamkorlik qilyapsiz")
# else:
#     print("Xato qiymat qayta kiriting!")

""" 10. 🚲 Velosiped ijarasi """

# v_turi = input("Velosiped turini (“shahar” yoki “sport”) da kiriting: ")
# i_vaqti = int(input("Ijaraga olingan vaqtni kiriting: "))
#
# if v_turi == "shahar":
#     if 0 < i_vaqti:
#         print(f"Sizdan: {10000 * i_vaqti}")
#     else:
#         print("Qimat xato qayta kiriting!")
# elif v_turi == "sport":
#     if 0 < i_vaqti:
#         print(f"Sizdan: {15000 * i_vaqti}")
#     else:
#         print("Qimat xato qayta kiriting!")
# else:
#     print("Qimat xato qayta kiriting!")

""" 11. 🍎 Meva sifatini baholash """

# g = int(input("Meva og'irligini kiritng: "))
# axvoli = input("Mevani korinishi qanday (“yaxshi”/“yomon”) da kirting: ")
#
# if axvoli == "yomon":
#     print("Past sifat")
# elif g < 100:
#     print("Rad etiladi")
# elif g >= 200:
#     print("Premium")
# else:
#     print("Standart")

""" 12. 🏪 Supermarket chegirmasi """

# xarid_sumasi= int(input("Harid summasini kiritng: "))
# saot = int(input("Hozirgi soatni (0-23) kirting: "))
#
# if xarid_sumasi >= 100_000 or 18 <= saot <= 22:
#     print("15% chegirma")
# elif xarid_sumasi >= 50000 or 10 <= saot <= 18:
#     print("10% chegirma")
# else:
#     print("Chegirma yo‘q")

""" 13. 📚 Kutubxona kitob ijarasi """

# kitob = input("Kitob turini kiriting (ilmiy yoki badiiy): ")
# kunlar = int(input("Ijaraga olingan kunlar sonini kiriting: "))

# if kitob == "ilmiy":
#     narx = 2000
# else:
#     narx = 1000

# umumiy_narx = narx * kunlar

# if kunlar > 14:
#    umumiy_narx = umumiy_narx * 0.7
# elif kunlar > 7:
#    umumiy_narx = umumiy_narx * 0.8

# print(f"Umumiy narx: {umumiy_narx} so'm")
""" 14. 🏋️ Sport zali mashqlari  """

# mashq_turi = input("Mashq turini kiriting (kardio yoki og'irlik): ")
# tajriba_davomiyligi = int(input("Tajriba davomiyligini kiriting (yil): "))

# if mashq_turi == "kardio" and tajriba_davomiyligi < 1:
#    print("20 daqiqa yengil")
# elif mashq_turi == "og'irlik" and tajriba_davomiyligi >= 2:
#    print("60 daqiqa intensiv")
# else:
#    print("30 daqiqa o'rtacha")
""" 15. 📺 Televizion ko‘rsatuv vaqti """

# dastur = input("Dastur nomini kiriting: ")
# soat = int(input("Hozirgi soatni kiriting (0–23): "))

# if dastur == "yangiliklar" and 18 <= soat <= 20:
#    print("Tomosha qiling")
# elif dastur == "serial" and 20 <= soat <= 22:
#    print("Qayta ko‘ring")
# else:
#    print("Boshqa ko‘rsatuv tanlang")
""" 16. 🛵 Skuter ijarasi"""

# skuter  = input("Skuter turini kiriting (elektr yoki oddiy): ")
# masofa = int(input("Masofani kiriting (km): "))

# if skuter == "elektr":
#    narx = 2000
# else:
#    narx = 1000

# umumiy_narx = narx * masofa

# if masofa >= 10:
#    umumiy_narx = umumiy_narx * 0.85

# print(f"Umumiy narx: {umumiy_narx} so'm")

""" 17. 🖥️ Komp’yuter ta’miri narxi """

# muomo =  input("Muammo turini kiriting (dasturiy yoki uskunaviy): ")
# qism_narxi = int(input("Qism narxini kiriting: "))

# if muomo == "dasturiy":
#    print("50 000 so'm")
# elif qism_narxi > 100_000:
#    print("150 000 so'm")
# else:
#    print("80 000 so'm")

""" 18. 🌳 Ekologik holat tekshiruvi. """

# ifloslanish = float(input("Ifloslanish darajasini kiriting (%): "))
# shamol = float(input("Shamol tezligini kiriting (km/soat): "))

# if ifloslanish > 50 and shamol < 5:
#    print("Maska kiying")
# elif ifloslanish <= 50 and shamol >= 10:
#    print("Sof havo")
# else:
#    print("Oddiy holat")

""" 19. 🎨 Rasm chizish kursi narxi """


# kurs_turi = input("Kurs turini kiriting (akvarel yoki yog'li): ")
# davomiyligi = int(input("Davomiyligini kiriting (oy): "))

# if kurs_turi == "akvarel":
#    narx = 200_000
# else:
#    narx = 300_000

# umumiy_narx = narx * davomiyligi

# if davomiyligi >= 3:
#    umumiy_narx = umumiy_narx * 0.9

# print(f"Umumiy narx: {umumiy_narx} so'm")

""" 20. 🚪 Eshik qulfi xavfsizligi """

# qulf_turi = input("Qulf turini kiriting (elektron yoki mexanik): ")
# qulf_yoshi = int(input("Qulf yoshini kiriting (yil): "))

# if qulf_turi == "elektron" and qulf_yoshi < 2:
#    print("Yuqori xavfsizlik")
# elif qulf_turi == "mexanik" and qulf_yoshi < 5:
#    print("O‘rtacha xavfsizlik")
# else:
#    print("Past xavfsizlik")

""" 21. 🏠 Uy ijarasi narxi. """

# hudud = input("Hududni kiriting (shahar markazi, shahar cheti yoki boshqa): ")
# xonalar = int(input("Xonalar sonini kiriting: "))

# if hudud == "shahar markazi" and xonalar == 3:
#    print("5 000 000 so'm")
# elif hudud == "shahar cheti" and xonalar == 2:
#    print("3 000 000 so'm")
# else:
#    print("2 000 000 so'm")

""" 22. 🛴 Elektr skuter quvvati """

# quvvat = int(input("Quvvat foizini kiriting: "))
# masofa = int(input("Masofani kiriting (km): "))

# if quvvat < 20 and masofa > 5:
#    print("Zaryadlang")
# elif quvvat < 50 and masofa < 3:
#    print("Ehtiyot bo'ling")
# else:
#    print("Yaxshi holat")

""" 23. 📷 Kamera sifati tekshiruvi """

# ruxsat = int(input("Kamera ruxsatini kiriting (MP): "))
# yoruglik = input("Yorug'lik darajasini kiriting (yaxshi, o'rtacha, yomon): ")

# if ruxsat >= 12 and yoruglik == "yaxshi":
#    print("Yuqori sifat")
# elif ruxsat >= 8 and yoruglik == "o'rtacha":
#    print("O'rtacha sifat")
# else:
#    print("Past sifat")

""" 24. 🏞️ Sayr maslahati """

# masofa = int(input("Masofani kiriting (km): "))
# ob_havo = input("Ob-havo darajasini kiriting (yaxshi, o'rtacha, yomon): ")

# if masofa < 5 and ob_havo == "yaxshi":
#    print("Piyoda")
# elif masofa < 20 and ob_havo == "o'rtacha":
#    print("Velosiped")
# else:
#    print("Avtobus")

""" 25. 📩 E-pochta tekshiruvi """
#
# email = input("Email manzilini kiriting: ")
#
# if len(email) >= 10 and email.endswith("@gmail.com"):
#    print("Qabul qilindi")
# elif len(email) < 10 and email.endswith("@yahoo.com"):
#    print("Qisqa email")
# else:
#    print("Noto‘g‘ri email")

"""  26. 🥗 Ovqat kaloriyasi """

# ovqat = input("Ovqat turini kiriting (salat yoki go'sht): ")
# porsiya = int(input("Porsiya hajmini kiriting (g): "))

# if ovqat == "salat":
#    asosiy_kkal = (porsiya / 100) * 50
# else:
#    asosiy_kkal = (porsiya / 100) * 200

# if porsiya >= 300:
#    yakuniy_kkal = asosiy_kkal * 1.1
# else:
#    yakuniy_kkal = asosiy_kkal

# print(f"Yakuniy kaloriya: {yakuniy_kkal} kkal")

""" 27. 🏦 **Bank krediti foizi """

# summasi = int(input("Kredit summasi (mln so'm): "))
# muddati = int(input("Kredit muddati (yil): "))

# if summasi < 10 and muddati == 1:
#    print("12%")
# elif summasi >= 10 and muddati == 2:
#    print("10%")
# else:
#    print("15%")

""" 28. 🛫Parvoz narxi """

# sinf = input("Sinfni kiriting (biznes yoki ekonom): ")
# masofa = int(input("Masofani kiriting (km): "))

# if sinf == "biznes" and masofa < 1000:
#    asosiy = 1_000_000
# elif sinf == "ekonom" and masofa < 1000:
#    asosiy = 500_000
# elif sinf == "biznes":
#    asosiy = 1_000_000

# if masofa >= 1000:
#   yakuniy = asosiy * 1.2
# else:
#   yakuniy = asosiy

# print(f"Yakuniy narx: {yakuniy} so'm")

""" 29. 🧴 Kosmetika muddati """

# maxsut_turi = input("Mahsulot turini kiriting (lo'shon yoki krem): ").lower()
# ochilgan_oylar = int(input("Ochilganidan o'tgan oylar sonini kiriting: "))

# if maxsut_turi == "lo'shon" and ochilgan_oylar >= 6:
#     print("Ishlatish mumkin emas")
# elif maxsut_turi == "krem" and ochilgan_oylar >= 12:
#     print("Ishlatish mumkin emas")
# else:
#     print("Xavfsiz ishlatishingiz mumkin")


""" 30. 🧵 Kiyim tikish vaqti """

# kiyim_turi = input("Kiyim turini kiriting (bolalar yoki kattalar): ").lower()

# if kiyim_turi == "bolalar":
#     print("2 kun")
# else:
#     olcham = input("O'lchamni kiriting (S, M, L, XL): ").upper()
#     if olcham == "S" or olcham == "M":
#         print("4 kun")
#     else:
#         print("6 kun")

""" 31. 🧁 Tort narxi """

# qavatlar = int(input("Qavatlar sonini kiriting (kamida 1): "))
# meva = input("Meva qo'shasizmi? (ha/yo'q): ").lower()
# shokolad = input("Shokolad qo'shasizmi? (ha/yo'q): ").lower()

# asosiy_narx = 100_000 + (qavatlar - 1) * 50_000
# if meva == "ha":
#     asosiy_narx += 20_000
# if shokolad == "ha":
#     asosiy_narx += 30_000
# print(f"Yakuniy narx: {asosiy_narx} so'm")

""" 32. 🧼 Kir yuvish rejimi """

# maton_turi = input("Maton turini kiriting (paxta/sintetik): ").lower()
# ifloslik = input("Ifloslik darajasini kiriting (yengil/og'ir): ").lower()

# if maton_turi == "paxta" and ifloslik == "yengil":
#     print("Rejim 1")
# elif maton_turi == "sintetik" and ifloslik == "og'ir":
#     print("Rejim 3")
# else:
#     print("Rejim 2")


"""  33. 📚 Kitob janrini aniqlash """

# kitob_nomi = input("Kitob nomini kiriting: ").lower()

# if "sir" in kitob_nomi or "jinoyat" in kitob_nomi:
#     print("Detektiv")
# elif "sevgi" in kitob_nomi or "romantika" in kitob_nomi:
#     print("Romantik")
# elif "kosmos" in kitob_nomi or "kelajak" in kitob_nomi:
#     print("Fantastik")
# else:
#     print("Boshqa")

"""  34. 🎭 Konsert chiptasi narxi """

# chipta_turi = input("Chipta turini kiriting (VIP yoki oddiy): ").lower()
# yosh = int(input("Yoshingizni kiriting: "))

# if chipta_turi == "vip" and yosh > 60:
#     print("50 000 so'm")
# elif chipta_turi == "oddiy" and yosh < 18:
#     print("20 000 so'm")
# else:
#     print("30 000 so'm")

""" 35. 🏪 Do'kon ish vaqti tekshiruvi. """

# kun = input("Kun nomini kiriting (masalan: Dushanba, Seshanba...): ").lower()
# soat = int(input("Hozirgi soatni kiriting (0–23): "))
# ish_kuni = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma']
# dam_kuni = ['shanba', 'yakshanba']

# if kun in ish_kuni and 9 <= soat <= 18:
#     print("Ochiq")
# elif kun in dam_kuni and 10 <= soat <= 16:
#     print("Ochiq")
# else:
#     print("Yopiq")

""" 36. 🌱 O'simlik parvarishi tavsiyasi """

# osimlik_turi = input("O'simlik turini kiriting (gul yoki daraxt): ").lower()
# fasl = input("Faslni kiriting (bahor, yoz, kuz, qish): ").lower()

# if osimlik_turi == "gul" and fasl == "bahor":
#     print("Haftada 3 marta sug'oring")
# elif osimlik_turi == "daraxt" and fasl == "yoz":
#     print("Har kuni sug'oring")
# elif osimlik_turi == "gul" and fasl == "qish":
#     print("Haftada 1 marta sug'oring")
# else:
#     print("Haftada 2 marta sug'oring")

""" 37. 🎭 Teatr tomoshasi uchun joy tavsiyasi """

# budjet = int(input("Budjetni kiriting (so'm): "))
# vip_kerak = input("VIP kerakmi? (ha/yo'q): ").lower()
# yaxshi_korish = input("Yaxshi ko'rish kerakmi? (ha/yo'q): ").lower()

# if budjet > 100_000 and vip_kerak == "ha":
#     print("Birinchi qator VIP")
# elif budjet > 100_000 and vip_kerak == "yo'q":
#     print("Birinchi qator oddiy")
# elif budjet <= 100_000 and yaxshi_korish == "ha":
#     print("O'rta qatorlar")
# else:
#     print("Orqa qatorlar")

""" 38. 📱 Telefon xotirasi tekshiruvi. """

# xotira_foizi = int(input("Xotira bandligi foizini kiriting: "))

# if xotira_foizi >= 95:
#     print("Xotira to'la! Tozalash kerak")
# elif xotira_foizi >= 80:
#     print("Xotira kam qoldi")
# elif xotira_foizi >= 50:
#     print("Xotira yetarli")
# else:
#     print("Xotira bo'sh")

"""" 39. 🎯 O'yin ballini baholash"""

# umumiy_ball = int(input("Umumiy ballni kiriting: "))

# if umumiy_ball >= 90:
#     print("Ustoz")
# elif umumiy_ball >= 70:
#     print("Malakali")
# elif umumiy_ball >= 50:
#     print("O'rta")
# else:
#     print("Boshlang'ich")

""" 40. 🎓 Talaba reytingi """

# ball = int(input("Talabaning umumiy ballini kiriting (0-100): "))

# if 90 <= ball <= 100:
#     print("5 baxo")
# elif 71 <= ball <= 89:
#     print("4 baxo")
# elif 60 <= ball <= 70:
#     print("3 baxo")
# else:
#     print("Ball yetarli emas!")

"""  41. 🚌 Avtobus chipta narxi. """

# yosh = int(input("Yoshingizni kiriting: "))
# talaba = input("Talaba misiz? (ha/yo'q): ").lower()

# if yosh < 7:
#     print("Bepul")
# elif talaba == "ha":
#     print("5000 so'm")
# elif yosh >= 60:
#     print("Chegirma: 3000 so'm")
# else:
#     print("7000 so'm")

"""  42. 🗓️ Yil faslini aniqlash """

# oy = int(input("Oy raqamini kiriting (1-12): "))

# if oy in [12, 1, 2]:
#     print("Qish")
# elif oy in [3, 4, 5]:
#     print("Bahor")
# elif oy in [6, 7, 8]:
#     print("Yoz")
# else:
#     print("Kuz")

"""  43. 📱 Telefon narxini hisoblash """

# model = input("Telefon modelini kiriting (iPhone yoki Samsung): ")
# holat = input("Telefon holatini kiriting (yangi yoki ishlatilgan): ")

# if model == "iPhone" and holat == "yangi":
#     print("Narxi: 1200$")
# elif model == "iPhone" and holat == "ishlatilgan":
#     print("Narxi: 800$")
# elif model == "Samsung" and holat == "yangi":
#     print("Narxi: 900$")
# elif model == "Samsung" and holat == "ishlatilgan":
#     print("Narxi: 600$")
# else:
#     print("Noma'lum model yoki holat.")

"""  44. 🏫 Maktabga qabul """

# yosh = int(input("Yoshingizni kriting: "))
# test = int(input("Test ballini kiriting: "))

# if yosh >= 6 and test >= 70:
#     print("Qabul qilindi")
# else:
#     print("Qabul qilinmadi")

""" 45. 🌐 Internet tezligi tahlili """

# tezlik = int(input("Internet tezligini kiriting (Mbps): "))

# if tezlik < 5:
#     print("Juda sekin")
# elif 5 <= tezlik < 20:
#     print("O'rtacha")
# elif 20 <= tezlik <= 100:
#     print("Tez")
# else:
#     print("Juda tez")

""" 46. 🐶 Uy hayvoni tavsiyasi """

# vaqt = input("Bo'sh vaqtingizni kiriting (kam/ko'p/o'rtacha): ").lower()
# joy = input("Uy joyingizni kiriting (kam/ko'p): ").lower()
# sabr = input("Sabr-toqatingiz bormi? (bor/yo'q): ").lower()

# if vaqt == "kam" and joy == "kam":
#     print("Baliq")
# elif vaqt == "ko'p" and sabr == "bor":
#     print("It")
# else:
#     print("Mushuk")

""" 47. 👔 Ishga qabul sharti """

# yosh = int(input("Yoshingizni kiriting: "))
# tajriba = int(input("Tajriba muddatini kiriting (yil): "))
# ingliz = input("Ingliz tili darajasini kiriting (boshlang'ich, o'rta, yaxshi): ").lower()

# if yosh >= 22 and tajriba >= 2 and (ingliz == "o'rta" or ingliz == "yaxshi"):
#     print("Qabul qilindi")
# else:
#     print("Qabul qilinmadi")

""" 48. 📆 Kabisa yili tekshiruvi """

# yil = int(input("Yilni kiriting: "))

# if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
#     print("Kabisa yil")
# else:
#     print("Kabisa yil emas")

""" 49. 💸 Soliq hisoblagich """

# daromad = float(input("Oylik daromadingizni kiriting (mln so'm): "))

# if daromad <= 1:
#     print("0%")
# elif daromad <= 3:
#     print("10%")
# else:
#     print("20%")

""" 50. 🏪 Chegirma tizimi """

# yosh = int(input("Yoshingizni kiriting: "))
# mahsulot = input("Mahsulot turini kiriting (Oziq-ovqat, Kiyim, Texnika): ")
# if mahsulot.lower() == "oziq-ovqat":
#     print("Chegirma yo'q")
# elif yosh < 12:
#     print("20% chegirma")
# elif yosh > 60:
#     print("15% chegirma")
# else:
#     print("Chegirma mavjud emas")