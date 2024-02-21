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
    file = reader()
    maxNum = 0
    maxSum = 0
    count = 0
    for item in file:
        if item % 100 == 15 and item > maxNum:
            maxNum = item
    for triad in range(len(file) - 2):
        arr = [file[triad], file[triad + 1], file[triad + 2]]
        arrSum = sum(arr)
        if check(arr) and arrSum >= maxNum:
            count += 1
            if arrSum > maxSum:
                maxSum = arrSum
    return [count, maxSum]
print(main())

