def main():
    N = 9999
    while N >= 1000:
        str_N = str(N)
        sum1 = int(str_N[0]) + int(str_N[1])
        sum2 = int(str_N[1]) + int(str_N[2])
        sum3 = int(str_N[2]) + int(str_N[3])
        sorted_summ_arr = sorted([sum1, sum2, sum3], reverse=True)
        if (str(sorted_summ_arr[1]) + str(sorted_summ_arr[0])) == '1315':
            return N
        else:
            N -= 1


print(main())
