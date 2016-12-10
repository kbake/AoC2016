# Advent of Code, D10_2016

INPUT = """bot 123 gives low to bot 191 and high to bot 162
bot 191 gives low to output 9 and high to bot 192
bot 182 gives low to bot 175 and high to bot 196
bot 113 gives low to bot 172 and high to bot 94
bot 78 gives low to bot 37 and high to bot 25
bot 187 gives low to bot 125 and high to bot 45
bot 71 gives low to bot 108 and high to bot 61
bot 154 gives low to bot 2 and high to bot 64
bot 142 gives low to bot 110 and high to bot 163
bot 109 gives low to output 0 and high to bot 43
bot 198 gives low to bot 101 and high to bot 52
bot 138 gives low to bot 9 and high to bot 47
value 5 goes to bot 189
bot 179 gives low to bot 176 and high to bot 14
bot 115 gives low to bot 82 and high to bot 181
bot 101 gives low to bot 90 and high to bot 5
bot 9 gives low to output 5 and high to bot 149
bot 181 gives low to bot 0 and high to bot 27
bot 119 gives low to bot 207 and high to bot 65
bot 202 gives low to bot 69 and high to bot 154
bot 100 gives low to bot 206 and high to bot 169
bot 72 gives low to bot 205 and high to bot 12
bot 146 gives low to bot 8 and high to bot 106
bot 58 gives low to bot 180 and high to bot 123
value 37 goes to bot 1
value 61 goes to bot 144
bot 205 gives low to bot 169 and high to bot 3
bot 91 gives low to bot 76 and high to bot 84
bot 93 gives low to bot 122 and high to bot 100
bot 76 gives low to bot 147 and high to bot 89
bot 102 gives low to bot 11 and high to bot 23
bot 43 gives low to output 11 and high to output 12
bot 128 gives low to bot 15 and high to bot 85
bot 137 gives low to bot 112 and high to bot 2
bot 88 gives low to bot 103 and high to bot 55
bot 162 gives low to bot 192 and high to bot 141
bot 183 gives low to bot 49 and high to bot 81
bot 127 gives low to bot 113 and high to bot 207
value 11 goes to bot 165
bot 28 gives low to bot 62 and high to bot 42
bot 95 gives low to bot 42 and high to bot 32
bot 50 gives low to bot 160 and high to bot 194
bot 68 gives low to bot 133 and high to bot 142
bot 20 gives low to bot 208 and high to bot 203
bot 178 gives low to bot 182 and high to bot 54
bot 120 gives low to bot 102 and high to bot 99
bot 131 gives low to bot 67 and high to bot 83
bot 21 gives low to bot 111 and high to bot 69
bot 27 gives low to bot 46 and high to bot 193
bot 98 gives low to bot 63 and high to bot 22
value 13 goes to bot 7
bot 121 gives low to bot 155 and high to bot 146
bot 41 gives low to bot 153 and high to bot 53
bot 75 gives low to bot 100 and high to bot 205
value 43 goes to bot 4
bot 206 gives low to bot 151 and high to bot 77
bot 0 gives low to bot 95 and high to bot 46
bot 208 gives low to output 14 and high to bot 126
bot 40 gives low to bot 187 and high to bot 184
bot 184 gives low to bot 45 and high to bot 124
bot 60 gives low to bot 188 and high to bot 202
value 67 goes to bot 198
bot 145 gives low to bot 22 and high to bot 108
bot 197 gives low to bot 195 and high to bot 190
bot 203 gives low to bot 126 and high to bot 51
bot 87 gives low to bot 51 and high to bot 179
bot 64 gives low to bot 128 and high to bot 85
bot 1 gives low to bot 198 and high to bot 173
bot 29 gives low to bot 71 and high to bot 168
bot 47 gives low to bot 149 and high to bot 113
bot 165 gives low to bot 80 and high to bot 135
bot 112 gives low to bot 162 and high to bot 174
bot 149 gives low to output 1 and high to bot 172
value 41 goes to bot 80
bot 5 gives low to bot 136 and high to bot 62
bot 143 gives low to bot 97 and high to bot 41
bot 86 gives low to bot 145 and high to bot 71
value 59 goes to bot 147
bot 57 gives low to bot 30 and high to bot 188
bot 36 gives low to bot 150 and high to bot 30
bot 135 gives low to bot 44 and high to bot 117
bot 134 gives low to bot 16 and high to bot 35
bot 167 gives low to bot 28 and high to bot 95
bot 22 gives low to bot 127 and high to bot 119
bot 26 gives low to bot 81 and high to bot 16
bot 33 gives low to bot 6 and high to bot 78
bot 171 gives low to bot 186 and high to bot 17
bot 16 gives low to bot 96 and high to bot 33
bot 118 gives low to bot 117 and high to bot 56
bot 199 gives low to bot 98 and high to bot 145
bot 188 gives low to bot 21 and high to bot 202
value 29 goes to bot 164
bot 169 gives low to bot 77 and high to bot 140
bot 96 gives low to bot 181 and high to bot 6
value 71 goes to bot 201
bot 194 gives low to bot 87 and high to bot 150
bot 160 gives low to bot 203 and high to bot 87
bot 15 gives low to bot 158 and high to bot 105
bot 42 gives low to bot 166 and high to bot 39
bot 133 gives low to bot 54 and high to bot 110
value 47 goes to bot 13
bot 31 gives low to output 8 and high to bot 9
bot 159 gives low to bot 74 and high to bot 155
bot 157 gives low to bot 12 and high to bot 187
bot 176 gives low to bot 139 and high to bot 58
bot 35 gives low to bot 33 and high to bot 78
bot 90 gives low to bot 148 and high to bot 136
bot 122 gives low to bot 70 and high to bot 206
bot 114 gives low to bot 72 and high to bot 157
bot 55 gives low to bot 40 and high to bot 184
bot 37 gives low to bot 193 and high to bot 25
value 31 goes to bot 13
bot 107 gives low to bot 99 and high to bot 93
bot 14 gives low to bot 58 and high to bot 38
bot 77 gives low to bot 86 and high to bot 29
bot 116 gives low to bot 79 and high to bot 170
bot 23 gives low to bot 132 and high to bot 70
bot 148 gives low to bot 144 and high to bot 120
bot 195 gives low to bot 170 and high to bot 185
bot 185 gives low to bot 138 and high to bot 63
bot 62 gives low to bot 107 and high to bot 166
bot 174 gives low to bot 141 and high to bot 128
bot 7 gives low to bot 91 and high to bot 11
bot 3 gives low to bot 140 and high to bot 34
bot 12 gives low to bot 3 and high to bot 125
value 7 goes to bot 148
bot 70 gives low to bot 161 and high to bot 151
bot 89 gives low to bot 116 and high to bot 195
bot 108 gives low to bot 119 and high to bot 204
bot 201 gives low to bot 1 and high to bot 104
bot 18 gives low to output 15 and high to bot 208
bot 66 gives low to bot 177 and high to bot 130
bot 189 gives low to bot 165 and high to bot 177
bot 48 gives low to output 13 and high to bot 18
bot 186 gives low to bot 189 and high to bot 66
bot 82 gives low to bot 167 and high to bot 0
bot 92 gives low to bot 201 and high to bot 49
bot 144 gives low to bot 7 and high to bot 102
bot 97 gives low to bot 146 and high to bot 153
bot 104 gives low to bot 173 and high to bot 82
bot 74 gives low to bot 83 and high to bot 50
bot 49 gives low to bot 104 and high to bot 115
bot 172 gives low to output 20 and high to bot 48
bot 163 gives low to bot 41 and high to bot 53
bot 117 gives low to bot 26 and high to bot 134
bot 168 gives low to bot 61 and high to bot 182
bot 65 gives low to bot 131 and high to bot 74
bot 180 gives low to output 6 and high to bot 191
bot 126 gives low to output 19 and high to bot 19
value 19 goes to bot 186
bot 166 gives low to bot 93 and high to bot 75
bot 193 gives low to bot 59 and high to bot 88
bot 81 gives low to bot 115 and high to bot 96
bot 207 gives low to bot 94 and high to bot 131
bot 130 gives low to bot 118 and high to bot 56
bot 153 gives low to bot 106 and high to bot 152
value 17 goes to bot 92
bot 110 gives low to bot 143 and high to bot 163
bot 192 gives low to output 7 and high to bot 129
bot 156 gives low to bot 10 and high to bot 68
bot 83 gives low to bot 20 and high to bot 160
bot 2 gives low to bot 174 and high to bot 64
value 23 goes to bot 91
bot 10 gives low to bot 178 and high to bot 133
bot 103 gives low to bot 157 and high to bot 40
bot 61 gives low to bot 204 and high to bot 175
bot 63 gives low to bot 47 and high to bot 127
bot 105 gives low to bot 200 and high to bot 24
bot 79 gives low to output 10 and high to bot 31
bot 73 gives low to bot 168 and high to bot 178
bot 19 gives low to output 2 and high to bot 139
bot 125 gives low to bot 34 and high to bot 156
bot 56 gives low to bot 134 and high to bot 35
bot 44 gives low to bot 183 and high to bot 26
bot 4 gives low to output 3 and high to bot 79
bot 155 gives low to bot 50 and high to bot 8
value 73 goes to bot 101
bot 38 gives low to bot 123 and high to bot 112
bot 151 gives low to bot 199 and high to bot 86
bot 17 gives low to bot 66 and high to bot 130
bot 13 gives low to bot 171 and high to bot 17
bot 190 gives low to bot 185 and high to bot 98
bot 161 gives low to bot 190 and high to bot 199
bot 139 gives low to output 16 and high to bot 180
bot 99 gives low to bot 23 and high to bot 122
bot 53 gives low to bot 152 and high to bot 60
bot 94 gives low to bot 48 and high to bot 67
bot 132 gives low to bot 197 and high to bot 161
bot 150 gives low to bot 179 and high to bot 209
bot 173 gives low to bot 52 and high to bot 167
bot 45 gives low to bot 156 and high to bot 124
bot 30 gives low to bot 209 and high to bot 21
bot 67 gives low to bot 18 and high to bot 20
bot 84 gives low to bot 89 and high to bot 197
bot 8 gives low to bot 194 and high to bot 36
bot 59 gives low to bot 114 and high to bot 103
bot 209 gives low to bot 14 and high to bot 111
value 53 goes to bot 76
bot 69 gives low to bot 137 and high to bot 154
bot 46 gives low to bot 32 and high to bot 59
bot 111 gives low to bot 38 and high to bot 137
bot 196 gives low to bot 121 and high to bot 97
bot 52 gives low to bot 5 and high to bot 28
bot 11 gives low to bot 84 and high to bot 132
bot 204 gives low to bot 65 and high to bot 159
bot 164 gives low to bot 92 and high to bot 183
bot 24 gives low to bot 109 and high to bot 43
value 2 goes to bot 171
bot 51 gives low to bot 19 and high to bot 176
bot 136 gives low to bot 120 and high to bot 107
bot 147 gives low to bot 4 and high to bot 116
bot 25 gives low to bot 88 and high to bot 55
bot 129 gives low to output 18 and high to bot 158
bot 152 gives low to bot 57 and high to bot 60
bot 39 gives low to bot 75 and high to bot 72
bot 124 gives low to bot 68 and high to bot 142
bot 141 gives low to bot 129 and high to bot 15
bot 85 gives low to bot 105 and high to bot 24
value 3 goes to bot 90
bot 80 gives low to bot 164 and high to bot 44
bot 54 gives low to bot 196 and high to bot 143
bot 34 gives low to bot 73 and high to bot 10
bot 175 gives low to bot 159 and high to bot 121
bot 32 gives low to bot 39 and high to bot 114
bot 140 gives low to bot 29 and high to bot 73
bot 200 gives low to output 17 and high to bot 109
bot 106 gives low to bot 36 and high to bot 57
bot 177 gives low to bot 135 and high to bot 118
bot 170 gives low to bot 31 and high to bot 138
bot 158 gives low to output 4 and high to bot 200
bot 6 gives low to bot 27 and high to bot 37"""

