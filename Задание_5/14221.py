def main(n):
    n = str(n)
    f = int(n[0]) + int(n[1])
    s = int(n[1]) + int(n[2])
    a = [f , s]
    a.sort()
    return str(a[0]) + str(a[1])
for i in range(101,1000):
        print(i, main(i))


