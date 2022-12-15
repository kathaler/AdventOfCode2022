def is_max(v, l):
    for i in l:
        if i >= v:
            return False
    return True


def check_mat(m):
    s = set()
    row = 0
    for l in m:
        i = 0
        j = len(l) - 1
        while i < len(l) and j > 0:
            if is_max(l[i], l[:i]):
                s.add(str(row) + ":" + str(i))
            if is_max(l[j], l[j+1:]):
                s.add(str(row) + ":" + str(j))
            i += 1
            j -= 1
        row += 1
    return s


def flip(l):
    s = set()
    for i in l:
        p = i.split(":")
        n = p[1] + ":" + p[0]
        s.add(n)
    return s


f = open("AoC8.txt", "r")
matrix = []
for line in f.readlines():
    temp = list(line.strip("\n"))
    matrix.append(temp)

t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

s1 = check_mat(matrix)
s2 = check_mat(t_matrix)
print(sorted(s1))
print(sorted(s2))

s = check_mat(matrix).union(flip(check_mat(t_matrix)))
print(sorted(s))
print(len(s))
