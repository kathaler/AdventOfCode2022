class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subs = set()

    def add_sub(self, sub):
        self.subs.add(sub)

    def __repr__(self):
        return "DIR: " + self.name + " : " + str(self.parent) + " : " + str(self.subs) + "\n"


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return "FILE: " + self.name + " : " + self.size


def get_root_dir(dir):
    temp = dir
    while temp.parent is not None:
        temp = temp.parent
    return temp


def analyse_dir(dir):
    s = "DIR: " + dir.name + " | "
    if type(dir).__name__ == "File":
        return "FILE: " + dir.name + ":" + dir.size + " | "
    else:
        for sub in dir.subs:
            s += analyse_dir(sub)
    return s

sizes = []
def sum_dir(dir):
    s = 0
    if type(dir).__name__ == "File":
        return int(dir.size)
    else:
        for sub in dir.subs:
            s += sum_dir(sub)
        print("DIR: " + dir.name + " : SIZE: " + str(s))
        sizes.append(s)
    return s


f = open("AoC7.txt", "r")
i = 0
main_dir = None
current_dir = None
for line in f.readlines():
    # print(line)
    if line[0] == "$":
        # print(line)
        if "cd" in line:
            if "/" in line:
                current_dir = Directory("/", None)
                print(" "*i*2 + "- " + line[5] + " (dir)")
            elif "cd" in line:
                if ".." in line:
                    current_dir = current_dir.parent
                    i -= 1
                else:
                    new_sub = Directory(line[5], current_dir)
                    current_dir.add_sub(new_sub)
                    current_dir = new_sub
                    i += 1
                    print(" "*i*2 + "- " + line[5] + " (dir)")
    else:
        l = line.strip("\n").split(" ")
        if "dir" not in l[0]:
            print(" "*(i+1)*2 + "- " + l[1] + " (file, size=" + l[0] + ")")
            current_dir.add_sub(File(l[1], l[0]))

print(analyse_dir(get_root_dir(current_dir)))
print(str(sum_dir(get_root_dir(current_dir))))

space_to_free = 70000000 - max(sizes)
print("SPACE TO FREE: ", space_to_free)
for s in sizes:
    if s >= (30000000 - space_to_free):
        print(s)
