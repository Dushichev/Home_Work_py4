#Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю.
#Задача - сформировать файл, содержащий сумму многочленов

from random import randint
import itertools

k = randint(1, 5)

def get_rat(k):
    rat = [randint(0, 10) for i in range (k + 1)]
    while rat[0] == 0:
        rat[0] = randint(1, 10) 
    return rat

def get_poly(k, rat):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(rat, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


rat = get_rat(k)
polynom1 = get_poly(k, rat)
print(polynom1)

with open('poly_1', 'w') as data:
    data.write(polynom1)

k = randint(2, 5)

rat = get_rat(k) 
polynom2 = get_poly(k, rat)
print(polynom2)

with open('poly_2', 'w') as data:
    data.write(polynom2)