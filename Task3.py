# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

def uniquelist(list1):
    res = []
    for i in list1:
        f = 0
        for j in res:
            if j == i:
                f = 1
        if f == 0:
            res.append(i)
    return res
                
def listgen(n):
    res = []
    for i in range(n):
        res.append(random.randint(1, 10))
    return res

