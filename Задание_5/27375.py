def ten_to_any_system_numeration(digit, base):
    IsFinished = False
    result = ''
    while IsFinished == False:
        cel = digit // base
        ost = digit % base
        result += str(ost)
        if cel <= 0:
            IsFinished = True
        digit = cel
    return result[::-1]
def main(n):
    three_digit = ten_to_any_system_numeration(n, 3)
    ost = n % 3

    return int(three_digit + str(ost), 3)
counter = 1
while counter < 1000:
    if 0 < (main(counter) // 100) < 10:
        break
    counter += 1
print(main(counter))










