print('w','z','y','x','F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((z==w) or (w and not(x)) or (x and not(y))):
                    print(w,z,y,x,0)