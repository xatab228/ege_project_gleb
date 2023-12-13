def main():
    # 20 + 10 + 70
    max_numbers_count = 100
    for count_one in range(max_numbers_count):
        for count_two in range(max_numbers_count):
            for count_three in range(max_numbers_count):
                temp_str = '0' + count_one * '1' + count_two * '2' + count_three * '3'
                while ('01' in temp_str) or ('02' in temp_str) or ('03' in temp_str):
                    temp_str = temp_str.replace('01', '30', 1)
                    temp_str = temp_str.replace('02', '101', 1)
                    temp_str = temp_str.replace('03', '202', 1)
                if temp_str.count('1') == 20 and temp_str.count('2') == 10 and temp_str.count('3') == 70:
                    return count_one

print(main())
