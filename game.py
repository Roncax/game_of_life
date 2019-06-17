import time
import os

def field_initialization(n, field):
    for i in range(1, n):
        field.append([0] * (n-1))

def check_rules(field):
    proximity_matrix = []

    new_field = field
    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    for row in range(0, field_size - 1):
        proximity_row = []
        for column in range(0, field_size - 1):

            neighbours = 0
            for k in range(-1, 2):
                for h in range(-1, 2):
                    if 0 <= row+k < field_size-1 and 0 <= column+h < field_size-1:
                        if field[row+k][column+h] == 1:
                            if k == 0 and h == 0:
                                continue
                            neighbours = neighbours + 1

            if (field[row][column] == 1 and (neighbours < 2 or neighbours > 3)):
                new_field[row][column] = 0
            if (field[row][column] == 0 and neighbours == 3):
                new_field[row][column] = 1


            proximity_row.append(neighbours)
        proximity_matrix.append(proximity_row)
    show_field(proximity_matrix)
    show_field(new_field)





def cells_positioning(field):
    for row in range(0, field_size-1, 2):
        for elem in range(0, field_size-1):
            field[row][elem] = 1
    field[1][2] = 1
    field[1][3] = 1
    field[1][1] = 1
    field[5][6] = 1
    field[4][9] = 1

def show_field(field):
    print("\n")
    for row in field:
        print(row)

if __name__=="__main__":
    field_size = 30
    current_field = []
    old_field = []
    new_field = []

    field_initialization(field_size, current_field)
    field_initialization(field_size, old_field)
    field_initialization(field_size, new_field)
    cells_positioning(current_field)

# TODO: verificare il passaggio di parametri in python e modificare il codice sotto di conseguenza
    while old_field != new_field:
        check_rules(current_field)
        old_field = current_field
        current_field = new_field
        show_field(current_field)
        time.sleep(.400)

    print("The game is in a stall")
    cells_positioning(current_field)
    show_field(current_field)
    check_rules(current_field)

