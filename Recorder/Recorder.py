from email import message
from tkinter import *
from tkinter import messagebox
import sounddevice as sound  # pip install sounddevice
from scipy.io.wavfile import write  # pip install scipy
import time
import wavio as wv  # pip install wavio

oyna = Tk()
oyna.geometry("600x700+400+80")
oyna.resizable(False, False)
oyna.title("Ovoz Yozuvchi")
oyna.configure(bg="#4A4A4A")


def Record():
    global time, temp
    freq = 44100
    dur = int(duration.get())
    recording = sound.rec(dur * freq,
                          samplerate=freq, channels=2)
    sound.wait()
    write("-1", freq, recording)

    # timer

    try:
        temp = int(duration.get())
    except:
        print("Iltimos To'g'ri Kiriting!")
    while temp > 0:
        oyna.update()
        time = sound.sleep(1)
        temp -= 1
    if (temp == 0):
        message.showinfo("Countdown", "Time's up!")
    Label(text=f"{str(temp)}", font="arial 40", width=4, bg="#4A4A4A").place(x=240, y=590)


# icon

image_icon = PhotoImage(file="Record.png")
oyna.iconphoto(False, image_icon)

# logo

photo = PhotoImage(file="Record.png")
myimage = Label(image=photo, bg="#4A4A4A")
myimage.pack(padx=5, pady=5)

# name

Label(text="Ovoz Yozuvchi", font="arial 30 bold", bg="#4A4A4A", fg="white").pack()

# entry box

duration = StringVar()
entry = Entry(oyna, textvariable=duration, font="arial 30 bold", width=15).pack(pady=10)
Label(text="Vaqtni Sekundlarda Yozing", font="arial 15", bg="#4A4A4A", fg="white").pack()

# button

recocrd = Button(oyna, font="arial 20 bold", text="YOZISH", bg="#111111", fg="white", border=0, command=Record).pack(
    pady=30)

oyna.mainloop()
