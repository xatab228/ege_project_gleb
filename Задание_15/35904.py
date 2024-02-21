def is_del(n, m):
    return n % m == 0

for a in range(1, 1000):
    if all( is_del(a, 40) and not(is_del(780, x)) or ( is_del(a, x) or not(is_del(180, x))) for x in range(1, 1000)):
        print(a)

