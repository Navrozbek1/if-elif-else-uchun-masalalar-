""" Ichma-ich shart operatorlaridan masalalar! """

""" Masala 1: Baho tizimi """

# ball = int(input("Ballni kiriting (0-100): "))

# if ball < 0 or ball > 100:
#     print("Xato: Ball 0 dan 100 gacha bo‘lishi kerak.")
# elif ball >= 90:
#     print("A")
# elif ball >= 80:
#     print("B")
# elif ball >= 70:
#     print("C")
# elif ball >= 60:
#     print("D")
# else:
#     print("F")

""" Masala 2: Yosh va daromad bo‘yicha soliq """

# yosh = int(input("Yoshingizni kiriting: "))
# daromad = float(input("Daromadingizni kiriting: "))

# if yosh < 0 or yosh > 120 or daromad < 0:
#     print("Xato: Yosh 0-120 oralig‘ida, daromad musbat bo‘lishi kerak.")
# elif yosh < 18:
#     print("Soliq: 0%")
# elif yosh <= 60:
#     if daromad > 5000:
#         print("Soliq: 20%")
#     else:
#         print("Soliq: 10%")
# else:
#     print("Soliq: 5%")

""" Masala 3: Kun va vaqt bo‘yicha ish rejimi """

# kun = int(input("Hafta kunini kiriting (1-7): "))
# soat = int(input("Soatni kiriting (0-23): "))

# if kun < 1 or kun > 7 or soat < 0 or soat > 23:
# 	print("Xato: Kun 1-7, soat 0-23 oralig‘ida bo‘lishi kerak.")
# elif kun == 6 or kun == 7:
# 	print("Dam olish kuni")
# else:
# 	if 9 <= soat <= 17:
# 		print("Ish vaqti")
# 	else:
# 		print("Ish vaqtidan tashqari")

""" Masala 4: Iqlim sharoitlari """

# harorat = float(input("Haroratni kiriting (°C): "))
# yomgir = input("Yomg‘ir yog‘ayotganmi? (ha/yo‘q): ").strip().lower() == 'ha'
# if harorat < -50 or harorat > 60:
#     print("Xato: Harorat –50°C dan 60°C gacha bo‘lishi kerak.")
# elif harorat < 0:
#     print("Qor yog‘ishi mumkin")
# elif harorat <= 20:
#     if yomgir:
#         print("Yomg‘irli va sovuq")
#     else:
#         print("Sovuq, lekin quruq")
# else:
#     print("Issiq")

""" Masala 5: Transport tanlash """

# masofa = float(input("Masofani kiriting (km): "))
# vaqt = float(input("Vaqtni kiriting (soat): "))

# if masofa < 0 or vaqt < 0:
#     print("Xato: Masofa va vaqt manfiy bo‘lmasligi kerak.")
# else:
#     if masofa < 5:
#         print("Piyoda boring")
#     elif masofa <= 50:
#         if vaqt > 1:
#             print("Avtobus")
#         else:
#             print("Velosiped")
#     else:
#         print("Samolyot")

""" Masala 6: Bank krediti """

# yosh = int(input("Yoshingizni kiriting: "))
# daromad = float(input("Daromadingizni kiriting: "))
# kredit_summa = float(input("Kredit summasini kiriting: "))

# if yosh < 18 or yosh > 100 or daromad < 0 or kredit_summa <= 0:
#     print("Xato: Yosh 18-100 oralig'ida, daromad va kredit summasi musbat bo'lishi kerak.")
# else:
#     if yosh < 21:
#         print("Kredit berilmaydi")
#     elif yosh <= 60:
#         if daromad > kredit_summa * 0.2:
#             print("Kredit tasdiqlandi")
#         else:
#             print("Kredit rad etildi")
#     else:
#         print("Kredit faqat maxsus shartlarda") 

""" Masala 7: Restoran menyusi """

# ovqat_turi = input("Ovqat turini kiriting (go'sht, baliq, vegetarian): ").lower()
# narx = float(input("Narxni kiriting: "))

# if narx <= 0:
#     print("Xato: Narx musbat bo'lishi kerak.")
# else:
#     if ovqat_turi == "go'sht":
#         if narx > 50:
#             print("Premium go'shtli taom")
#         else:
#             print("Oddiy go'shtli taom")
#     elif ovqat_turi == "baliq":
#         print("Baliqli taom")
#     elif ovqat_turi == "vegetarian":
#         if narx > 30:
#             print("Premium vegetarian")
#         else:
#             print("Oddiy vegetarian")
#     else:
#         print("Xato: Noto'g'ri ovqat turi.")

""" Masala 8: Talaba stipendiyasi """

