print('y','z','w','x','F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(x) or y) == (not(w) or x)) and (not(z) or w):
                    print(y,z,w,x,1)