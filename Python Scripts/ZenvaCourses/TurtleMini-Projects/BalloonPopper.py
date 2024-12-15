#Detect Inputs
#Require multiple inputs to pop the balloon
#Utilize Variables Conditions and Functions
#Draw the balloon
#check if up key is pressed
    #if pressed is it at max size?
        #if yes clear balloon write POP!
    #elif not max size
        #increase balloon size
#end
from turtle import *
diameter=40
pop_diameter=100
def draw_balloon():
    color('red')
    dot(diameter)

def inflate_balloon():
    global diameter
    diameter+=10
    draw_balloon()

    if diameter>=pop_diameter:
        clear()
        diameter=40
        write("POP!")

draw_balloon()
onkey(inflate_balloon,"Up")
listen()
done()