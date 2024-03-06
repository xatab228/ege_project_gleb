alf = '012345678'
a = []
for x in alf:
    for y in alf:
        st = int(f'2{y}66{x}', 9)
        nd = int(f"{x}0{y}1", 12)
        if (st + nd) % 170 == 0:
            a.append((st + nd))
print(min(a) // 170)