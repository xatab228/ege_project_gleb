for i in range(100,1000):
    n1=str(i)[0]
    n2=str(i)[1]
    n3=str(i)[2]
    s1=int(n1)+int(n2)
    s2=int(n2)+int(n3)
    if s1>=s2:
        r=str(s2)+str(s1)
    else:
        r=str(s1)+str(s2)
    if int(r)==1216:
        print(i,r)



