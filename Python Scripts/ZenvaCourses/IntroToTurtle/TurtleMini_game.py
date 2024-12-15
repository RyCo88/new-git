#Create a turtle that can move in 4 directions
    #move with arrow keys
#have end goal
    #reach the ocean
#visual feedback when you reach the goal
    #text 'YOU WIN!'
#beach(orance)ocean(blue)turtle(green)
#background color to orange
#draw the ocean
#move turtle to starting position
#check if move key pressed(listen())
    #if yes move the turtle in that direction
    #check if turtle has reached the ocean
        #if yes hide turtle
        #display 'YOU WIN!'
        #end
from turtle import*
move_distance=20
bgcolor('#D2691E')
penup()
goto(100,400)
pendown()
begin_fill()
color('blue')
goto(500,400)
goto(500,-400)
goto(100,-400)
goto(100,400)
end_fill()
penup()
goto(-400,0)
color('green')
shape('turtle')
def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()
def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()
def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()
def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()
def check_goal():
    if xcor()>100:
        hideturtle()
        color('white')
        write('YOU WIN!')
        penup()
        onkey(None,'Up')
        onkey(None,'Down')
        onkey(None,'Right')
        onkey(None,'Left')
onkey(move_up,'Up')
onkey(move_down,'Down')
onkey(move_right,'Right')
onkey(move_left,'Left')
listen()

done()