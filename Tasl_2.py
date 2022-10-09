#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#70 = 2*5*7 => [2, 5, 7]
#140 = 2*2*5*7 => [2, 2, 5, 7]


number = int(input("Введите число: "))
i = 2 
list_prostyh_chisel = []
#old = number
while i <= number:
    if number % i == 0:
        list_prostyh_chisel.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители данного числа: {list_prostyh_chisel}")