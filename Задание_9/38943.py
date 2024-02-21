
def reader():
    raw_file = open('source/09-5.txt')
    line = []
    for raw_line in raw_file:
        temp = []
        for item in raw_line.split():
            temp.append(int(item))
        line.append(temp)
    return line
f = reader()
c = 0
for line in f:
    line = sorted(line)
    if line[2] > line[1] + line[0]:
        print(line)
        c+=1
print(c)
