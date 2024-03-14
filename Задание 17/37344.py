def F(a, b):
    if ((a * b) % 10) == 0: return True
    else: return False
def reader():
    rf = open('source/37344.txt')
    a = []
    for rl in rf.readlines():
        a.append(int(rl))
    return a
f = reader()
c = 0
m = 0
for biba in range(0, len(f) -1):
    for boba in range(len(f)):
        if F(f[biba], f[boba]) and biba != boba:
            c += 1
            if m < (f[biba] + f[boba]): m = (f[biba] + f[boba])
print(c, m)

