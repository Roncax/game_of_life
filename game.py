import time
import random

def check_rules():
    proximity_matrix = []

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

            proximity_row.append(neighbours)
        proximity_matrix.append(proximity_row)
    show_field(proximity_matrix)
    for row in range(0, field_size - 1):
        for column in range(0, field_size - 1):
            if (field[row][column] == 1 and (proximity_matrix[row][column] < 2 or proximity_matrix[row][column] > 3)):
                field[row][column] = 0
            if (field[row][column] == 0 and proximity_matrix[row][column] == 3):
                field[row][column] = 1


def show_field(field):
    print("\n")
    for row in field:
        print(row)


if __name__=="__main__":
    field_size = 10
    field = []
    for i in range(1, field_size):
        field.append([random.randint(0,1)] * (field_size-1))
    show_field(field)
    for i in range(2):
        check_rules()
        show_field(field)
        time.sleep(.500)


