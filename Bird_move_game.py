import turtle
from time import sleep
from random import randint, choice
# Screen setup
screen = turtle.Screen()
screen.setup(1024,620,300,20)
screen.bgcolor("black")
screen.bgpic(r"C:\Neural network\Game\pexels-pixabay-459225.gif")
screen.title("Bird Game")
# out text
text = turtle.Turtle()
text.color("red")
text.penup()
text.hideturtle()
text.setposition(0, 0)



# border
b = turtle.Turtle()
# b.hideturtle()
b.penup()
b.setposition(0,280)
# b.pendown()
b.color("red")
b.write("Score: ".format(0), False, align="center", font=("Arial", 18, "normal"))
# b.speed(10)
# b.pensize(10)
# for l in range(2):
#     b.fd(1024)
#     b.lt(90)
#     b.fd(620)
#     b.lt(90)
# moving object
color = ["blue","#452565","#857496","#359575","#457812","green"]
up_wall =[]
for i in range(14):
    up_wall.append(turtle.Turtle())
location = -510
c = 1
for wall in up_wall:
    s = randint(10,15)
    wall.speed(10)
    if c % 2 != 0:
        y = 310 - s * 10
        wall.penup()
        wall.shape("square")
        wall.color(choice(color))
        wall.setposition(location, y)
        wall.shapesize(s, 2)
        location += 1024 / 6
    if c == 8:
        location = -510
    if c % 2 == 0:
        y = -310 + s * 10
        wall.penup()
        wall.shape("square")
        wall.color(choice(color))
        wall.setposition(location, y)
        wall.shapesize(s, 2)
        location += 1024 / 6

    c += 1

# Player
player = turtle.Turtle()
player.tilt(180)
player.penup()
player.shape("triangle")
player.color("yellow")
player.shapesize(1,2)
def up_move():
    player.sety(player.ycor()+5)
def down_move():
    player.sety(player.ycor()-5)

# key board action
turtle.listen()
turtle.onkeypress(up_move, "space")
turtle.onkey(up_move, "w")
turtle.onkey(down_move, "Left")
turtle.onkeypress(down_move, "s")
# parameter for objects
x = 2.8
height = 620
gap = 200
screen.tracer(x*10)
down_rate = 0.05
Score = 0
while True:
    screen.update()
    if x <= 8:
        x += 0.1
    for obj1 in up_wall:
        obj1.setx(obj1.xcor() + x)
        l1 = randint(10, 15)
        b.undo()
        b.write("Score: {}".format(Score), False, align="center", font=("Arial", 18, "normal"))
        if obj1.xcor() >= 580 and obj1.ycor() > 0:
            obj1.hideturtle()
            y = 310 - l1 * 10
            obj1.shapesize(l1,2)
            obj1.setposition(-580, y)
            obj1.showturtle()
        if obj1.xcor() >= 580 and obj1.ycor() < 0:
            obj1.hideturtle()
            y = -310 + l1 * 10
            obj1.shapesize(l1, 2)
            obj1.setposition(-580, y)
            obj1.showturtle()
        enemy = obj1.get_shapepoly()
        print(enemy[1])
        pl = player.get_shapepoly()
        print(pl[2])
        player.sety(player.ycor() - down_rate)
        if player.ycor() <=  -320:
            text.write("GAME OVER!", False, align="center", font=("Arial", 48, "normal"))
            sleep(2)
            exit()
    Score += 1
turtle.mainloop()


