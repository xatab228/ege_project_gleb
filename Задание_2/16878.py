print('z','w','y','x','F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(not(x == (not(y))) or (z == (y or w))):
                    print(z,w,y,x,0)