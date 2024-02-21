alp = 'abcx'
c = 0
for st in alp:
    for nd in alp:
        for rd in alp:
            for th in alp:
                for fth in alp:
                    if st != 'x' and nd != 'x' and rd != 'x' and th != 'x':
                        c+=1
print(c)