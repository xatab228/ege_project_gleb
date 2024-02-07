def main():
    arr = []
    alf = '0123456789ABC'
    for x in alf:
        for y in alf:

            s1 = int(f'8{x}78{y}', 13)
            s2 = int(f'79{x}{y}7', 18)
            res = s1 + s2
            if res % 9 == 0:
                arr.append(res)
    return min(arr) // 9
print(main())