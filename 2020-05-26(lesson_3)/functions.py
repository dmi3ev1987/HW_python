##########
# max, min, len, print, range, input, enumerate, sum  # основные функции

# x = max(1, 2, 3)
# print(x)
# print(max('z', 'aaa'))  # смотрить по ASCII
# print(max('z', 'aaa', key=len))  # по длине строки key=len

# print(round(1.999))
# print(round(1.98754, 2))  # сколько знаков после запятой я хочу увидеть

# for index, char in enumerate('qwerty', 3):
#     print(index, char)


#
# пишем свои функции
#


# def say_hello():  # def - define (создать/определить новую(свою) функции)
#     print('hello')
#
#
# def say_hello_2(name):  # def - define (создать/определить новую(свою) функции)
#     print('Hello', name)
#
#
# say_hello()
# say_hello_2('Ivan')


# def average(numbers):
#     count = len(numbers)
#     all_sum = sum(numbers)
#     # print(all_sum/count)
#     answer = all_sum / count
#     return answer  # return это своего рода break (он прерывает функции)
#     print('qwerty')  # после ретерна не будет выводиться
#
#
# avg_num = average([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(avg_num)

# def print(text):  # если назвать именем стандартной функции то она заменит стандартную
#     pass  # заглушка чтобы можно было закончить функцию потом и при этом python не ругался


# # глобальные и локальные переменные
# x = 100  # глобальная переменная
# def test():
#     # print(x)  # bad practice
#     # global x  # берем глобальный x  # bad practice
#     x = 10  # локальная переменная
#     return x
#
#
# # test()
# x = test()
# print(x)

# # аргументы
# def my_func(name, surname='Guest'):  # surname - argument with default value(значение) - default always the last
#     print(name, surname)
#
#
# my_func('Ivan')
# my_func('Ivan', 'Ivanov')


# def func(name, *args):
#     print(name)
#     print(args)
#
#
# func('Ivan', 10, 20, 30, 40, 50, 60, 70, 80, 90)

# def func(name, age, surname='Guest'):  # необязательный элемент обязательно должен быть в конце
#     print(name, surname, age)
#
#
# func('Ivan', 50, 'Ivanov')
# func(surname='Ivanov', name='Ivan', age='50')  # order is not important when we know key and value
# func('Ivan', surname='Ivanov', age='50')  # this is also correct
# func('Ivan', age='50')  # this is also correct


# def func(name, **kwargs):  # key word arguments (kwargs) - create a dictionary whit key + value
#     print(name, kwargs)
#
#
# func('Ivan', surname='Ivanov', age='50', flat=160)


# # builtin functions (встроенные функции)
#
# names = ['Ivan', 'Oleg', 'Sosed']
# ages = (35, 45, 80)
#
# zip ########
# for name, age in zip(names, ages):  # glued two elements(list and tuple) in one
#     print(name, age)
#
# print(list(zip(names, ages)))
# print(dict(zip(names, ages)))

# x = 4
# print(pow(x, 2))  # возведение х в степень

# def my_pow(x):
#     return x**2
#
#
# data = [-2, -10, 6, 19]
# result = []

# for num in data:
#     rs = my_pow(num)
#     result.append(rs)
# print(result)

# map ############
# # при помощи map замениям то что было в цикле for выше
# result1 = list(map(my_pow, data))  # my_pow без скобок, чтобы не передавать туда значения (1.фунция;2.итерируемый об.)
# print(result1)


# filter ##########
# def my_filter(x):
#     return x > 0  # если х больше, то return будет true, а если х меньше 0, то return будет false
#
#
# result2 = list(filter(my_filter, data))  # my_filter будет запускать по мере того как будет запускаться filter
# print(result2)

# # анонимная люмбда функция
# data = [-2, -10, 6, 19]
# result = list(map(lambda x: x ** 2, data))  # x: x ** 2 - как бы return (заменяет map который выше)
# print(result)
# result = list(filter(lambda x: x > 2, data))  # x: x > 2 - как бы return (заменяет filter который выше)
# print(result)


########################
# работа с файлами

# file = open('1.txt')
# file = open('1.txt', 'r')  # 'r' - read from file - default value
# for line in file:
#     print(line, end='')  # end='\n' - default value for end argument
#     print(line.strip())  # убрать все системные переносы в конце строки


# file = open('2.txt', 'w')  # 'w' - write - если запустить еще раз то он перезапишет и не будет ничего спрашивать
# # 'a' - append (дозапись); 'a+' -дозапись и чтение; 'w+' (и запись и чтение)
# # r, w, a, a+, w+
# file.write('1000')
# file.close()  # обязательно закрывать чтобы сохранилось и не висело в памяти

# file = open('2.txt', 'a+', encoding='utf-8')  # лучше писать encoding (т.к. по дефолту encoding=''cp1251')
# file.write('\na\n')
# print(file.readlines())  # когда a+ то он принтом не выведет ничего - т.к. указатель в конце файла
# file.seek(0)  # перевести указатель(курсор) на первую строку - seek(0) - позиция в байтах
# print(file.readlines())  # а после seek(0) выведет все
# file.close()

##################
# # life hack (в такой конструкции писать close не нужно)
# # пищем то что написанно наверху через with

# with open('1.txt', encoding='utf-8') as f:  # file = open('1.txt', 'a+', encoding='utf-8')
#     for line in f:
#         print(line.strip())
