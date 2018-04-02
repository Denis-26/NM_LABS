def _gorner(coeffs: list, point)->list:
#    inverted_coeffs = coeffs * (-1) if coeffs[0] < 0
    gorner_coeffs = [0] * len(coeffs)
    for i in range(0, len(gorner_coeffs)):
        gorner_coeffs[i] = gorner_coeffs[i-1]*point+coeffs[i]
    return gorner_coeffs

def upper_border(coeffs):
    start_point = delta = 1
    while True:
        result = _gorner(coeffs, start_point)
        if result[0] >= 0 and all(map(lambda x: x > 0, result)):
            return start_point
        start_point += delta


def lower_border(coeffs):
    transformed_coeffs = [((-1)**i)*coeff for i, coeff in enumerate(coeffs)]
    start_point = delta = 1
    while True:
        result = _gorner(transformed_coeffs, start_point)
        if result[0] >= 0 and all(map(lambda x: x > 0, result)):
            return -start_point
        start_point += delta
