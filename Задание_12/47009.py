minn = 1
maxx = 50
for one_count in range(minn, maxx):
    for two_count in range(minn, maxx):
        for three_count in range(minn, maxx):
            temp = '0' + '1' * one_count + '2' * two_count + '3' * three_count + '0'
            d = len(temp)
            while temp.find('00') == -1:
                temp = temp.replace('01', '210', 1)
                temp = temp.replace('02', '3101', 1)
                temp = temp.replace('03', '2012', 1)
            if temp.count('1') == 61 and temp.count('2') == 50 and temp.count('3') == 18:
                print(d)