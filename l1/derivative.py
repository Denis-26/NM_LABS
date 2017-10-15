def derivative(coeffs):
    return ([coeff*((len(coeffs)-i)-1) for i, coeff in enumerate(coeffs)])


if __name__ == '__main__':
    print(derivative([2,3,4,3,2]))
