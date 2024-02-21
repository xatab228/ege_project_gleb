def main():
    alpha = ['а', 'о', 'у']
    counter = 0
    for s1 in alpha:
        for s2 in alpha:
            for s3 in alpha:
                for s4 in alpha:
                    for s5 in alpha:
                        counter +=1
                        if counter == 170:
                            return (s1 + s2 + s3 + s4 + s5)
print(main())