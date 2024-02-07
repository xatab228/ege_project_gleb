alf = '0123456789abcdef'
for x in alf:
    s1 = int(f'1{x}bad', 16)
    s2 = int(f'2c{x}fe', 16)
    if (s1 + s2) % 15 == 0:
         print((s1 + s2) / 15)


