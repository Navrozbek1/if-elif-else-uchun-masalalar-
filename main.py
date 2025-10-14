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