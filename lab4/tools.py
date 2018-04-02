from math import factorial as fac
import numpy as np

def get_y_data(file):
    with open(file, "r") as data:
        data = data.read().strip().split('\n')
        return [float(i) for i in data]

def gen_x(start, step, count):
    acc = [start]
    for i in range(count-1):
        start += step
        acc.append(round(start, 5))
    return acc

def difference_table(X, Y):
    res = []
    while len(Y):
        dY = [(Y[i] - Y[i-1]) for i in range(1, len(Y))]
        if not any(dY):
            break
        dY = [round(_, 4) for _ in dY]
        res.append(dY.copy())
        Y = dY.copy()
        dY = []
    return res

def P_x(q, y_n, DY):
    calc_q = lambda q, q_f, count: q if count == 0 else q*(q_f + count)
    count = 0
    q_f = q
    res = y_n
    for y in DY:
        q = calc_q(q, q_f, count)
        res += (q * y) / fac(count+1)
        count += 1
    return res

def _l_i(X, x):
    def wrap(x):
        frac = lambda x, x_j, x_i: (x-x_j)/(x_i-x_j)
        result = 1
        res = []
        for i in range(len(X)):
            for j in range(len(X)):
                if i != j:
                    result *= frac(x, X[j], X[i])
            res.append(result)
            result = 1
        return res
    return wrap

def L(X, Y):
    def wrap(x):
        result = 0
        l_i_res = _l_i(X, x)(x)
        for y, l in zip(Y, l_i_res):
            result += l*y
        return result
    return wrap
