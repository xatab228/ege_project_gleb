print('z','y','w','x','F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and not(y)) or (not(w) or z)) == (z == x):
                    print(z,y,w,x,1)