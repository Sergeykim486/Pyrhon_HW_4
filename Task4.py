# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 

import random
import sympy
k = random.randint(1,5)
def polinom_gen(k):
    k = k+1
    res = ''
    for i in range(k):
        tmp = f'{random.randint(0,10)}*x**{i}'
        if i == 0:
            res = tmp
        else:
            res = tmp + '+' + res
    return str(sympy.simplify(res))

def save_to_file(pol, file_name):
    f = open(f'{file_name}.txt', 'w')
    f.write(pol)
    f.close()
    print(f'-->    Файл: {file_name}.txt - Сохранен.')