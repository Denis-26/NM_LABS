from Zeidel import seidel
from Choletsky import choletsky
import numpy as np

A = [
    [5,      1,  -1,  2],
    [0.5,    4,   2,   -1],
    [1,    0.2,  -6,   3],
    [1,   -0.5,  3,   -6]
]
B = [11, -4, -22.4, -8]

def main():
    result_s = seidel(A, B, 0.00001)
    result_c = choletsky(A, B)

    print("Seidel method")
    for i, el in enumerate(result_s):
        print('x{} = {}'.format(i+1, el))
    print("Check result: {}\n".format(np.allclose(np.dot(A, result_s), B)))

    print("Choletsky method")
    for i, el in enumerate(result_c):
        print('x{} = {}'.format(i+1, el))
    print("Check result: {}".format(np.allclose(np.dot(A, result_c), B)))

if __name__ == '__main__':
    main()
