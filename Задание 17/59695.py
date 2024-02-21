def reader():
    raw_file = open('source/59695.txt')
    temp = []
    for item in raw_file:
        temp.append(int(item))
    return temp
def check(arr):
    count = 0
    for item in arr:
        if 999 < item < 10000:
            count += 1
    return count == 1
def main():
    maxnum = 0
    maxsum = 0
    file = reader()
    count = 0
    for item in file:
        if item % 100 == 15 and item > maxnum:
            maxnum = item
    print(maxnum)
    for triad in range(0, len(file), 3):
        rd = 0 if (triad + 2) > (len(file) - 1) else file[triad + 2]
        nd = 0 if (triad + 1) > (len(file) - 1) else file[triad + 1]
        st = file[triad]
        arr = [st, nd, rd]
        sa = sum(arr)
        if check(arr) and sa >= maxnum:
            count += 1
            if sa > maxsum:
                maxsum = sa
    return [count, maxsum]
print(main())

