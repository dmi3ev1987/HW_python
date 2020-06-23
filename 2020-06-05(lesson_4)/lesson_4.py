# # глобальные и локальные переменные
#
# x = [1, 2, 3]
#
#
# def test(some_list):
#     some_list.append(100)  # когда мы передаем изменяемый объект (ссылку на объект) - по ссылке он его изменет
#
#
# test(x)
# print(x)


# a = [1, 2, 3, 4, 5, 6]
# for number in a:
#     print(number)
#     a.remove(number)
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# for number in a.copy():
#     print(number)
#     a.remove(number)
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# b = a  # в переменную "b" положи ссылку на переменную "a"
# b.append(1000)
# print(a)  # добавит к "а" 1000
#
# a = [1, 2, 3, 4, 5, 6]
# b = a.copy()  # когда .copy мы отвязанны от переменной "а"
# b.append(1000)
# print(a)  # не добавит 1000 к "а"


# a = [1, 2, 3, [100]]  # [100] - своя ссылка
# b = a.copy()
# b[3].append(200)
# print(b)
# print(a)  # меняется так же как и b т.к. [3] элемент ссылвется на ссылку внутри ссылки

# import copy
# a = [1, 2, 3, [100]]  # [100] - своя ссылка
# b = copy.deepcopy(a)
# b[3].append(200)  # глубокое копирование со всеми внутренними ссылками при помощи .deepcopy()
# print(b)
# print(a)


############
# ctrl + alt + L - выровнить все по pep8
############
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for line in matrix:
#     for number in line:
#         print(number)
#
# print('\n', matrix[2][2], end='')


# name = input('Name: ')
# print(name or 'Guest')  # если ввожу имя - оно выводится (if true), а если нет имени - выводится guest (if false)


# # тернарный оператор - сократить конструкцию if else в одну строку
# age = int(input('Age: '))
# print('Welcome' if age >= 18 else 'No access')  # только if / else (elif нельзя впихнуть)


# # выполнить функцию если условие верно (такое лучше избегать)
# def admin():
#     print('I am admin')
#
#
# login = input('login: ')
# admin() if login == 'admin' else print('Hello user')  # выполнить функцию если условие верно


# x = [1, 2, 3]
# y = x
# print(x is y)  # функция "is" проверяет равенство - если верно, то выводит true
# a = 10
# b = 10
# print(a is b)  # если значения переменных равны то питон умно ссылается на одну ячейку памяти
# # кэшируются области памяти от -5 до 256 (все что выше будут разные id - если числа равны)
# # более подробно загуглить - литералы интов в питоне
# a = 300
# b = 300
# print(a is b)  # но здесь pyCharm сам закэшировал, а в консоли false


# генераторные вырожения
# result = []
# for i in range(10):
#     result.append(i)
# print(result)
#
# result_1 = [i for i in range(10)]  # добавь i из такого то цикла [что получить | как это получить]
# print(result_1)
# result_2 = [i*2 for i in range(10)]
# print(result_2)
# result_3 = [i for i in range(-10, 10)]  # диапазон от -10 до 10 (десять не включая)
# print(result_3)
# result_4 = [i for i in range(-10, 10) if i > 0]  # из ренджа с условием
# print(result_4)
# result_5 = [i for i in range(-10, 10) if i % 2 == 0]  # из ренджа с условием
# print(result_5)

#
# keys = 'qwerty'
# values = (1, 2, 3, 4, 5, 6)
# my_dict = {key: value * 2 for key, value in zip(keys, values)}
# print(my_dict)


# виды ошибок
# 1 - dec вместо def (синтаксичекая ошибка)
# 2 - a=[] b=a[0] (индескная оибка / ошибка выполнениея)
# 3 - не правильно считается (семантическая / логическая ошибка)
# a = [1, 2]
# try:  # поробовать выполнить
#     b = a[5]
# # когда изначально знаем класс ошибки
# except IndexError:  # если будет IndexError то писать 'Неверный индекс'
#     print('Неверный индекс')

#
# a = [1, 2]
# try:  # поробовать выполнить
#     b = a[5]
# # если мы не знаем какая ошибка будет
# except Exception as e:  # всегда использовать переменную e
#     print(e.__class__)  # посмотреть какой класс ошибки у переменной e (Exception)

#
# age = ''
# while age == '':
#     try:
#         age = 100 / int(input('input age: '))
#     except ValueError:
#         print('вы должны были ввести число')
#     except ZeroDivisionError:
#         print('Деление на ноль')
#
# print('100 поделенное на ваш возраст =', age)


#
# регулярные выражения

# import regular expression
import re
# \.{2,} - встриться 2 или более раз
pattern = '([a-zA-Z0-9_.]+@[a-z]+\.{1,9}(ru|org|com))'  # \.{1,9} - встретить точку от 1 до 9 раз
email = 'alex@mail.ru'
# print(re.match(pattern, email))  # ищет сначала строки
# print(re.match(pattern, email).group(1))  # здесь нумерация не от нуля а от 1
# print(re.search(pattern, email))  # может найти в тексте !!!!!!!!!!!!!alex@mail.ru (и покажет где начало)

text = 'wrjwqnwroq alex@mail.ru asfasf alex@mail.ru sfafas alex@mail.ru afasfagagwga'
print(re.findall(pattern,text))
