# baho = float(input("Bahoni kiriting (0-5.0): "))
# daromad = float(input("Daromadingizni kiriting: "))

# if baho < 0 or baho > 5.0 or daromad < 0:
#     print("Xato: Baho 0-5.0 oralig'ida, daromad musbat bo'lishi kerak.")
# elif baho < 3.0:
#     print("Stipendiya yo'q")
# elif baho < 4.0:
#     if daromad < 1000:
#         print("Oddiy stipendiya")
#     else:
#         print("Stipendiya yo'q")
# else:
#     if daromad < 2000:
#         print("Yuqori stipendiya")
#     else:
#         print("Stipendiya yo'q")

""" Masala 9: Telefon tarifi. """

# daqiqalar = int(input("Daqiqalarni kiriting: "))
# internet = float(input("Internet miqdorini kiriting (GB): "))

# if daqiqalar < 0 or internet < 0:
#     print("Xato: Daqiqalar va internet manfiy bo'lmasligi kerak.")
# else:
#     if daqiqalar < 100:
#         print("Mini tarif")
#     elif daqiqalar <= 500:
#         if internet > 5:
#             print("Standart tarif")
#         else:
#             print("Ekonom tarif")
#     else:
#         print("Premium tarif")

""" Masala 10: Ob-havo bo'yicha maslahat """

# harorat = float(input("Haroratni kiriting (°C): "))
# shamol = float(input("Shamol tezligini kiriting (m/s): "))

# if harorat < -50 or harorat > 50 or shamol < 0:
#     print("Xato: Harorat –50°C dan 50°C gacha, shamol manfiy emas.")
# elif harorat < 10 and shamol > 10:
#     print("Uyda qoling")
# elif harorat <= 25:
#     if shamol < 5:
#         print("Sayr qiling")
#     else:
#         print("Ehtiyot bo'ling")
# else:
#     print("Suv iching")

""" Masala 11: Ish haqi """

# saat = int(input("Ish soatlarini kiriting: "))
# tajriba = float(input("Tajribangizni kiriting (yil): "))

# if saat < 0 or tajriba < 0:
#     print("Xato: Soat va tajriba manfiy bo'lmasligi kerak.")
# else:
#     if tajriba < 1:
#         ish_haq = saat * 10
#     elif tajriba <= 5:
#         if saat > 40:
#             ish_haq = saat * 15
#         else:
#             ish_haq = saat * 12
#     else:
#         ish_haq = saat * 20

#     print(f"Umumiy ish haqi: ${ish_haq}")

""" Masala 12: Yil fasli. """

# oy = int(input("Oy raqamini kiriting (1-12): "))
# harorat = float(input("Haroratni kiriting (°C): "))

# if oy < 1 or oy > 12 or harorat < -50 or harorat > 50:
#     print("Xato: Oy 1-12, harorat –50°C dan 50°C gacha bo'lishi kerak.")
# else:
#     if oy == 12 or oy == 1 or oy == 2:
#         print("Qish")
#     elif 3 <= oy <= 5:
#         if harorat > 15:
#             print("Iliq bahor")
#         else:
#             print("Sovuq bahor")
#     elif 6 <= oy <= 8:
#         print("Yoz")
#     else:
#         print("Kuz")

""" Masala 13: Chegirma tizimi """

# xarid_summa = float(input("Xarid summasini kiriting ($): "))
# doimiy_mijoz = input("Siz doimiy mijozmisiz? (ha/yo'q): ").lower() == 'ha'

# if xarid_summa <= 0:
#     print("Xato: Summa musbat bo'lishi kerak.")
# else:
#     if xarid_summa < 100:
#         chegirma = 0
#     elif xarid_summa <= 500:
#         if doimiy_mijoz:
#             chegirma = 10
#         else:
#             chegirma = 5
#     else:
#         chegirma = 15

#     print(f"Chegirma: {chegirma}%")

""" Masala 14: Internet tezligi """

# tezlik = float(input("Internet tezligini kiriting (Mb/s): "))
# hajm = float(input("Yuklash hajmini kiriting (MB): "))

# if tezlik <= 0 or hajm <= 0:
#     print("Xato: Tezlik va hajm musbat bo'lishi kerak.")
# elif tezlik < 10:
#     print("Yuklash sekin")
# elif tezlik <= 50:
#     if hajm > 1000:
#         print("O'rtacha yuklash")
#     else:
#         print("Tez yuklash")
# else:
#     print("Juda tez yuklash")

""" Masala 15: Sport musobaqasi """

# ball = int(input("Ballni kiriting (0-100): "))
# jins = input("Jinsingizni kiriting (erkak/ayol): ").lower()

