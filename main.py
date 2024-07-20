from stanfordkarel import *

def main():
    find_the_center()

def find_the_center():
    find_row_midpoint()
    find_column_midpoint()

def find_column_midpoint():
    check_height()
    fill_column()
    clear_column()
    find_the_col_midpoint()

def fill_column():
    if beepers_present():
        pick_beeper()
        turn_around()
    else:
        while no_beepers_present():
            check_front_beeper()
            fill_middle()
    turn_around()
    move()

def clear_column():
    if front_is_blocked():
        turn_around()
    else:
        move()
        clear_row_first_part()
        clear_row_second_part()

def find_the_col_midpoint():
    while no_beepers_present():
        move()
    turn_right()

def check_height():
    turn_left()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    move()

def find_row_midpoint():
    check_width()
    fill_row()
    go_to_middle()
    clear_row()
    find_the_midpoint()

def find_the_midpoint():
    while no_beepers_present():
        move()
    while not_facing_east():
        turn_left()

def clear_row():
    if front_is_blocked():
        turn_around()
    else:
        move()
        clear_row_first_part()
        clear_row_second_part()

def clear_row_first_part():
    while front_is_clear():
        pick_beeper()
        move()
    pick_beeper()
    turn_around()

def clear_row_second_part():
    while no_beepers_present():
        move()
    move()
    while front_is_clear():
        pick_beeper()
        move()
    pick_beeper()
    turn_around()

def go_to_middle():
    turn_around()
    if front_is_blocked():
        turn_around()
        move()
    else:
        move()

def fill_row():
    if beepers_present():
        pick_beeper()
        turn_around()
    else:
        while no_beepers_present():
            check_front_beeper()
            fill_middle()

def check_width():
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    put_beeper()
    move()

def check_front_beeper():
    if beepers_present():
        move()
    while no_beepers_present():
        move()
    turn_around()
    move()

def fill_middle():
    if no_beepers_present():
        put_beeper()
        move()
   
def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == "__main__":
    run_karel_program()