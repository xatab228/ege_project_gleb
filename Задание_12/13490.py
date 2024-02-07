string = '1' + '8' * 99 + '1'
while '81' in string or '882' in string or '8883' in string:
    if '81' in string:
        string = string.replace('81', '2', 1)
    elif '882' in string:
        string = string.replace('882', '3', 1)
    else:
        string = string.replace('8883', '1', 1)
print(string)