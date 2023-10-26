def re(n):
    strn=str(n)
    n1=strn[:1]
    n2 = strn[1:2]
    n3 = strn[2:3]
    n4 = strn[3:4]
    s12=int(n1)+int(n2)
    s23 = int(n2) + int(n3)
    s34 = int(n3) + int(n4)
    a=[s12,s23,s34]
    a.remove(min(a))
    return(str(min(a))+str(max(a)))
b=[]
for i in range(1000, 10000):
    if re(i) == '613':
        b.append(i)
print(min(b))