# IN'PUT = """value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
# value 3 goes to bot 1
# bot 1 gives low to output 1 and high to bot 0
# bot 0 gives low to output 2 and high to output 0
# value 2 goes to bot 2"""'

class Bot:
    def __init__(self, bot_id, is_output):
        self._id = bot_id
        self.vals = []
        self.low_bot = ""
        self.high_bot = ""
        self.is_output = is_output

    def add_value(self, val):
        self.vals.append(val)
        self.vals = sorted(self.vals)

    def set_low_command(self, command):
        self.low_bot = command

    def set_high_command(self, command):
        self.high_bot = command

    def enact_command(self, is_high_command):
        to_return = ()
        if is_high_command:
            value = self.vals[len(self.vals)-1]
            self.vals.remove(value)
            to_return = (self.high_bot, value)
        else:
            value = self.vals[0]
            self.vals.remove(value)
            to_return = (self.low_bot, value)
        return to_return

    def get_id(self):
        return self._id

    def has_comparables(self):
        return len(self.vals) > 1

def create_bots(instructions):
    bots = {}
    for instruction in instructions.split('\n'):
        split_instruction = instruction.split()
        if split_instruction[0] == "value":
            bot_id = split_instruction[4] + split_instruction[5]
            value = int(split_instruction[1])
            if bot_id in bots.keys():
                bots[bot_id].add_value(value)
            else:
                bots[bot_id] = Bot(bot_id, False)
                bots[bot_id].add_value(value)
        else:
            bot_id = split_instruction[0] + split_instruction[1]
            is_output = split_instruction[0] == "output"
            low_command = split_instruction[5] + split_instruction[6]
            high_command = split_instruction[10] + split_instruction[11]
            if low_command not in bots.keys():
                bots[low_command] = Bot(low_command, low_command[:6] == "output")
            if high_command not in bots.keys():
                bots[high_command] = Bot(high_command, high_command[:6] == "output")
            if bot_id in bots.keys():
                bots[bot_id].set_low_command(low_command)
                bots[bot_id].set_high_command(high_command)
            else:
                bots[bot_id] = Bot(bot_id, is_output)
                bots[bot_id].set_low_command(low_command)
                bots[bot_id].set_high_command(high_command)
    return bots

