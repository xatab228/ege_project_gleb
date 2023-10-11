print('z','y','w','x','F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x or not(z)) and (x == (not(w))) and (not(x) or y):
                    print(z,y,w,x,1)