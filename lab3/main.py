from Newton import Newton, check_result
from Iteration import Iteration, check_iteration
from math import cos, sin, sqrt

F1 = [lambda x,y: cos(x) + y - 1.5, lambda x,y: 2*x - sin(y - 0.5) - 1]
F_d1 = [
    [lambda x,y: -sin(x), lambda x,y: 1],
    [lambda x,y: 2, lambda x,y: -cos(y - 0.5)]
]

F2 = [lambda x,y: sin(x+y) - 1.5*x + 1, lambda x, y: x**2 + y**2 - 1]
F_d2 = [
    [lambda x,y: cos(x+y) - 1.5, lambda x,y: cos(x+y)],
    [lambda x,y: 2*x, lambda x,y: 2*y]
]

if __name__ == '__main__':
    result = Newton([3.4, 3.2], 0.001, F1, F_d1)
    result1 = Iteration([0.8, -0.4], 0.001, F2, F_d2)
