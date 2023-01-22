a = int(input("Yilni kiriting! ==> "))

if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("kabisa yili to'g'ri tanlandi")
else:
    print("Kabisa yili xato kiritildi!")

