print('w','z','x','y','F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((not (x == (not y)) or (y and not z)) or (z and not w)):
                    print(w,z,x,y,0)


# Answer: wzxy
