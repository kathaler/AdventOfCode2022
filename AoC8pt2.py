def is_max(v, l):
    for i in l:
        if i >= v:
            return False
    return True


def get_dir(m, r, c):
    left = []
    right = []
    up = []
    down = []
    # LEFT
    row = r
    col = c - 1
    left.append(m[r][c])
    while col >= 0:
        left.append(m[row][col])
        col -= 1
    # RIGHT
    row = r
    col = c + 1
    right.append(m[r][c])
    while col < len(m):
        right.append(m[row][col])
        col += 1
    # UP
    row = r - 1
    col = c
    up.append(m[r][c])
    while row >= 0:
        up.append(m[row][col])
        row -= 1
    # DOWN
    row = r + 1
    col = c
    down.append(m[r][c])
    while row < len(m):
        down.append(m[row][col])
        row += 1

    return left, right, up, down


def calc_score(ls):
    score = 1
    for l in ls:
        if len(l) == 1:
            return 0
        else:
            t = 0
            for i in range(len(l)-1):
                t += 1
                if l[i+1] >= l[0]:
                    break
            score *= t
    return score


f = open("AoC8.txt", "r")
matrix = []
for line in f.readlines():
    temp = list(line.strip("\n"))
    matrix.append(temp)

val = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        temp = calc_score(get_dir(matrix, i, j))
        if temp > val:
            val = temp

print(val)
