from turtle import *




speed(30)
width(7)
color("green")
begin_fill()
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of squar


#drawing a door
forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawing a window
color("blue")
begin_fill()
penup()
goto(150 ,150)
pendown()

right(60)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()


exitonclick()