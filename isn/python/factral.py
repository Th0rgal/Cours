from turtle import *


def fractal(side):
    rt(120)
    for i in range (3):
        fd(side)
        rt(120)
    fd(side/2)
    fractal(side/2)

fractal(150)
mainloop()