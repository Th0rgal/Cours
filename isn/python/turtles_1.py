from turtle import *

def polygon(side_amount, side_size):
    angle = 360/side_amount
    for i in range (side_amount):
        fd(side_size)
        rt(angle)

def mission2(line_size, side_amount, side_size):
    fd(line_size)
    pre_angle = 90 - 180/side_amount
    lt(pre_angle)
    polygon(side_amount, side_size)
    rt(pre_angle)
    bk(line_size)

def mission3(side_size, side_amount):
    if side_amount > 50:
        color("Red")
    else:
        color("Blue")
    mission2(60, side_amount, side_size)

def figure(branches, branch_length, polygon_sides_amount, polygon_side_size):
    angle = 360/branches
    for i in range (branches):
        mission2(branch_length, polygon_sides_amount, polygon_side_size)
        rt(angle)

pendown()

figure(5, 100, 3, 50)
mainloop()