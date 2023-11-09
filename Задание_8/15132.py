
def main():
    alphabet = ['А', 'П', 'Р', 'С', 'У']
    counter = 0

    for s1 in alphabet:
        for s2 in alphabet:
            for s3 in alphabet:
                for s4 in alphabet:
                    counter += 1
                    print(s1, s2, s3, s4)
                    if s1 == 'У':
                        print(counter)
                        return

main()