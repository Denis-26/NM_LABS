import tools

def task_1(X, Y, step, q_func, nodes):
    table = tools.difference_table(X, Y)
    last = list(map(lambda cell: cell[-1], table))
    return [tools.P_x(q_func(x, X[-1], step), Y[-1], last) for x in nodes]

def task_3(X, Y, nodes):
    L_i = tools.L(X, Y)
    return [L_i(n) for n in nodes]

if __name__ == '__main__':
    step = 0.005

    X1 = tools.gen_x(1.415, step, 13)
    Y1 = tools.get_y_data("data_task1.txt")

    X2 = [0.298, 0.303, 0.310, 0.317, 0.323, 0.330, 0.339, 0.350, 0.359]
    Y2 = tools.get_y_data("data_task3.txt")

    q_func = lambda x, x_n, h: (x - x_n)/h

    nodes1 = [1.4625 - 0.001*n for n in range(1, 31)]
    nodes2 = [0.765 - 0.025*n for n in range(5, 16)]

    res1 = task_1(X1, Y1, step, q_func, nodes1)
    res2 = task_3(X2, Y2, nodes2)
    
