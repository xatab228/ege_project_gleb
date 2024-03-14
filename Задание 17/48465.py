def reader():
    r_file = open('source/48465.txt')
    temp = []
    for r_line in r_file.readlines():

        for item in r_line.split():
            temp.append(int(item))
    return temp
def is_six(n):
    str_n = str(n)
    if str_n[len(str_n)-1 :] == '6':
        return 1
    else: return 0

f = reader()
sumInF = []
minInF = 100000
for i in f:
    if is_six(i) == 1:
        if i < minInF:
            minInF = i

for i in range(0, len(f) - 1):
    temp = [f[i], f[i + 1]]
    if is_six(f[i]) != is_six(f[i + 1]):
        print(f[i] ** 2 + f[i + 1] ** 2, minInF ** 2 )
        if (f[i] ** 2 + f[i + 1] ** 2) < (minInF ** 2):
            sumInF.append((f[i] ** 2 + f[i + 1] ** 2))
print(len(sumInF), max(sumInF))





