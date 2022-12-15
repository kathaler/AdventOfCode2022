f = open("AoC6.txt", "r")
signal = f.read()
print(signal)

temp = set()
i = 0
while i < len(signal):
    for item in signal[i:i+14]:
        temp.add(item)
    if len(temp) == 14:
        break
    temp = set()
    i += 1

print(i+14)
