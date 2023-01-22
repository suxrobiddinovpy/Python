from turtle import Turtle, Screen

oyna = Screen()
oyna.title("Tegib qaytuvchi o'yin")

chiziq = Turtle()
chiziq.color("red")
chiziq.pensize(5)
chiziq.speed(0)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(300, 300)
chiziq.down()
chiziq.goto(300, -300)
chiziq.goto(-300, -300)
chiziq.goto(-300,300)
chiziq.goto(300, 300)

koptok = Turtle()
koptok.shape("circle")
koptok.color("blue")
koptok.up()
koptok.goto(0, 0)

step_x = 4
step_y = 3

while True:
	x, y = koptok.position()

	if x + step_x >  300 or x + step_x <= -300:
		step_x = -step_x
	if x + step_y >  300 or y + step_y <= -300:
		step_y = -step_y

	koptok.goto(x+step_x, y+step_y)

oyna.mainloop()
