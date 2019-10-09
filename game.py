
import random
import pygame


def check_rules():
    proximity_matrix = []

    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    for row in range(0, field_y):
        proximity_row = []
        for column in range(0, field_x):

            neighbours = 0
            for k in range(-1, 2):
                for h in range(-1, 2):
                    if 0 <= row+k < field_y and 0 <= column+h < field_x:
                        if field[row+k][column+h] == 1:
                            if k == 0 and h == 0:
                                continue
                            neighbours = neighbours + 1

            proximity_row.append(neighbours)
        proximity_matrix.append(proximity_row)

    # iteration to check the proximity matrix and update the field consequently
    for row in range(field_y):
        for column in range(field_x):
            if field[row][column] == 1 and (proximity_matrix[row][column] < 2 or proximity_matrix[row][column] > 3):
                field[row][column] = 0
            if field[row][column] == 0 and proximity_matrix[row][column] == 3:
                field[row][column] = 1


# for the CLI version of the game (not used with GUI)
def show_field():
    print("\n")
    for row in field:
        print(row)


def game_loop ():
    pygame.display.set_caption("Conway's Game of Life - Game")
    set_random_field(False)
    pygame.draw.rect(win, (255, 255, 255), (0, 0, display_x, display_y), field_thick)
    pause = False
    run = True
    ref_rate = vel
    while run:
        pygame.time.delay(ref_rate)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not pause:
                pause = True
            elif keys[pygame.K_SPACE] and pause:
                pause = False
            if keys[pygame.K_a]:    # increase velocity
                ref_rate = ref_rate + 10
            if keys[pygame.K_d]:    # decrease velocity
                ref_rate = ref_rate - 10
            if keys[pygame.K_1]:    # random reset
                set_random_field(True)
        if not pause:
            for row in range(0, field_y):
                for col in range(0, field_x):
                    if field[row][col] == 1:
                        pygame.draw.rect(win, (255, 255, 255), (field_thick + dist_y * col, field_thick + dist_x * row, cell_size, cell_size))
                    else:
                        pygame.draw.rect(win, (0, 0, 0), (field_thick + dist_y * col, field_thick + dist_y * row, cell_size, cell_size))

            pygame.display.update()
            check_rules()


def set_random_field(reset):    # random and reset initialization
    if reset:
        for i in range(field_y):
            for n in range(field_x):
                field[i][n] = random.randint(0, 1)
    else:
        for i in range(field_y):
            row = []
            for n in range(field_x):
                row.append(random.randint(0, 1))
            field.append(row)

def set_custom_field():
    for i in range(field_y):
        row = [[0]*field_x]
    field.append(row)




def setup_page():
    pygame.display.set_caption("Conway's Game of Life - Setup")
    button_x = 100
    button_y = 50
    command_bar_x = 0
    command_bar_y = display_y - cmd_size

    button_play = pygame.Rect(display_x/2 - 50, display_y/2 - 25, button_x, button_y)  # left, top width, height
    button_increase = pygame.Rect(command_bar_x, command_bar_y, button_x, button_y)  # left, top width, height
    button_decrease = pygame.Rect(command_bar_x + 200, command_bar_y, button_x, button_y)  # left, top width, height
    button_pause = pygame.Rect(command_bar_x + 400, command_bar_y, button_x, button_y)  # left, top width, height
    button_reset = pygame.Rect(command_bar_x + 600, command_bar_y, button_x, button_y)  # left, top width, height

    # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simply type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom
    pygame.draw.rect(win, [0, 200, 0], button_increase)
    pygame.draw.rect(win, [0, 200, 0], button_decrease)
    pygame.draw.rect(win, [0, 200, 0], button_pause)
    pygame.draw.rect(win, [0, 200, 0], button_reset)

    pygame.draw.rect(win, [0, 200, 0], button_play)  # draw button
    win.blit(font.render('Play!', True, (0, 0, 0)), (display_x/2 - 25, display_y/2 - 13))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if button_play.collidepoint(mouse_pos):
                    # prints current location of mouse
                    win.fill((0, 0, 0))
                    return True




if __name__ == "__main__":
    pygame.init()

    # field parameters
    field = []
    field_x = 120
    field_y = 70

    # cell parameters
    cell_size = 5
    cell_distance = 2
    dist_x = cell_size * cell_distance
    dist_y = cell_size * cell_distance
    vel = 100

    # gui parameters
    field_thick = 5
    display_x = (field_x) * dist_x + field_thick
    display_y = (field_y) * dist_y + field_thick
    cmd_size = 50
    font = pygame.font.SysFont('Arial', 25)

    win = pygame.display.set_mode((display_x, display_y + cmd_size))

    if setup_page():
        game_loop()


