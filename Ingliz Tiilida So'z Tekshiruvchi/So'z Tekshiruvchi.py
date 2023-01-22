import tkinter
from tkinter import *
from textblob import TextBlob

oyna = Tk()

oyna.title("So'z Tekshiruvchi")
oyna.geometry("700x400")
oyna.config(bg="#DAE6F6")

def check():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())
    cs=Label(oyna, text="To'g'ri Text Bu: ", font=("poppins", 20), bg="#DAE6F6", fg="#364971")
    cs.place(x=100, y=250)
    spell.config(text=right)

heading = Label(oyna, text="So'z Tekshiruvchi", font=("Trebuchet MS", 30, "bold"), bg="#DAE6F6", fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(oyna, justify="center", width=30, font=("poppins", "25"), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(oyna, text="Tekshiring", font=("arial", 20, "bold"), bg="red", fg="white", command=check)
button.pack()

spell = Label(oyna, font=("poppins", 20), bg="#DAE6F6", fg="#364971")
spell.place(x=350, y=250)

oyna.mainloop()
