def main():
    counter = 0
    for s1 in range(9):
        for s2 in range(9):
            for s3 in range(9):
                for s4 in range(9):
                    for s5 in range(9):
                        if s1 > s2 and s2 > s3 and s3 > s4 and s4 > s5:
                            counter +=1
    return counter
print(main())