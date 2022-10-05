# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = input(
    "Введите список вещественных чисел, разделенных пробелом: ").split()
num_list = [float(i) for i in list1]
result = []
for i in num_list:
    if i % 1 != 0:
        float_num = i % 1
        result.append(float_num)
print(f"Список дробных частей -> {result}")
min_float = min(result)
max_float = max(result)
result = round(max_float - min_float, 2)
print(f"Минимальная дробная часть -> {min_float}")
print(f"Максимальная дробная часть -> {max_float}")
print(result)
