
def get_from_file():
    file = open('source/48430.txt', 'r')
    temp = file.readlines()
    arr = []
    for item in temp:
        arr.append(item.split())
    return arr


def main():
    file_arr = get_from_file()
    count = 0
    for line in file_arr:
        repeat_values = []
        uniq_values = []
        for value in line:
            if line.count(value) == 1:
                uniq_values.append(int(value))
            elif line.count(value) == 2 and not (int(value) in repeat_values):
                repeat_values.append(int(value))
        if len(repeat_values) == 2 and len(uniq_values) == 2:
            summ_repeat = sum(repeat_values)
            summ_uniq = sum(uniq_values)
            if summ_repeat < summ_uniq:
                count += 1
    print(count)


main()