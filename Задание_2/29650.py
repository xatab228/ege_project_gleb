print('w','y','z','x','F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w or not x) and (w == (not y)) and (not w or z):
                    print(w,y,z,x,1)

# Answer: wyzx
