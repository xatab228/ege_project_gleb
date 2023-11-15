def main():
    alpha = ['в', 'о', 'л', 'к']
    counter = 0
    for s1 in alpha:
        for s2 in alpha:
            for s3 in alpha:
                for s4 in alpha:
                    for s5 in alpha:
                        str = s1 + s2 + s3 + s4 + s5
                        if str.count('в') == 1:
                            counter += 1
    return counter
print(main())
