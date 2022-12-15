def find_min(l):
    min_index = -1
    min = 10000000000000000000000
    for i in range(len(l)):
        if l[i] < min:
            min_index = i
            min = l[i]
    return min_index


f = open("AoC1.txt", "r")
max = [0, 0, 0]
i = 0
for line in f.readlines():
    if line == "\n":
        for j in range(3):
            if i > max[j]:
                max[find_min(max)] = i
                break
        i = 0
    else:
        i += int(line)
    print(max)

print(max)
print(sum(max))
