def function(n):
    n1 = int(str(n)[:1])
    n2 = int(str(n)[1:2])
    n3 = int(str(n)[2:])
    s1 = n1 * n2
    s2 = n2 * n3
    if s1 < s2:
        s1 = str(s1) + str(s2)
    else:
        s1 = str(s2) + str(s1)
    return s1
a=[]
for i in range(100, 1000):
    if function(i) == '621':
        a.append(i)
print(min(a))