# if ball < 0 or ball > 100:
#     print("Xato: Ball 0 dan 100 gacha bo‘lishi kerak.")
# else:
#     if jins == "erkak":
#         if ball > 80:
#             print("Finalga chiqdi")
#         else:
#             print("Saralashdan o'tmadi")
#     elif jins == "ayol":
#         if ball > 75:
#             print("Finalga chiqdi")
#         else:
#             print("Saralashdan o'tmadi")
#     else:
#         print("Xato: Noto'g'ri jins kiritildi.")


""" Masala 16: Elektroenergiya to'lovi """

# istemol = float(input("Iste'molni kiriting (kVt): "))
# vaqt = input("Vaqtni kiriting (kecha/kunduz): ").lower()

# if istemol < 0:
#     print("Xato: Iste'mol manfiy bo'lmasligi kerak.")
# else:
#     if vaqt == "kecha":
#         tolov = istemol * 0.05
#         print(f"Elektr energiya to'lovi: ${tolov}")
#     elif vaqt == "kunduz":
#         if istemol > 100:
#             tolov = istemol * 0.1
#         else:
#             tolov = istemol * 0.08
#         print(f"Elektr energiya to'lovi: ${tolov}")
#     else:
#         print("Xato: Vaqt faqat 'kecha' yoki 'kunduz' bo'lishi kerak.")

""" Masala 17: Talaba imtihon natijasi """

# fan1 = int(input("Birinchi fan ballini kiriting (0-100): "))
# fan2 = int(input("Ikkinchi fan ballini kiriting (0-100): "))

# if fan1 < 0 or fan1 > 100 or fan2 < 0 or fan2 > 100:
#     print("Xato: Ballar 0 dan 100 gacha bo'lishi kerak.")
# elif fan1 > 80 and fan2 > 80:
#     print("A'lo")
# elif (fan1 > 80 and fan2 > 60) or (fan2 > 80 and fan1 > 60):
#     print("Yaxshi")
# else:
#     print("Qoniqarli")

""" Masala 18: Yo'l harakati qoidalari """

# tezlik = float(input("Tezlikni kiriting (km/s): "))
# guvohnoma = input("Guvohnomangiz bormi? (ha/yo'q): ").lower() == 'ha'

# if tezlik < 0:
#     print("Xato: Tezlik manfiy bo'lmasligi kerak.")
# else:
#     if not guvohnoma:
#         print("Jarima: 100$")
#     else:
#         if tezlik > 60:
#             print("Jarima: 50$")
#         else:
#             print("Jarima yo'q")

""" Masala 19: Do'kon chegirmasi. """

# summa = float(input("Xarid summasini kiriting ($): "))
# mijoz_turi = input("Mijoz turini kiriting (oddiy/premium): ").lower()

# if summa <= 0:
#     print("Xato: Summa musbat bo'lishi kerak.")
# else:
#     if mijoz_turi == "oddiy":
#         if summa > 200:
#             chegirma = 5
#         else:
#             chegirma = 0
#     elif mijoz_turi == "premium":
#         if summa > 100:
#             chegirma = 10
#         else:
#             chegirma = 3
#     else:
#         print("Xato: Mijoz turi noto'g'ri.")
#         chegirma = None

#     if chegirma is not None:
#         print(f"Chegirma: {chegirma}%")

""" Masala 20: Universitet qabul """

# ball = int(input("Ballni kiriting (0-100): "))
# yashash_joyi = input("Yashash joyingizni kiriting (shahar/qishloq): ").lower()

# if ball < 0 or ball > 100:
#     print("Xato: Ball 0 dan 100 gacha bo'lishi kerak.")
# else:
#     if ball > 90:
#         if yashash_joyi == "shahar":
#             print("Grant")
#         elif yashash_joyi == "qishloq":
#             print("Shartnoma")
#         else:
#             print("Xato: Yashash joyi noto'g'ri.")
#     elif ball >= 70:
#         print("Shartnoma")
#     else:
#         print("Qabul qilinmadi")


""" Masala 21: Tibbiy sug'urta to'lovi """


# yosh = int(input("Yoshingizni kiriting: "))
# sogliq = input("Sog'liq holatingizni kiriting (yaxshi/o'rtacha/yomon): ").strip().lower()
# oila_azo = int(input("Oila a'zolari sonini kiriting: "))

# if yosh < 0 or yosh > 120 or oila_azo < 1:
#     print("Xato: Yosh 0-120, oila a'zolari 1 dan kam bo'lmasligi kerak.")
# else:
#     if yosh < 18:
#         tolov = 0
#     elif yosh <= 60:
#         if sogliq == "yaxshi" and oila_azo < 3:
#             tolov = 100
#         else:
#             tolov = 150
#     else:
#         if sogliq == "yomon":
#             tolov = 300
#         else:
#             tolov = 200

