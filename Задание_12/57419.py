def f(s):
    while ('25' in s) or ('355' in s) or ('555' in s):
        if '25' in s:
            s = s.replace('25', '5', 1)
        elif '355' in s:
            s = s.replace('355', '52', 1)
        elif '555' in s:
            s = s.replace('555', '3', 1)

    return s
for i in range(3, 100):
    s = f('2' + '5' * i)
    print(s)
    sum = 0
    for k in range(len(s)):
        sum += int(s[k])
    if sum == 17:
        print(i)