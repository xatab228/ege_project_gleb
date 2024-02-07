print('y, w, z, x, f1, f2')
for w in range(2):
    for y in range(2):
        for x in range(2):
            for z in range(2):
                f1 = not(w or not(y)) or (z == x)
                f2 = (w or not(y)) == (not(x) or z)
                if f1 == 0 or f2 == 0:
                    print(y, w, z, x, f1, f2)
