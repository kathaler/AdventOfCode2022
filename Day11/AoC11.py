class Monkey:
    def __init__(self, num, items, operation, test, t, f):
        self.num = num
        self.items = []
        for i in items:
            self.items.append(int(i))
        self.op = [operation[0], operation[2], operation[1]]
        self.test = int(test)
        self.t = int(t)
        self.f = int(f)
        self.count = 0

    def pop_item(self):
        return self.items.pop(0)

    def push_item(self, val):
        self.items.append(val)

    def operate(self, item, mod):
        n = []
        for i in self.op[:2]:
            if i == 'old':
                n.append(int(item) % mod)
            else:
                n.append(int(i))
        o = self.op[2]
        if o == "+":
            return n[0] + n[1]
        if o == "*":
            return n[0] * n[1]


    def test_val(self, val):
        self.count += 1
        if val % self.test == 0:
            return self.t
        else:
            return self.f

    def __repr__(self):
        return str(self.num) + "\n" + str(self.items) + "\n" + str(self.op) + "\n" + \
            str(self.test) + "\n" + str(self.t) + "\n" + str(self.f) + "\n\n"


file = open("AoC11.txt", "r")
i = 0
monkeys = []
num, items, operation, test, t, f = 0,0,0,0,0,0
mod = 1
for line in file.readlines():
    line = line.strip("\n")
    if "Monkey" in line:
        num = line[7]
    elif "Starting items: " in line:
        items = line.strip("Starting items: ").split(", ")
    elif "Operation: " in line:
        operation = line.strip("Operation: ").split(" ")[2:]
    elif "Test: " in line:
        d = line.strip("Test: ").split(" ")
        test = d[2]
        mod *= int(test)
    elif "true" in line:
        t = line.strip("If true: throw to monkey ")
    elif "false" in line:
        f = line.strip("If false: throw to monkey ")
        monkeys.append(Monkey(num, items, operation, test, t, f))

i = 0
while i < 10000:
    for m in monkeys:
        while m.items:
            curr_item = m.pop_item()
            p = int(m.operate(curr_item, mod))
            throw = m.test_val(p)
            monkeys[throw].push_item(p)
    i += 1

counts = []
for m in monkeys:
    counts.append(m.count)

counts = sorted(counts)
print(counts[-1] * counts[-2])


