# Advent of Code, D8_2016

INPUT = """rect 1x1
rotate row y=0 by 10
rect 1x1
rotate row y=0 by 10
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 4
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=1 by 12
rotate row y=0 by 10
rotate column x=0 by 1
rect 9x1
rotate column x=7 by 1
rotate row y=1 by 3
rotate row y=0 by 2
rect 1x2
rotate row y=1 by 3
rotate row y=0 by 1
rect 1x3
rotate column x=35 by 1
rotate column x=5 by 2
rotate row y=2 by 5
rotate row y=1 by 5
rotate row y=0 by 2
rect 1x3
rotate row y=2 by 8
rotate row y=1 by 10
rotate row y=0 by 5
rotate column x=5 by 1
rotate column x=0 by 1
rect 6x1
rotate row y=2 by 7
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate column x=40 by 2
rotate row y=2 by 10
rotate row y=0 by 12
rotate column x=5 by 1
rotate column x=0 by 1
rect 9x1
rotate column x=43 by 1
rotate column x=40 by 2
rotate column x=38 by 1
rotate column x=15 by 1
rotate row y=3 by 35
rotate row y=2 by 35
rotate row y=1 by 32
rotate row y=0 by 40
rotate column x=32 by 1
rotate column x=29 by 1
rotate column x=27 by 1
rotate column x=25 by 1
rotate column x=23 by 2
rotate column x=22 by 1
rotate column x=21 by 3
rotate column x=20 by 1
rotate column x=18 by 3
rotate column x=17 by 1
rotate column x=15 by 1
rotate column x=14 by 1
rotate column x=12 by 1
rotate column x=11 by 3
rotate column x=10 by 1
rotate column x=9 by 1
rotate column x=8 by 2
rotate column x=7 by 1
rotate column x=4 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 34x1
rotate column x=44 by 1
rotate column x=24 by 1
rotate column x=19 by 1
rotate row y=1 by 8
rotate row y=0 by 10
rotate column x=8 by 1
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=5 by 2
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=0 by 40
rotate column x=43 by 1
rotate row y=4 by 10
rotate row y=3 by 10
rotate row y=2 by 5
rotate row y=1 by 10
rotate row y=0 by 15
rotate column x=7 by 2
rotate column x=6 by 3
rotate column x=5 by 2
rotate column x=3 by 2
rotate column x=2 by 4
rotate column x=0 by 2
rect 9x2
rotate row y=3 by 47
rotate row y=0 by 10
rotate column x=42 by 3
rotate column x=39 by 4
rotate column x=34 by 3
rotate column x=32 by 3
rotate column x=29 by 3
rotate column x=22 by 3
rotate column x=19 by 3
rotate column x=14 by 4
rotate column x=4 by 3
rotate row y=4 by 3
rotate row y=3 by 8
rotate row y=1 by 5
rotate column x=2 by 3
rotate column x=1 by 3
rotate column x=0 by 2
rect 3x2
rotate row y=4 by 8
rotate column x=45 by 1
rotate column x=40 by 5
rotate column x=26 by 3
rotate column x=25 by 5
rotate column x=15 by 5
rotate column x=10 by 5
rotate column x=7 by 5
rotate row y=5 by 35
rotate row y=4 by 42
rotate row y=2 by 5
rotate row y=1 by 20
rotate row y=0 by 45
rotate column x=48 by 5
rotate column x=47 by 5
rotate column x=46 by 5
rotate column x=43 by 5
rotate column x=41 by 5
rotate column x=38 by 5
rotate column x=37 by 5
rotate column x=36 by 5
rotate column x=33 by 1
rotate column x=32 by 5
rotate column x=31 by 5
rotate column x=30 by 1
rotate column x=28 by 5
rotate column x=27 by 5
rotate column x=26 by 5
rotate column x=23 by 1
rotate column x=22 by 5
rotate column x=21 by 5
rotate column x=20 by 1
rotate column x=17 by 5
rotate column x=16 by 5
rotate column x=13 by 1
rotate column x=12 by 3
rotate column x=7 by 5
rotate column x=6 by 5
rotate column x=3 by 1
rotate column x=2 by 3"""

screen = [
    [False] * 50,
    [False] * 50,
    [False] * 50,
    [False] * 50,
    [False] * 50,
    [False] * 50
]

# INPUT = """rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4
# rotate column x=1 by 1
# rotate row y=0 by 1"""

# screen = [
#     [False] * 7,
#     [False] * 7,
#     [False] * 7,
# ]

def create_rect(params):
    split_params = params.split('x')
    x_size = int(split_params[0])
    y_size = int(split_params[1])
    for y_pos in range(0, y_size):
        for x_pos in range(0, x_size):
            screen[y_pos][x_pos] = True

def rotate_col(col, increment):
    while increment > 0:
        was_last_on = False
        for y_pos in range(0, len(screen)):
            if y_pos + 1 == len(screen):
                screen[0][col] = screen[y_pos][col]
            if was_last_on:
                was_last_on = screen[y_pos][col]
                screen[y_pos][col] = True
            else:
                was_last_on = screen[y_pos][col]
                screen[y_pos][col] = False
        increment -= 1

def rotate_row(row, increment):
    while increment > 0:
        was_last_on = False
        for x_pos in range(0, len(screen[0])):
            if x_pos + 1 == len(screen[0]):
                screen[row][0] = screen[row][x_pos]
            if was_last_on:
                was_last_on = screen[row][x_pos]
                screen[row][x_pos] = True
            else:
                was_last_on = screen[row][x_pos]
                screen[row][x_pos] = False
        increment -= 1

def rotate_pixels(params):
    focus = params[0]
    pos = int(params[1:][0].split('=')[1])
    inc = int(params[1:][2])
    if focus == "column":
        rotate_col(pos, inc)
    else:
        rotate_row(pos, inc)

def read_commands(commands):
    for command in commands.split('\n'):
        split_command = command.split()
        if split_command[0] == "rotate":
            rotate_pixels(split_command[1:])
        else:
            create_rect(split_command[1])

def pretty_print_screen(focus_screen):
    for row in focus_screen:
        to_print = ''
        for is_pixel_on in row:
            if is_pixel_on:
                to_print += '#'
            else:
                to_print += '.'
        print(to_print)

def get_num_on(focus_screen):
    total = 0
    for row in focus_screen:
        for is_on in row:
            if is_on:
                total += 1
    return total

read_commands(INPUT)
pretty_print_screen(screen)
print(get_num_on(screen))