def focus_bot(comparables, look_for):
    to_return = None
    for bot in comparables:
        if look_for[0] in bot.vals and look_for[1] in bot.vals:
            to_return = bot
            break
    return to_return

def run_through_comparables(comparables, bots):
    for comp in comparables:
        low = comp.enact_command(False)
        high = comp.enact_command(True)
        bots[low[0]].add_value(low[1])
        bots[high[0]].add_value(high[1])
    return bots

def do_the_thing(input, look_for):
    bots = create_bots(input)
    comparables = [b[1] for b in bots.items() if b[1].has_comparables()]
    found_bot = focus_bot(comparables, look_for)
    while found_bot is None and len(comparables) > 0:
        bots = run_through_comparables(comparables, bots)
        comparables = [b[1] for b in bots.items() if b[1].has_comparables()]
        found_bot = focus_bot(comparables, look_for)
    return found_bot.get_id() if found_bot is not None else -1

# print(do_the_thing(INPUT, (2, 5)))
print(do_the_thing(INPUT, (61, 17)))

def get_output(input):
    bots = create_bots(input)
    comparables = [b[1] for b in bots.items() if b[1].has_comparables()]
    while len(comparables) > 0:
        bots = run_through_comparables(comparables, bots)
        comparables = [b[1] for b in bots.items() if b[1].has_comparables()]
    outputs = [o[1].vals[0] for o in bots.items() if o[1].is_output and o[0][6:] in ('0', '1', '2')]
    print(outputs)
    total = outputs[0]
    for output in outputs[1:]:
        total *= output
    return total

print(get_output(INPUT))
