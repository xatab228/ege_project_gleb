alp = [i for i in range(6)]
c = 0
for st in alp:
    for nd in alp:
        for rd in alp:
            s = str(st) + str(nd) + str(rd)
            if st >= nd and nd >= rd:
                print(s)
                c += 1
print(c)