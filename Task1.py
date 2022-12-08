# 1'. Вычислить число Пи c заданной точностью d

# Пример: 

# при d = 0.001, π = 3.141
# при d = 0.0001, π = 3.1415
 
import math

def round_pi(d):
    d.split('.')[1]
    n = ''
    f = 0
    for i in d:
        if i == ',':
            i = '.'
        if f == 1:
            n = n + i
        if i == '.':
            f = 1
    result = round(math.pi, len(n))
    return result
