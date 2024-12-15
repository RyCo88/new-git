from turtle import *
def move_and_turn(angle):
    forward(50)
    right(angle)
turns=int(input())
angle=360//turns
for i in range(turns):
    move_and_turn(angle)
done()