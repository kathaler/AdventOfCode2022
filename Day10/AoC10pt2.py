def sprite_line(j):
    s = ""
    for i in range(40):
        if i in range(j-1, j+2):
            s += "#"
        else:
            s += "."
    return s


f = open("Aoc10.txt", "r")
commands = f.read().split("\n")
comms = []
for c in commands:
    comms.append(c.split(" "))

register = []
commands = []
for item in comms:
    commands += item

register.append(1)
i = 0
while i < len(commands):
    if commands[i-1] == "addx":
        register.append(register[i] + int(commands[i]))
    else:
        register.append(register[i])
    i += 1

print(register)
sprite_pos = ""
crt_rows = []
crt_row = ""
for j in range(len(register)):
    sprite_pos = sprite_line(int(register[j]))
    print("Sprite pos: ", sprite_pos)
    if sprite_pos[j%40] == "#":
        crt_row += "#"
    else:
        crt_row += "."
    print("CRT ROW: ", crt_row)
    if j%40 == 0 and j != 0:
        crt_rows.append(crt_row)
        crt_row = ""

for row in crt_rows:
    print(row)