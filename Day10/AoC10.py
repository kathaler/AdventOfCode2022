f = open("Aoc10.txt", "r")

commands = f.read().split("\n")
comms = []
for c in commands:
    comms.append(c.split(" "))

cycle_counts = [20,60,100,140,180,220]
register = []
cycle = 0

commands = []
for item in comms:
    commands += item

print(commands)
register.append(1)
i = 1
while i < len(commands):
    if commands[i-1] == "addx":
        register.append(register[i-1] + int(commands[i]))
    else:
        register.append(register[i-1])
    i += 1

val = 0
for i in cycle_counts:
    val += int(register[i-2]) * i
    print(int(register[i-2]) * i)

print(val)

