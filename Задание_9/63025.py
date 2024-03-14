def reader():
    rf = open('source/63025.txt')
    f = []
    for rl in rf.readlines():
        temp = []
        for item in rl.split():
            temp.append(int(item))
        f.append(temp)
    return f
f = reader()
a = []
c = 0
for line in f:
    rep_val = []
    rep_val_c = []
    temp = []
    for val in line:
        if line.count(val) != 1 and not (val in rep_val):
            rep_val.append(val)
            rep_val_c.append(line.count(val))
    if rep_val != []:
        temp.append(rep_val)
        temp.append(rep_val_c)
        temp.append(max(line))
        a.append(temp)
for i in range(len(a)):
    suma = 0
    for j in range(len(a[i][0])):
        suma += a[i][0][j] * a[i][1][j]
    if suma > a[i][2] and a[i][2] != max(a[i][0]):
        c += 1
print(c)




















#Я САМ НЕ ЗНАЮ ЧТО ТУТ ПРОИСХОДИТ)