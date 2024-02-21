def main():
    alpha = ['н', 'а', 'с', 'т', 'я']
    counter = 0
    for s1 in alpha:
        for s2 in alpha:
            for s3 in alpha:
                for s4 in alpha:
                    for s5 in alpha:
                        for s6 in alpha:
                            str = s1 + s2 + s3 + s4 + s5 + s6
                            if str.count('а') < 2 and str.count('я') < 2:
                                counter += 1
    return counter
print(main())