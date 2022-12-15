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
        print("here2")
        c2 = c1
        if r1 - r2 == 2:
            r2 += 1
        elif r2 - r1 == 2:
            r2 -= 1
    elif r1 - r2 == 1 and abs(c1-c2) == 2:
        print("here3")
        r2 = r1
        if c1 - c2 == 2:
            c2 += 1
        elif c2 - c1 == 2:
            c2 -= 1
    elif r2 - r1 == 1 and abs(c1-c2) == 2:
        print("here4")
        r2 = r1
        if c1 - c2 == 2:
            c2 += 1
        elif c2 - c1 == 2:
            r2 = r1
            c2 -= 1

    return r2, c2


h = set()
t = set()
f = open("AoC9.txt", "r")
hx = 0
hy = 0
tx = 0
ty = 0
h.add(point(hx, hy))
for line in f.readlines():
    print(line)
    step = int(line[1:])
    for k in range(step):
        if line[0] == "R":
            hy += 1
        elif line[0] == "L":
            hy -= 1
        elif line[0] == "U":
            hx += 1
        elif line[0] == "D":
            hx -= 1
        h.add(point(hx, hy))
        t_pos = calc_tail_move(hx, hy, tx, ty)
        tx = t_pos[0]
        ty = t_pos[1]
        t.add(point(tx, ty))
        print("HEAD POINT:", point(hx, hy))
        print("TAIL POINT:", point(tx, ty))

print(sorted(h))
print(sorted(t))
print(len(t))