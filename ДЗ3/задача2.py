# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



entered_list = input("Введите список чисел, разделенных пробелом: ").split()
list1 = [int(i) for i in entered_list]
list2 = []
n = int(len(list1))
for i in range(len(list1)):
    if i < len(list1)/2  and n > len(list1)/2:
        a = list1[i] * list1[n-1]
        i+=1
        n-=1
        list2.append(a)
print(f"Список чисел: {list1}")
print(list2)
