from  turtle import Turtle, Screen
oyna=Screen()
oyna.title('mening oynam')


tusiq=Turtle()
tusiq.color('red')
tusiq.pensize(3)
tusiq.speed(0)
tusiq.hideturtle()
tusiq.up()
tusiq.goto(50,-160)
tusiq.down()
tusiq.goto(50,-196)
tusiq.goto(-70,-196)
tusiq.goto(-70,-160)
tusiq.goto(50, -160)


chiziq=Turtle()
chiziq.color('blue')
chiziq.pensize(5)
chiziq.speed(0)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(200,200)
chiziq.down()
chiziq.goto(200,-200)
chiziq.goto(-200,-200)
chiziq.goto(-200,200)
chiziq.goto(200,200)
koptok=Turtle()
koptok.shape('circle')
koptok.up()
koptok.goto(0,0)
koptok.color('red')
step_x=2.1
step_y=5
while True:
	x,y=koptok.position()
	if x+step_x>=200 or x+step_x<=-200:
		step_x=-step_x
	elif y+step_y>=200 or y+step_y<=-200:
		step_y=-step_y

	elif y+step_y<=-160 and x+step_x<=50 and x+step_x>=-70  :
		break
	
	koptok.goto(x+step_x, y+step_y)



oyna.mainloop()