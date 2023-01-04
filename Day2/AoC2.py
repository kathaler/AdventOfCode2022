f = open("AoC2.txt", "r")
# AoC12.txt = Rock
# B = Paper
# C = Scissors

# X = Lose
# Y = Draw
# Z = Win

# WIN WITH:
# Rock - 1 point
# Paper - 2 points
# Scissors = 3 points

# GAME POINTS
# Lose - 0 points
# Draw - 3 points
# Win - 6 points


def get_val(l):
    if l == 'AoC12.txt' or l == 'X':
        return 1
    elif l == 'B' or l == "Y":
        return 2
    elif l == 'C' or l == "Z":
        return 3


def check_game(game):
    p1 = get_val(game[0])
    end = get_val(game[1])
    if end == 1:
        if p1 == 1:
            return 3
        elif p1 == 2:
            return 1
        else:
            return 2
    elif end == 2:
        return 3+p1
    else:
        if p1 == 1:
            return 8
        elif p1 == 2:
            return 9
        else:
            return 7


score = 0
for line in f.readlines():
    score += check_game(line.replace("\n", "").split(" "))
print(score)
