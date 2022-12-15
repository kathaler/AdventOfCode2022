f = open("AoC5.txt", "r")
stacks = []
procs = []
nums = []
for line in f.readlines():
    line = line.strip("\n").split(" ")
    if not("move" in line):
        if line != [""]:
            if line[1] == "1":
                i = 0
                while i < len(line):
                    if line[i] == "":
                        line.pop(i)
                    else:
                        i += 1
                nums = line
            else:
                i = 0
                length = len(line)
                while i < length-1:
                    if line[i] == "" and line[i+3] == "":
                        line.pop(i+3)
                        line.pop(i+2)
                        line.pop(i+1)
                    i += 1
                    length = len(line)
                stacks.append(line)
    else:
        line = [line[1], line[3], line[5]]
        procs.append(line)

m = []
for i in range(len(nums)):
    temp = []
    for j in range(len(stacks)):
        temp.append(stacks[j][i])
    temp.reverse()
    m.append([j for j in temp if j != ""])
print(m)
print(procs)

for i in procs:
    n = int(i[0])
    j = 0
    curr = []
    while j < n:
        curr.append(m[int(i[1])-1].pop())
        j += 1
    curr.reverse()
    m[int(i[2]) - 1] += curr

print(m)
s = ""
for i in m:
    s += i[-1].strip("[").strip("]")

print(s)