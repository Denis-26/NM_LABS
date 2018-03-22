from math import cos, sin
from numpy.linalg import det, inv
from numpy import array

def Newton(X0, e, F, F_d):
    print("Solving system by NEWTON METHOD")
    yako_m = F_d
    X0 = array(X0)
    XN = array([0,0])
    while all([abs(i) >= e for i in X0 - XN]):
        Fx_0 = array([f(*X0) for f in F])
        Wx_0 = [[0 for y in range(len(F))] for x in range(len(F))]
        for i in range(len(F)):
            for j in range(len(F)):
                Wx_0[i][j] = yako_m[i][j](*X0)
        det_ = det(Wx_0)
        if not det_:
            print("Определитель равен 0, обратная матрица не существует")
            return
        inv_ = array(inv(Wx_0))
        XN = X0.copy()
        X0 = X0 - (inv_.dot(Fx_0))
    print("Solution by Newton method is:", XN)
    check_result(XN, F)
    return XN


def check_result(result, F):
    r1 = F[0](*result)
    r2 = F[1](*result)
    print('After substitution into system:', r1, r2)
    if r1 < 0.001 and r2 < 0.001:
        print("Check Newton OK!")
    else:
        print("Check Newton FAIL!")
    print()
