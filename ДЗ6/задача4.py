# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# input_str = input("Введите текс")
# text = "абв"
# input_list = input_str.split()
# result_list = []
# for word in input_list:
#     if text not in word:
#         result_list.append(word)
# print(" ".join(result_list))

input_str = input("Введите текст")
text = "абв"
input_list = input_str.split()
result_list = [word for word in input_list if text not in word]
print(" ".join(result_list))