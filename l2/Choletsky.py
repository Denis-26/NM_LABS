import numpy as np

def split(A):
    length = len(A[0])
    B = np.zeros((length,length))
    C = np.eye(length)

    for i in range(length):
        B[i][0] = A[i][0]
    for j in range(length):
        C[0][j] = A[0][j] / B[0][0]

    for i in range(1, length):
        for j in range(1, length):
            if j <= i:
                sum1 = sum( [B[i][k] * C[k][j] for k in range(0, j)] )
                B[i][j] = A[i][j] - sum1
            if i < j:
                sum2 = sum( [B[i][k]*C[k][j] for k in range(0, i)] )
                C[i][j] = (A[i][j] - sum2)/B[i][i]
    return B, C

def choletsky(A, b):
    B, C = split(A)
    n = len(A)
    y = [0 for i in range(n)]
    x = [0 for i in range(n)]
    y[0] = b[0] / B[0][0]
    for i in range(1, n):
        sum1 = sum([B[i][k]*y[k] for k in range(0, i)])
        y[i] = 1/B[i][i]*(b[i] - sum1)

    x[n-1] = y[n-1]
    for i in range(n-1, -1, -1):
        sum2 = sum([C[i][k]*x[k] for k in range(i+1, n)])
        x[i] = y[i] - sum2

    return x
