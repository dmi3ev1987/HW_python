# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

rand_list = []
elem_count = int(input('Введите количество элементов: '))

# i = 0
# while i < elem_count:
#     rand_list.append(random.randint(-100, 100))
#     i += 1

for _ in range(elem_count):
    rand_list.append(random.randint(-100, 100))

print(rand_list)
