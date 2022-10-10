#Задайте последовательность чисел. Напишите программу, 
#которая выведет список неповторяющихся элементов исходной последовательности.

pos_number = list(map(int, input("Введите числа через запятую:\n").split(",")))
#print(f"Исходный список: {pos_number }")
new_list = []
[new_list.append(i) for i in pos_number if i not in new_list]
print(f"Список из неповторяющихся элементов: {new_list}")