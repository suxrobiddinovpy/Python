from datetime import datetime
from tkinter import *

oyna = Tk()
oyna.title("Yoshni topadigan dastur")
oyna.geometry("300x300")

natija = Label(text="Yoshingiz", bg="red")
natija.place(x=90, y=170, width=120, height=40)

yil = Entry()
yil.place(x=80, y=50, width=150, height=30)

def farq():
    bugun = datetime.today()
    natija.config(text=bugun.year - int(yil.get()))

tugma = Button(text="Hisoblash", command=farq)
tugma.place(x=90, y=100, width=120, height=40)

oyna.mainloop()
