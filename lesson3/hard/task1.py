# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


player = {'name': input('Введите имя: '), 'health': 100, 'damage': 50}
enemy = {'name': input('Введите имя: '), 'health': 100, 'damage': 50}

print(player['damage'])


def attack(who_attack, who_defend):
    who_defend['health'] -= who_attack['damage']  # обращаемся в словарь по ключу
    # who_defend['health'] = who_defend['health'] - who_attack['damage']


attack(player, enemy)
print(enemy['health'], player['health'])




