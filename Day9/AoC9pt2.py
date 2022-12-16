def point(x, y):
    return str(x) + ":" + str(y)


def calc_tail_move(r1, c1, r2, c2):
    if r1 - r2 == 2 and c1 == c2:
        r2 += 1
    elif r2 - r1 == 2 and c1 == c2:
        r2 -= 1
    elif c1 - c2 == 2 and r1 == r2:
        c2 += 1
    elif c2 - c1 == 2 and r1 == r2:
        c2 -= 1
    elif abs(r1 - r2) == 2 and c1 - c2 == 1:
        print("here1")
        c2 = c1
        if r1 - r2 == 2:
            r2 += 1
        elif r2 - r1 == 2:
            r2 -= 1
    elif abs(r1 - r2) == 2 and c2 - c1 == 1:
        c2 = c1
        if r1 - r2 == 2:
            r2 += 1
        elif r2 - r1 == 2:
            r2 -= 1
    elif r1 - r2 == 1 and abs(c1-c2) == 2:
        r2 = r1
        if c1 - c2 == 2:
            c2 += 1
        elif c2 - c1 == 2:
            c2 -= 1
    elif r2 - r1 == 1 and abs(c1-c2) == 2:
        r2 = r1
        if c1 - c2 == 2:
            c2 += 1
        elif c2 - c1 == 2:
            r2 = r1
            c2 -= 1

    return r2, c2


s = []
for i in range(10):
    s.append(set())
    
f = open("Day9/AoC9.txt")
for line in f.readlines():
    print(line)
    