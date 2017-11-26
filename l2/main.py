import numpy as n

def sum(i, j, lim, B, C):
    sum = 0
    for k in range(lim):
        sum += B[i][k]*C[k][j]
    return sum

def find_c_b(A):
    length = len(A[0])

    B = n.zeros((length,length))
    C = n.eye(length)

    for i in range(length):
        B[i][0] = A[i][0]

    for j in range(length):
        C[0][j] = A[0][j] / B[0][0]

    for i in range(1, length):
        for j in range(1, length):
            if i >= j:
                B[i][j] = A[i][j] - sum(i, j, j-1, B, C)
            if i < j:
                C[i][j] = (A[i][j] - sum(i, j, i-1, B, C))/B[i][i]

    return B, C

def solve_system(matrix, i, b):

    solve_system(matrix, i+1, )

def main():
    A = [
        [5,      1,  -1,  2],
        [0.5,    4,   2,   -1],
        [1,    0.2,  -6,   3],
        [1,   -0.5,  3,   -6]
    ]
    A1 = [
        [4, 2, -1, 0.5],
        [1, -5, 2, 1],
        [2, 1, -4, -1.5],
        [1, -0.4, 0.8, -3]
    ]
    b = [11, -4, -22.4, -8]
    ln = 4

    A = n.array(A1)

    B, C = find_c_b(A)

    print(B, "\n")
    print(C, '\n')

    print(n.dot(B, C))


if __name__ == '__main__':
    main()
