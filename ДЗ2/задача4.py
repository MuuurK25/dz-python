# Реализуйте алгоритм перемешивания списка.

import random

list_1 = [random.randint(0,10) for i in range(random.randint(5,10))]
print(f"Исходный список:\n {list_1}")
random.shuffle(list_1)
print(f"Список после перемешивания:\n{list_1}")