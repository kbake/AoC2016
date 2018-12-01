# Advent of Code, D13_2016

INPUT = 1352
INPUT = 10

magic_number_maker = lambda x, y: (x*x + 3*x + 2*x*y + y + y*y) + 1352
is_open = lambda x: str(bin(x))[2:].count('1') % 2 == 0

# magic_num = magic_number_maker(1, 1) 
# print(magic_num)
# print(is_even(magic_num))

SIZE = (7,4)

def build_grid(size, input_val):
    office_space = [[None] * (size[0] + 5)] * (size[1] + 5)
    for y in range(0, size[1]+5):
        for x in range(0, size[0]+5):
            magic_num = magic_number_maker(x, y)
            # print(magic_num)
            # print(bin(magic_num))
            # print(len([i for i in str(bin(magic_num))[2:] if i == '1'])%2 == 0)
            if is_open(magic_num):
                office_space[y][x] = "."
            else:
                office_space[y][x] = "#"
    for y in range(0, size[1]+5):
        line = ''
        for x in range(0, size[0]+5):
            line += office_space[y][x]
        print(line)

build_grid(SIZE, INPUT)