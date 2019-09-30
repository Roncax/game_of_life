import random
import pygame


def check_rules():
    proximity_matrix = []

    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    for row in range(0, field_x - 1):
        proximity_row = []
        for column in range(0, field_x - 1):

            neighbours = 0
            for k in range(-1, 2):
                for h in range(-1, 2):
                    if 0 <= row+k < field_x-1 and 0 <= column+h < field_x-1:
                        if field[row+k][column+h] == 1:
                            if k == 0 and h == 0:
                                continue
                            neighbours = neighbours + 1

            proximity_row.append(neighbours)
        proximity_matrix.append(proximity_row)
     #show_field(proximity_matrix)

    #iteration to check the proximity matrix and update the field consequently
    for row in range(0, field_x - 1):
        for column in range(0, field_y - 1):
            if (field[row][column] == 1 and (proximity_matrix[row][column] < 2 or proximity_matrix[row][column] > 3)):
                field[row][column] = 0
            if (field[row][column] == 0 and proximity_matrix[row][column] == 3):
                field[row][column] = 1


# for the CLI version of the game
def show_field(field):
    '''
    print("\n")
    for row in field:
        print(row)
    '''


if __name__=="__main__":

    field_x = 30
    field_y = 30
    field = []
    cell_size = 4
    x =  cell_size * 3 # X distance between cells
    y = cell_size * 2  # Y distance between cells

    display_x = field_x * 10
    display_y = field_y * 10
    pygame.init()
    win = pygame.display.set_mode((display_x, display_y))
    pygame.display.set_caption("Conway's Game of Life")

    for i in range(1, field_x):
        field.append([random.randint(0,1)] * (field_x-1))
    show_field(field)

    pause = False
    run = True
    while run:
        pygame.time.delay(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not pause:
                pause = True
            elif keys[pygame.K_SPACE] and pause:
                pause = False

        if not pause:
            for row in range(0, field_x - 1):
                for col in range(0, field_y - 1):
                    if field[row][col] == 1:
                        pygame.draw.rect(win, (255, 255, 255), (x * row, y * col, cell_size, cell_size))
                    else:
                        pygame.draw.rect(win, (0, 0, 0), (x * row, y * col, cell_size, cell_size))

            pygame.display.update()
            check_rules()


