from random import randint

a = randint(0, 10)
b = randint(0, 10)

c = int(input("{} + {} = ".format(a, b)))
if c == (a + b):
        print("To'g'ri topdingiz, ofarin!")
else:
   print("Xato! Qayta urunib ko'ring")
