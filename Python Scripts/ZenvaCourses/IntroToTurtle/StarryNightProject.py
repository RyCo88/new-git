#Create a star system on a black background
    #use randomness for star size and position
    #use for loop to generate a large amount of stars
#Set background to black
#check to see if we've drawn 100 stars(will run 100 times use for loop)
    #if not generate a random x and y coordinate
    #generate random star size
    #draw star
#end
from turtle import *
from random import *
speed(10)
bgcolor('black')
hideturtle()
width=window_width()
height=window_height()
def draw_star(xpos, ypos):
    size=randrange(1,10)
    penup()
    goto(xpos,ypos)
    pendown()
    dot(size, 'white')
for i in range(100):
    xpos=randrange(-width/2,width/2)
    ypos=randrange(-height/2,height/2)
    draw_star(xpos,ypos)
done()