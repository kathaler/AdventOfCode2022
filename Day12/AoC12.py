import string

class PQueue:
    def __init__(self):
        self.q = []
    def put(self, node):
        self.q.append(node)
        self.q.sort()

    def pop(self):
        return self.q.pop(0)

    def is_empty(self):
        return len(self.q) == 0


class Node:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y
        self.visited = False
        self.dist = 10000000
        self.prev = None

    def visit(self):
        self.visited = True

    def is_visited(self):
        return self.visited

    def set_dist(self, n):
        self.dist = n

    def set_prev(self, p):
        self.prev = p

    def __repr__(self):
        return "Node " + str(self.val) + " : "  +str(self.x) + "," \
            + str(self.y) + " is visited? " + str(self.visited) \
            + "Dist: " + str(self.dist) + " | "

    def __lt__(self, other):
        return self.dist < other.dist



def convert_to_value(l, x, y):
    if l == "S":
        return Node("S", x, y)
    if l == "E":
        return Node("E", x, y)
    else:
        letters = list(string.ascii_letters)
        return Node(letters.index(l), x, y)

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

def dijkstra(m, s):
    q = []
    root = m[s[0]][s[1]]
    root.set_dist(0)
    while q:
        print(q.q)
        u = q.pop()
        neighbors = get_child_nodes(m, u)
        for v in neighbors:
            qu = q.q
            if v in qu:
                if v.val == "E":
                    alt = u.dist
                else:
                    alt = u.dist + v.val
                if alt < v.dist:
                    v.set_dist(alt)
                    v.set_prev(u)



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


for m in matrix:
    print(m)

dijkstra(matrix, s)
print("=============================================")
for m in matrix:
    print(m)
print(e)
end = matrix[e[0]][e[1]]
print(end.dist)