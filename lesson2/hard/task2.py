# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.

# Условия корректности:

# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# # пример корректной даты
# date = '01.11.1985'
#
# # примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

########

days_count_by_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # кортеж - неизменяемый список
date = input('Введите дату: ')
day, month, year = date.split('.')

if len(day) == 2 and len(month) == 2 and len(year) == 4:
    if 0 < int(month) <= 12 \
            and 0 < int(year) <= 9999 \
            and 0 < int(day) <= days_count_by_month[int(month)]:
        print('Дата корректна')
    else:
        print('Дата некорректна')
else:
    print('Длинна одной из часткей некорректна')





