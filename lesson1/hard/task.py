# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.

# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.

# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

name = input('введите ваше имя: ')
surname = input('введите вашу фамилию: ')
age = int(input('введите ваш возраст: '))
weight = int(input('введите ваш вес: '))

if age <= 30 and 50 <= weight <= 120:
    print('Уважаемый ', name, surname, 'вы в хорошой форме')
elif 40 >= age > 30 and 50 >= weight or 40 >= age > 30 and weight >= 120:
    print('Уважаемый ', name, surname, 'вам следует начать вести правильный образ жизни')
elif age > 40 and 50 >= weight or age > 40 and weight >= 120:
    print('Уважаемый ', name, surname, 'вам требуется врачебный осмотр!')

# if age <= 30 and 50 <= weight <=120:
#     print('Уважаемый ', name, surname, 'вы в хорошой форме')
# elif age > 40 and (weight <50 or weight > 120):
#     print('Уважаемый ', name, surname, 'вам требуется врачебный осмотр!')
# elif age > 30 and (weight <50 or weight > 120):
#     print('Уважаемый ', name, surname, 'вам следует начать вести правильный образ жизни')
# else:
#     print('Мой врачебный опыт не велик, приходите позже, когда будете подходить под формулу=) ')

