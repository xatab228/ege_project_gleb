from sys import *
setrecursionlimit(3000)
def f(n):
    if n == 1: return 1
    elif n == 2: return 3
    else: return f(n - 1) * f(n - 2) + (n - 2)
print(f(5))
