def f(n):
    print(f"Step: {n}")
    if n == 1:
        print(f"Value: 2")
        print("-----------------------------")
        return 2
    elif n == 2:
        print(f"Value: 1")
        print("-----------------------------")
        return 1
    elif n > 2:
        print(f"Value: f({n} - 2) + f({n} - 1)")
        print("-----------------------------")
        return f(n - 2) + f(n - 1)


print(f(8))
