import string

letters = list(string.ascii_letters)
letters.append(list(string.ascii_letters.upper()))
f = open("AoC3.txt", "r")
val = 0
lines3 = []
t = 0
for line in f.readlines():
    lines3.append(line.strip("\n"))
    if t < 2:
        t += 1
    else:
        print(lines3)
        for item in lines3[0]:
            if item in lines3[1] and item in lines3[2]:
                val += (letters.index(item)+1)
                print("ITEM:" + item + " | VALUE: " + str(val))
                break
        lines3 = []
        t = 0


print(val)


