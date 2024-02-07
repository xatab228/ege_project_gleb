alf = "abcdef"
c=0
for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    if a1 != 'f' and a5 != 'a':
                        c += 1
print(c)