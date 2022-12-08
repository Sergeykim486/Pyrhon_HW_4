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