#     print(f"Sug'urta to'lovi: ${tolov}")

""" Masala 22: Avtomobil ijarasi. """

# aftomobil_turi = input("Avtomobil turini kiriting (ekonom/premium): ").lower()
# kunlar = int(input("Ijara kunlarini kiriting: "))
# tajriba = int(input("Haydovchilik tajribangizni kiriting (yil): "))

# if kunlar < 1 or tajriba < 0:
#     print("Xato: Kunlar 1 dan kam emas, tajriba manfiy emas.")
# else:
#     if tajriba < 2:
#         print("Ijaraga berilmaydi")
#     else:
#         if aftomobil_turi == "ekonom":
#             if kunlar > 7:
#                 tolov = kunlar * 20
#             else:
#                 tolov = kunlar * 25
#         elif aftomobil_turi == "premium":
#             if tajriba > 5:
#                 tolov = kunlar * 50
#             else:
#                 tolov = kunlar * 70
#         else:
#             print("Xato: Avtomobil turi noto'g'ri.")
#             tolov = None

#         if tolov is not None:
#             print(f"Ijara to'lovi: ${tolov}")

""" Masala 23: O'quv kursi narxi """

# kurs_turi = input("Kurs turini kiriting (online/offline): ").lower()
# davomiylik = int(input("Davomiylikni kiriting (soat): "))
# talaba_holati = input("Talaba holatini kiriting (talaba/ishchi): ").lower()

# if davomiylik < 1:
#     print("Xato: Davomiylik 1 soatdan kam bo'lmasligi kerak.")
# else:
#     if kurs_turi == "online":
#         if talaba_holati == "talaba" and davomiylik > 20:
#             tolov = davomiylik * 5
#         else:
#             tolov = davomiylik * 7
#     elif kurs_turi == "offline":
#         if davomiylik > 30:
#             tolov = davomiylik * 10
#         else:
#             tolov = davomiylik * 12
#     else:
#         print("Xato: Kurs turi noto'g'ri.")
#         tolov = None

#     if tolov is not None:
#         print(f"Kurs to'lovi: ${tolov}")

""" Masala 24: Ekologik to'lov """

# yonilgi_turi = input("Yonilg'i turini kiriting (benzin/dizel/elektr): ").lower()
# yillik_masofa = float(input("Yillik masofani kiriting (km): "))
# emissiya_darajasi = input("Emissiya darajasini kiriting (past/o'rtacha/yuqori): ").strip().lower()

# if yillik_masofa < 0:
#     print("Xato: Masofa manfiy bo'lmasligi kerak.")
# else:
#     if yonilgi_turi == "elektr":
#         tolov = 0
#     elif yonilgi_turi == "benzin":
#         if emissiya_darajasi == "yuqori" and yillik_masofa > 10000:
#             tolov = yillik_masofa * 0.05
#         else:
#             tolov = yillik_masofa * 0.03
#     elif yonilgi_turi == "dizel":
#         if emissiya_darajasi == "o'rtacha" or emissiya_darajasi == "yuqori":
#             tolov = yillik_masofa * 0.07
#         else:
#             tolov = yillik_masofa * 0.04
#     else:
#         print("Xato: Yonilg'i turi noto'g'ri.")
#         tolov = None

#     if tolov is not None:
#         print(f"Ekologik to'lov: ${tolov}")

""" Masala 25: Fitness klubi a'zoligi """

# yosh = int(input("Yoshingizni kiriting: "))
# mashgulot = input("Mashg'ulot turini kiriting (yoga/fitness/boks): ").strip().lower()
# muddat = int(input("A'zolik muddatini kiriting (oy): "))

# if yosh < 10 or muddat < 1:
#     print("Xato: Yosh kamida 10, muddat 1 oydan kam emas.")
# else:
#     if yosh < 16:
#         print("A'zolik taqiqlanadi")
#     else:
#         if mashgulot == "yoga":
#             if muddat > 6:
#                 tolov = muddat * 30
#             else:
#                 tolov = muddat * 40
#         elif mashgulot == "fitness":
#             if yosh > 30:
#                 tolov = muddat * 50
#             else:
#                 tolov = muddat * 45
#         elif mashgulot == "boks":
#             tolov = muddat * 60
#         else:
#             print("Xato: Mashg'ulot turi noto'g'ri.")
#             tolov = None

#         if tolov is not None:
#             print(f"A'zolik to'lovi: ${tolov}")