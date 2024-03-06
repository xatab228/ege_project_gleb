def reader():
    r_file = open('source/37359.txt')
    temp = []
    for r_line in r_file.readlines():

        for item in r_line.split():
            temp.append(int(item))
    return temp

print(reader())
f = reader()
temp = []
for st in range(0, len(f) - 1):
    for nd in range(st + 1, len(f)):
        if (f[st] + f[nd]) % 117 == 0:
            temp.append(f[st] + f[nd])
print(len(temp) ,max(temp))
