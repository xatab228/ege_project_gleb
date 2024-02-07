def get_file():
    raw_file = open('source/39238.txt')
    raw_lines = raw_file.readlines()
    int_file = []
    for lines in raw_lines:
        line = lines.split()
        temp = []
        for item in line:
            temp.append(int(item))
        int_file.append(temp)
    return int_file
def main():
    file = get_file()
    cnt = 0
    for line in file:
        sline = sorted(line)
        if sline[0] ** 2 + sline[1] ** 2 == sline[2] ** 2:
           cnt += 1
    return cnt
print(main())
