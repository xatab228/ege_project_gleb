# Заданные отрезки P и Q
P = [1, 39]
Q = [23, 58]

# Нахождение общего интервала между отрезками P и Q
common_interval_start = max(P[0], Q[0])
common_interval_end = min(P[1], Q[1])

# Вычисление длины общего интервала
common_interval_length = common_interval_end - common_interval_start

# Поиск интервала A за пределами общего интервала между P и Q
A_start = common_interval_end
A_end = common_interval_start - 1

# Вычисление длины интервала A
A_length = A_end - A_start + 1

print("Максимальная длина интервала A:", A_length)