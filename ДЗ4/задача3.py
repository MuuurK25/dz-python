# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# list1 = input("Введите список вещественных чисел, разделенных пробелом: ").split()
# num_list = [float(i) for i in list1]
# result = []

from itertools import count


entered_list = input("Введите список чисел, разделенных пробелом: ").split()
list1 = [int(i) for i in entered_list]
list2 = []

for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
print(list2)
