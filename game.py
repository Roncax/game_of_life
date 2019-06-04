import time
import os

def field_initialization(n, field):
    for i in range (1, n):
        field.append([0] * (n-1))
        field.append(2)
    print(field)

def check_rules(field):
    print('ok')

def cells_positioning(field):
    field[1][2] = 1
    print("\n".join(str(field)))

def show_field(field):
    os.system('clear')

if __name__=="__main__":
    field_size = 10
    current_field = []
    old_field = []
    new_field = []

    field_initialization(field_size, current_field)
    cells_positioning(current_field)

    while old_field != new_field:
        new_field = check_rules(current_field)
        old_field = current_field
        current_field = new_field
        show_field(current_field)
        time.sleep(.400)

    print("The game is in a stall")

