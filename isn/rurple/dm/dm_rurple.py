#réalisé par Emma et Thomas
import random

angles = 0
beepers = 0
changed = False

def turn(times):
    for i in range (times):
        turn_left()

def move_and_pickup():
    global beepers
    if front_is_clear():
        move()
    if on_beeper():
        pick_beeper()
        beepers += 1

def browse(counter):
    global angles
    move_and_pickup()
    orientation = 0
    if right_is_clear():
        orientation = 3 # turn right
    elif not front_is_clear():
        if left_is_clear():
            orientation = 1 # turn left
            angles += 1
        else:
            orientation = 2 # go back
    if orientation:
        turn(orientation)
        """ So basically we add 1 when we turn right
        and substract one when we turn left """
        counter += orientation-2
    if abs(counter) == 4:
        return
    browse(counter)

def random_browse():
    global beepers
    global angles
    possible_moves = []
    if front_is_clear():
        possible_moves.append(0)
    if right_is_clear():
        possible_moves.append(3)
    if left_is_clear():
        possible_moves.append(1)
    if not possible_moves:
        possible_moves.append(2)
    for i in range(random.choice(possible_moves)):
        turn_left()
    move_and_pickup()
    if not beepers == angles:
        random_browse()
    else:
        while front_is_clear():
            move()
        turn_left()
        return 
def final_browse():
    global beepers
    orientation = 2
    if right_is_clear():
        orientation = 3
    elif front_is_clear():
        orientation = 0
    elif left_is_clear():
        orientation = 1
        put_beeper()
        beepers -= 1
    turn(orientation)
    move()
    if beepers != 0:
        final_browse()
#permet de compter les angles
browse(0)
#permet de recup autant de beepers qu'il y a d'angles 
random_browse()
final_browse()
turn_off()