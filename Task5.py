# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

import sympy
def sum_of_pol():
    file1 = open('file 1.txt', 'r')
    f1 = str(file1.read())
    file1.close()
    file2 = open('file 2.txt', 'r')
    f2 = str(file2.read())
    file2.close()
    resfile = open('file result.txt', 'w')
    f3 = str(sympy.simplify(f1 + '+' + f2))
    resfile.write(f3)
    resfile.close()
    return [f1, f2, f3]