# Advent of Code, D1_2016
def update_face(direction, face):
    if direction == "R":
        if   face == "N": return "E";
        elif face == "E": return "S";
        elif face == "S": return "W";
        else:             return "N";
    if direction == "L":
        if   face == "N": return "W";
        elif face == "E": return "N";
        elif face == "S": return "E";
        else:             return "S";

def get_distance(lnode, rnode):
    return abs(lnode[0] - rnode[0]) + abs(lnode[1] - rnode[1]);

def walk(start_node, input_list):
    cur_node = start_node
    cur_face = "N"
    node_list = [start_node]
    for loc in input_list:
        direction = loc[0]
        distance = int(loc[1:])
        cur_face = update_face(direction, cur_face)
        for i in range(distance):
            if   cur_face == "N": cur_node = (cur_node[0],   cur_node[1]+1)
            elif cur_face == "E": cur_node = (cur_node[0]+1, cur_node[1])
            elif cur_face == "S": cur_node = (cur_node[0],   cur_node[1]-1)
            else:                 cur_node = (cur_node[0]-1, cur_node[1])
            if( cur_node in node_list):
                return cur_node;
            node_list.append(cur_node)
    return cur_node

input_string = "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3"
input_list   = input_string.replace(' ', '').split(',')
start_node = (0,0)
end_node = walk(start_node, input_list)
print(get_distance(start_node, end_node))
