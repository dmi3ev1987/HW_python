# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# list3 = list(set(list1) - set(list2))
#
# print(list3)

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

for b in list_b:
    # print(b)
    while b in list_a:
        list_a.remove(b)
print(list_a)

