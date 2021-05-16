import sympy

x , y = sympy.symbols("x, y")
f = x * (y ** 2) * sympy.ln(x ** 2)

for v1 in [x, y]:
    for v2 in [x, y]:
        for v3 in [x ,y]:
            if v1 + v2 + v3 == 2 * x + y:
                sympy.pprint(sympy.Derivative(f, v1, v2, v3))
                print('=', sympy.diff(f, v1, v2, v3))