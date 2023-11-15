def main():
    alphabet = "ВОЛК"
    counter = 0

    for s1 in alphabet:
        for s2 in alphabet:
            for s3 in alphabet:
                for s4 in alphabet:
                    for s5 in alphabet:
                        word = s1 + s2 + s3 + s4 + s5
                        if word.count('В') == 1:
                            counter += 1
    print(counter)

main()