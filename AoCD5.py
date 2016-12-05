# Advent of Code, D5_2016
import hashlib

def figure_password(start_input):
    hash_iter = 0
    count = 0
    password = ''
    while count < 8:
        combined = start_input + str(hash_iter)
        hashed = hashlib.md5(combined.encode("utf-8")).hexdigest()
        if hashed[:5] == "00000":
            password += hashed[5]
            count += 1
        hash_iter += 1
    return password

def figure_second_password(start_input):
    hash_iter = 0
    count = 0
    password = [''] * 8
    while count < 8:
        combined = start_input + str(hash_iter)
        hashed = hashlib.md5(combined.encode("utf-8")).hexdigest()
        if hashed[:5] == "00000":
            pos = hashed[5]
            if pos.isdigit() and int(pos) < len(password):
                val = hashed[6]
                if password[int(pos)] == '':
                    password[int(pos)] = val
                    count += 1
        hash_iter += 1
    return ''.join(password)

INPUT = "ugkcyxxp"
print(figure_password(INPUT))
print(figure_second_password(INPUT))
