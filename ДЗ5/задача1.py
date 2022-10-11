# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

input_str = input()
text = "абв"
input_list = input_str.split()
result_list = []
for word in input_list:
    if text not in word:
        result_list.append(word)
print(" ".join(result_list))
