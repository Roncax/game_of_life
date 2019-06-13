import time
import os

def field_initialization(n, field):
    for i in range(1, n):
        field.append([0] * (n-1))

def check_rules(field):

    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    for i in range(0, 10):
        for j in range(0, 10):
            neighbours = 0
            for k in range (-1,1):
                for h in range(-1, 1):
                    if i+k > 0 and i+k<9 and j+k > 0 and j+k<9:
                        if field[i+k][j+h] == 1:
                            neighbours = neighbours + 1
            if neighbours == 0:
                print("in cell " + str(i) + ", " + str(j) + " there are no neighbours")
            else:
                print("in cell " + str(i) + ", " + str(j) + " there are " + str(neighbours) + " neighbours")


def cells_positioning(field):
    field[1][2] = 1
    field[5][6] = 1
    field[4][9] = 1
    field[1][1] = 1


def show_field(field):
    for row in field:
        print(row)

if __name__=="__main__":
    field_size = 15
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
    cells_positioning(current_field)
    show_field(current_field)
    check_rules(current_field)

