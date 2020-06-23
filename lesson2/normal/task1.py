# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

list_a = [2, -5, 8, 9, -25, 25, 4]
list_b = []

for a in list_a:
    if a >= 0:  # корень нельзя взять из отрицательного числа
        # первый способ
        sq_a = a ** 0.5
        # print(sq_a)
        # второй способ
        sq_a2 = math.sqrt(a)
        # print(sq_a2)

        if sq_a == int(sq_a):  # 2.0 = 2
            list_b.append(int(sq_a))
print(list_b)



