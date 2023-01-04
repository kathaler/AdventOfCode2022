import string
import queue

class Node:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y
        self.dist = 10000000

def get_child_nodes(m, n):
    child_nodes = []
    if n.x - 1 >= 0:
        child_nodes.append(m[n.x - 1][n.y])
    if n.x + 1 < len(m):
        child_nodes.append(m[n.x + 1][n.y])
    if n.y - 1 >= 0:
        child_nodes.append(m[n.x][n.y - 1])
    if n.y + 1 < len(m):
        child_nodes.append(m[n.x][n.y + 1])
    return child_nodes

def convert_to_value(l, x, y):
    if l == "S":
        return Node("S", x, y)
    if l == "E":
        return Node("E", x, y)
    else:
        letters = list(string.ascii_letters)
        return Node(letters.index(l), x, y)


def bfs(m, s, e):
    src = m[s[0]][s[1]]
    end = m[e[0]][e[1]]
    visited = [[False for _ in range(len(m))] for _ in range(len(m[0]))]
    visited[src.x][src.y] = True
    q = [src]
    while q:
        curr = q.pop(0)
        if curr == end:
            return curr.dist
        cn = get_child_nodes(m, curr)
        # TODO




f = open("AoC12.txt", "r")
matrix = []
s = []
e = []
i = 0
for line in f.readlines():
    row = list(line.strip("\n"))
    l = []
    j = 0
    for n in row:
        if n == "S":
            s = [i,j]
        if n == "E":
            e = [i,j]
        l.append(convert_to_value(n, i, j))
        j += 1
    matrix.append(l)
    i += 1

print(matrix)
print(s)
print(e)

bfs(matrix, s, e)