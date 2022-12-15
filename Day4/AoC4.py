f = open("AoC4.txt", "r")
val = 0
for line in f.readlines():
    l = line.strip("\n").split(",")
    r = []
    for nums in l:
        t = nums.split("-")
        num1 = int(t[0])
        num2 = int(t[1])
        r.append(list(range(num1, num2+1)))
    print(r)
    if not (r[0][-1] < r[1][0] or r[0][0] > r[1][-1]):
        print("TRUE")
        val += 1

print(val)



