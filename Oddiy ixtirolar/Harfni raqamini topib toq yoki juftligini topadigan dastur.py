a=input("Biror harf kiriting  ").lower()
print(a)
if a.isalpha():
    if a=='a' or a=='e' or a=='u' or a=='i' or a=="o`":
        print("Unli harf")
    else:
        print("Undosh harf")
else:
    print("Iltimos harf kiriting")
