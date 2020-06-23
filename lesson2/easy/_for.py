list_a = [1, 2, 3, 4, 5]

# for a in list_a:
#     print(a)
#     list_a.remove(a)
# print('final list: ', list_a)
#
# print('\n')

for a in list_a.copy():  # создать копию элемента
    print(a)
    list_a.remove(a)
print('final list: ', list_a)

print('\n')

# for a in list_a[:]:  # можно сделать срез и по сути создать ту же самую копию
#     print(a)
#     list_a.remove(a)
# print('final list: ', list_a)


