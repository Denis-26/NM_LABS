from Zeidel import seidel
from Choletsky import choletsky
from check_time import check_time
import numpy as np

A = [
    [5,      1,  1,  2],
    [0.5,    4,   2,   -1],
    [1,    0.2,  -6,   3],
    [1,   -0.5,  3,   -6]
]
B = [11, -4, -22.4, -8]

def main():
    time, result_s = check_time(seidel, A, B, 0.0001429)
    print("Time of Seidel method: {}".format(time))

    time, result_c = check_time(choletsky, A, B)
    print("Time of Choletsky method: {}".format(time))

    print("Choletsky method")
    for i, el in enumerate(result_c):
        print('x{} = {}'.format(i+1, el))
    print("Подставим в исходную матрицу ответ и получим: ", np.dot(A, result_c), end='\n\n')

    print("Seidel method")
    for i, el in enumerate(result_s):
        print('x{} = {}'.format(i+1, el))

    print("Подставим в исходную матрицу ответ и получим: ", np.dot(A, result_s))
if __name__ == '__main__':
    main()
