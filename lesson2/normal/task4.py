# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]

temp_lst1 = []
temp_lst2 = []

temp_lst1 = list(set(lst))
print(temp_lst1)

for old_i in lst:
    if old_i not in temp_lst1:
        temp_lst1.append(old_i)
print(temp_lst1)


count = 0
i = 0

while i < len(lst):
    count = 0
    for new_i in lst:
        if new_i == lst[i]:
            count += 1
            # print(count)
    if count == 1:
        temp_lst2.append(lst[i])
    i += 1
print(temp_lst2)


second_a = list()  # []
for elem in lst:
    if lst.count(elem) == 1:
        second_a.append(elem)
print(second_a)

