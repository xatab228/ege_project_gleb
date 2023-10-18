print('y','z','w','x','F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(not((x and not(y)) == (z or not(w))) or (x and z)):
                    print(y,z,w,x,0)