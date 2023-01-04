import re

def parse(s):
    pause = 0
    new_s = []
    i = 0
    for j in range(len(s)):
        if s[j] == "[":
            pause += 1
        elif s[j] == "]":
            pause -= 1
            if pause == 0:
                new_s.append(s[i:j+1])
                i = j
        elif s[j] == "]":
            pause -= 1
        elif pause == 0 and s[j] == ",":
            i = j+1
        elif pause == 0:
            new_s.append(s[j])

    return new_s
def compare(sig1, sig2, pair_num):
    sig1 = parse(sig1[1:-1])
    sig2 = parse(sig2[1:-1])
    print("PAIR NUMBER: ", pair_num)
    print("SIGNAL1: ", sig1)
    print("SIGNAL2: ", sig2)

    if isinstance(sig1, int) and isinstance(sig2, int):
        if sig1 < sig2:
            return 1
        if sig1 == sig2:
            return 0
        if sig1 > sig2:
            return -1
    sig1 = [sig1] if isinstance(sig1, int) else sig1
    sig2 = [sig2] if isinstance(sig2, int) else sig2
    l1 = len(sig1)
    l2 = len(sig2)

    for i in range(min(l1, l2)):
        temp = compare(sig1[i], sig2[i], pair_num)
        if temp != 0:
            return temp;

    if l1 < l2:
        return 1
    if l1 == l2:
        return 0
    if l1 > l2:
        return -1



f = open("AoC13.txt", "r")
signals = []
signal = []
for line in f.readlines():
    if line == "\n":
        signals.append(signal)
        signal = []
    else:
        line = line.strip("\n")
        signal.append(line)

print(signals)
for i in range(len(signals)):
    print(compare(signals[i][0], signals[i][1], i), "\n")

