# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['apple', 'banana', 'watermelon', 'kiwi']
# без key=len - будет переводить в ASCII (где "aaa" <  "z")  # использует встроенную функциию len
right_offset = len(max(fruits, key=len))  # возвращает длину максимальноц строки

for index, item in enumerate(fruits, start=1):  # enumerate выдает два объекта index и item
    print('{}. {}'.format(index, item.rjust(right_offset)))




