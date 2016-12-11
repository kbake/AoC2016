# Advent of Code, D11_2016

INPUT = """The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
The third floor contains a thulium-compatible microchip.
The fourth floor contains nothing relevant."""

INPUT = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip, h generator.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""

def initalize_layout(input_text):
    floors = []
    for floor in input_text.split('\n'):
        split_floor = floor.split()
        split_floor = [s.strip('.,') for s in split_floor]
        relevant_items = []
        ind = 0
        for word in split_floor:
            word = word.strip('.')
            if word == "microchip" or word == "generator":
                ind = split_floor.index(word, ind)
                relevant_items.append(split_floor[ind-1][0] + split_floor[ind][0])
                ind += 1
        floors.append(relevant_items)
    return floors

LAYOUT = initalize_layout(INPUT)

def can_go_to_floor(items, floor):
    to_return = []
    microchips = [m for m in items if m[1] == "m"]
    generators = [g for g in items if g[1] == "g"]
    for chip in microchips:
        found_pair = False
        for generator in generators:
            if chip[0] == generator[0]:
                to_return.append((chip, generator))
                found_pair = True
        if not found_pair:
            if len(floor) == 0:
                to_return.append((chip, None))
            else:
                for floor_item in floor:
                    if floor_item[0] == chip[0]:
                        to_return.append((chip, None))
    return to_return

def figure_least_steps(layout):
    cur_floor = 0
    steps = 0
    while len(layout[0]) + len(layout[1]) + len(layout[2]) > 0:
        to_move_up = []
        to_move_down = []
        print("floor: " + str(cur_floor))
        if cur_floor < 3:
            to_move_up = can_go_to_floor(layout[cur_floor], layout[cur_floor+1])
        else:
            to_move_down = can_go_to_floor(layout[cur_floor], layout[cur_floor-1])
        if len(to_move_up) > 0:
            to_move = max(to_move_up)
            print("move up: " + str(to_move))
            layout[cur_floor+1].append(to_move[0])
            layout[cur_floor].remove(to_move[0])
            if to_move[1] is not None:
                layout[cur_floor+1].append(to_move[1])
                layout[cur_floor].remove(to_move[1])
            cur_floor += 1
        else:
            to_move = min(to_move_down)
            print("move down: " + str(to_move))
            layout[cur_floor-1].append(to_move[0])
            layout[cur_floor].remove(to_move[0])
            if to_move[1] is not None:
                layout[cur_floor-1].append(to_move[1])
                layout[cur_floor].remove(to_move[1])
            cur_floor -= 1
            # print(to_move_down)
        steps += 1
        temp = 0
        for l in layout:
            print(str(temp) + ": " + str(l))
            temp += 1
        if steps > 4:
            break
    return steps

print(figure_least_steps(LAYOUT))