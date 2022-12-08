# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 6 -> [1,2,3]
# 144 -> [2,3]

def Multiplier(n):
    an = []
    i = 2
    while n > 1:
        while n % i == 0:
            an.append(i)
            n //= i
        i += 1

    result = []
    for j in an:
        find = 0
        for k in result:
            if k == j:
                find = 1
        if find == 0:
            result.append(j)
    
    return result