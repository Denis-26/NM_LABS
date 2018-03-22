from math import factorial as fac
import numpy as np

def difference_table(X, Y, x_0, dx, n):
    res = []
    while len(Y):
        dY = [(Y[i] - Y[i-1]) for i in range(1, len(Y))]
        if not any(dY):
            break
        dY = [round(_, 4) for _ in dY]
        res.append(dY.copy())
        Y = dY.copy()
        dY = []
    for i in res:
        print(i)


def calc_q(q, q_f, count):
    if count == 0:
        return q
    return q*(q_f + count)

def P_x(q, y_n, DY):
    count = 0
    q_f = q
    res = y_n
    for y in DY:
        q = calc_q(q, q_f, count)
        res += (q * y) / fac(count+1)
        count += 1
    return res

if __name__ == '__main__':
    X = [15, 20, 25, 30, 35, 40, 45, 50, 55]
    Y = [0.2588, 0.3420, 0.4226, 0.5000, 0.5736, 0.6428, 0.7071, 0.7660, 0.8192]
    difference_table(X, Y, 1, 2, 10)
    last = [0.0532, -0.0057, -0.0003, 0.0002, 0.0002, 0.0003, 0.0005, 0.0008]
    q = lambda x, x_n, h: (x - x_n)/h
    for x in [14, 27, 32, 48, 56]:
        print("q =", q(x, 55, 5))
        print(P_x(q(x, 55, 5), 0.8192, last))
