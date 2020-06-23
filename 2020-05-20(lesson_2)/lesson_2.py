# расставить все пробелы по PEP 8 (Ctrl + Alt + L)

# name_of_person =  # так именуются обычные переменные (пока что именуем все так)
# Name_Of_Person =  # camel style - в питоне именуем обычно классы


# name_of_person = "Анастасия"
# print(type(name_of_person))

# методы
# срезы

# print(name_of_person[0])
# print(name_of_person[1])
# print(name_of_person[2])
# print(name_of_person[3])
# print(name_of_person[8])
# print(name_of_person[-1])  # первый элемент с конца
# print(name_of_person[-2])  # второй элемент с конца

# print(name_of_person[0:5])  # получаем "срез" от 0 (элемент берется) до 5 (не включая - элемент не берется )
# print(name_of_person[:5])  # короткая запись, если я иду сначала
# print(name_of_person[:])  # весь элемент
# print(name_of_person[2:])  # от 2го элемента и до конца

# print(name_of_person[0:8:2])  # интервал от 0 до 8 с интервалом(шагом) 2 (каждый второй)
# print(name_of_person[0:8:3])
# print(name_of_person[0:9:1])  # [от:до:шаг]
# print(name_of_person[::-1])  # вывести в обратном порядке (от начала до конца в обратном порядке)


# email = 'welcome@mail.ru'
# index = email.find('@')  # находим позицию(индекс) "@"
# print(index)
# print(email[:index])


# name = 'ПеТрОв иВаНоВ Иванович'

# print(name.lower())  # все маленькими буквами (нижний регистр)
# print(name.upper())

# print(name.capitalize())  # только первая буква в строке заглавная, а все остальные мальеникие
# print(name.title())  # каждая буква с заглавной буквы

# print(len(name))  # подсчитывает длину строки включая пробелы
# print(name.count('о'))  # подсчитывает количество указанных в скобках символов
# print(name.lower().count('о'))  # подсчитывает количество указанных в скобках символов без учета регистра
# print(name.split())  # создает список(list) из строки с разделителем "пробел" в строке
# print(name.split('В'))  # создает список из строки с разделителем "В" в строке

# email = 'welcome@mail.ru'
# print(email.split('@'))  # создает список(list) из строки с разделителем "@" в строке

##############
##############
# самостоятельно разобрать что делают эти две функции (прочитать в документации на английском)
# .ljust
# .rjust
##############
##############


# name = 'Ivan'  # строки неизменяемый тип данных
# age = 30
# money = 200.2
# print('Привет', name, 'вам', age, 'лет у вас', money)

# result = 'Привет %s вам %i лет у вас %f' % (name, age, money)  # запоминаем что такой есть но не пользуемся
# result = 'Привет {} вам {} лет у вас {}'.format(name, age, money)  # здесь не нужно задумываться о типе переменной
# result = f'Привет {name} вам {age} лет у вас {money}'  # fstring (здесь не перепутаешь переменные местами)
# print(result)


#####################################
# списки  # List - изменяемый список#

# name = 'Sergey'
# humans = ['Ivan', 'Alex', 'Olga', name]
#
# # print(humans)
# # print(humans[0])  # list - изменяемый список
# # print(humans[1:])
# # print(humans[::2])  # каждого второго
# # print(humans[::-1])  # все в обратном порядке
#
# humans.append(10)  # метот - добавить элемент в конец списка
# print(humans)
# humans.insert(1, 'Ivan')  # (вставка) заменить элемент с индексом 1 значением "200"
# print(humans)
# print(humans.index(name))  # какая позиция (индекс) у "name"
# humans.remove('Ivan')  # remove идет слева и удаляет первый попавшийся элемент
# print(humans)
# deleted_element = humans.pop(-1)  # удаляет элемент по индексу (метод может возвращать удаленный элемент в переменную)
# print(humans)
# print(deleted_element)
#
# print('Olga' in humans)  # есть ли имя Ольга в списке humans
# print('Den' in humans)  # есть ли имя Den в списке humans

# string = 'qwe'
# print('q' in string)  # и для строки тоже работает


################
# вложенность  #

# list (список - изменяемый)
# x = [1, 2, 3, ['qwe', 'asd']]
# print(x[3][0])  # выводим qwe из вложенного списка
# print(x[-1][0])  # выводим qwe из вложенного списка

# tuple кортеж (неизменяемый и соответсвенно занимает меньше памяти)
# humans = (1, 2, 3, 4, 5)
# print(type(humans))
# print(humans[0])
# print(humans[1:])
# print(list('qwe'))  # преобразует строку в список по буквам
# print(list(humans))  # преобразует котреж в список


############
# цикл for #

# humans = (1, 2, 3, 4, 5)
# humans = ('Ivan', 'Alex', 'Olga')

# # создаем цикл for своими силами (как будто его не знаем)
# x = 0
# print('Длина переменной: ', len(humans))
# while x < len(humans):
#     print(humans[x])
#     x = x + 1

# for name in humans:  # вместо name можно написать любую переменную
#     print(name)
# print('Длина переменной: ', len(humans))
# for i in humans:
#     print(i)
# for letter in 'qwerty':
#     print(letter)

# for i in [1, 2, 3, 4, 5]:
#     print(i, 'Привет')

# for _ in [1, 2, 3, 4, 5]:  # используем мусорную переменную "_" если мы не хотим использовать переменную в цикле
#     print('Привет')
#
# print('hello \n' * 5)

# for i in range(10):  # сделать что-либо 10 раз (или сколько угодно раз в зависимости от условия)
#     print(i, 'Привет')


########################
# словари # dictionary #

# human = {'name': 'Илья', 'age': 43, 'money': 39.1}
# human['data'] = [1, 2, 3, 4]
# human['input'] = input('input: ')
# print(human['name'])
# print(human['age'])
# print(human['money'])
# print(human.get('qwe'))  # если такого ключа qwe нету - то программа не падает
# print(human.get('name'))  # .get - метод который позволяет использовать ключи, которые мы не уверены, что существуют

# print(human.pop('age'))  # вырезает переменную с ключом "age"
# print(human.popitem())  # вырезает последний элемент и  возвращает его в качестве кортежа
# print(human)

# for key in human.keys():  # возвращает все ключи в словаре
#     print(key)
#
# print('\n')
#
# for value in human.values():  # возвращет все занчения в словаре
#      print(value)
#
# print('\n')

# for key, value in human.items():  # мы сразу можем разбивать на две переменные (а не на один кортеж)
#     print(key, value)


#############
# множества #

# my_set = {1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6}  # {} как словарь только нет пар(ключей)
# print(my_set)  # выведет набор уникальных чисел

# my_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6]
# print(my_list)
# print(set(my_list))  # при помощи set преобразуем list в множество
# print(len(set(my_list)))  # здесь всего 6 разных чисел

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)  # | - значит объединение для множеств
# print(a == b)  # сравнение
# print(a & b)  # пересечение
# print(a - b)  # разница
# print(b - a)  # разница
# print(a ^ b)  # все кроме пересечения






