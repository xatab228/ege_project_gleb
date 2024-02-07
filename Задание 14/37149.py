f = 4 * 625 ** 9 - 25 ** 15 + 2 * 5 ** 11 - 7
v = ''
while f != 0:
    v += str(f % 5)
    f //= 5
v = v[::-1]
print(v.count('4'))
