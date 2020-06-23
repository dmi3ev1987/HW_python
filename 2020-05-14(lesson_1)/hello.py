# print('hello world!')
# комментировать строку Ctrl + /
# Ctrl + Alt + L - расставить все по PEP 8


# number = 10
# a = 10
# b = 20
# print('hello world!', number)
# print(a - b)
# print(b % a)  # остаток от деления
# print(a ** b)  # возвести в степень
# print(b // a)  # целочисленное деление


# a = 33
# A = 50
# print(type(a))
# b = 222.1
# print(type(b))
# c = 'Name'
# print(type(c))
# is_admin = True  # False
# print(type(is_admin))
#
# people = [10, 50, 'a', a, A]
# print(type(people))
# print(people)
# people.append(100)
# print(people)
# print(people[2])
#
# people_2 = (10, 50, 'a', a)
# print(type(people_2))
# print(people_2)
#
# human = {'name': 'ivan', 'age': 30, 'data': is_admin, A: 'LOL'}
# print(type(human))
# print(human)
# print(human['name'])
# print(human[A])

''' # три кавычки для коммента участа и спользуется для описания функции
a = 100
b = '1'
c = '100.2'
# print(a + b)  # error
print(a + int(b))
print(str(a) + b)
print(a + int(b) + float(c))
'''


# name = input('Your name: ')  # input - всегда выдает стринговый (str) тип данных
# print('Hello,', name)  # пробел добавлять после Hello, - добавлять не нужно т.к. ставиться запитая между аргументами


# age = int(input('Your age: '))
# print('Your age:', age + 10)


# print(type(5 > 1))
# print(5 > 1)
# print(5 < 1)
# print(5 == 1)  # операция сравнение (а равно ли пять одному?)
# print(5 == 5)
# print(5 != 4)  # а не равно ли? (не равно)
# print(5 >= 4)  # больше или равно
# print(5 <= 4)  # меньше или равно


# print(bool(0))  # если 0 то false (только в том случае когда 0)
# print(bool(''))  # либо когда здесь пустая строка (даже без пробела)
# print(bool(' '))  # либо когда здесь пустая строка (даже без пробела)
# print(bool(23))  # если любое число отлично от нуля то всегда true
# print(bool('any word'))  # true когда любая строка


# price = 100
# money = int(input('Money in the pocket: '))
#
# if money >= price:
#     print('you can buy it')
# elif price - money <= 5:
#     print('мы можем поторговаться')
# else:
#     print('it is too expensive for you')

# name = input('name: ')
# surname = input('surname: ')
# if name and surname:
#     print('you input name and surname')
# elif name:
#     print('you input only name')
# elif surname:
#     print('you input only surname')
# else:
#     print('you input nothing))))))))))))) try again later')

# number = int(input('input number from 1 to 5: '))
# while number < 1 or number > 5:
#     print('incorrect number please try again')
#     number = int(input('input number from 1 to 5: '))
# print('your input is correct')

# x = 0
# while x < 10:
#     print(x)
#     x += 1  # x = x +1  # тоже самое  # вместо плюса можно поставить минус или умножить или делеение

# ctrl + стрелочка вбок перемещаться по словам
# ctrl + стрелочка вверх/вниз прокручивать код вверх/вниз
# зажать ctrl + shift + стрелочка вверх/вниз - выделяет и перевещает целую строку вверх/вниз


x = 0
while x < 10:
    x += 1  # x = x +1  # тоже самое  # вместо плюса можно поставить минус или умножить или делеение
    if x == 8:
        break
    elif x == 4:
        continue  # это значит не выполнять оставшийся код в цикле и уходит в начало цикла
    print(x)

x = 0
while x < 10:
    print(x)
    x += 1
else:
    print('цикл завершился по условию')


