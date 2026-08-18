def evel_quadratic(a, b, c, x):
    return a*x**2 + b*x + c
def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    result1 = evel_quadratic(a1, b1, c1, x1)
    result2 = evel_quadratic(a2, b2, c2, x2)
    return result1 + result2

print(two_quadratics(2, 2, 2, 2, 2, 2, 2, 2))

#this is teh second finger exercise for the 7 lesson of mit6.100.
