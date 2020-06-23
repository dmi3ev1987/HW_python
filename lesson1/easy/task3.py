# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

user_age = int(input('please input your age: '))
if user_age >= 18:
    print('access granted')
else:
    print('we are too sorry, but you cannot use this site')
