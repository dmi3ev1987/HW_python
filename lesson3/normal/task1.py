# Задание - 1

# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.

# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000

# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь)

# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.

# Так же при выводе имя должно быть полностью в верхнем регистре!

# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


# names = ['Андрей', 'Ольга', 'Александр', 'Василий', 'Петр']
# salary = ['1000000', '50000', '75000', '25000', '60000']

# my_dictionary = dict(zip(names, salary))
# print(my_dictionary)
# print(len(names))

# with open('result.txt', 'w', encoding='utf-8') as res:
#     i = 0
#     for name in my_dictionary:
#         sal = int(my_dictionary.get(names[i]))
#         str_res = str('{} - {}\n'.format(name.upper(), sal))
#         if i < len(names) - 1:
#             i += 1
#         if sal <= 500000:
#             res.write(str_res)


names = ['Андрей', 'Ольга', 'Александр', 'Василий', 'Петр']
salary = ['1000000', '50000', '75000', '25000', '60000']

TAX_PERCENT = 13  # Caps Lock - пишутся переменные, которые не меняются в процессе скрипта
MAX_SALARY = 500000

result = dict(zip(names, salary))

f = open('salary.txt', 'w+', encoding='utf-8')  # w+ режим записи и чтения

for key, value in result.items():
    if int(value) <= MAX_SALARY:
        f.write('{} - {}\n'.format(key, value))
f.seek(0)  # переход на нулевую позицию в открытом файле (w+)

for line in f:
    name, salary = line.split(' - ')
    tax = int(salary) / 100 * TAX_PERCENT
    after_tax = int(salary) - int(tax)
    print('{} получил зарплату в размере: {}, налог составил: {}'.format(name.upper(), after_tax, tax))
f.close()









