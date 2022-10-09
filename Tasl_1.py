#Вычислить число π c заданной точностью d
#Пример:
#при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)


import math
from math import pi

x = 100
chislo_pi = sum(1/16**i*(4/(8*i + 1) - 2/(8*i + 4) - 1/(8*i + 5) - 1/(8*i + 6)) for i in range(x))
print(chislo_pi)