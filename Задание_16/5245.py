def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 3 * F(n - 1) - 2 * F(n - 2)
print(F(7))