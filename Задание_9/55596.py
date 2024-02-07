def get_files():
    file = open('source/11111.txt')
    file_arr = file.readlines()
    int_file_arr = []
    for line in file_arr:
        temp = []
        for item in line.split():
            temp.append(int(item))
        int_file_arr.append(temp)
    return int_file_arr
def main():
    file = get_files()
    for line in file:


        print(line)
main()