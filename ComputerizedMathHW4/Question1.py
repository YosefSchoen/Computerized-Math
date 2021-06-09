import sympy as sp
import pprint
import math as m

# Q1
def Q1():
    x = sp.symbols('x')
    integ = sp.Integral(1 / (1 + pow(x, 2)), x)

    pprint.pprint(integ)
    pprint.pprint((integ.doit()))
    return


# Q2
def Q2():
    x, y, yp, yc = sp.symbols('x y yp yc')
    z, z1, z2 = sp.symbols('z z1 z2')
    c0, c1, c2, c3 = sp.symbols('c0 c1 c2 c3')
    A, B = sp.symbols('A B')

    expr = pow(z, 2) + 4*z + 4
    sol = sp.solve(expr, z)

    pprint.pprint(sol)

    if len(sol) == 1:
        yp = (A + B*x)*sp.exp(z1*x)

    if len(sol) == 2:
        yp = (A * sp.exp(z1)) + (B * sp.exp(z2*x))


    yc = c0 + c1*x + c2*(x**2) + c3*(x**3)
    dyc = sp.diff(yc, x)
    ddyc = sp.diff(dyc, x)

    ydict = sp.collect(yc + 4*dyc + 4*ddyc, x, evaluate=False)
    c3 = 1

    exp0 = ydict[x**0]
    exp1 = ydict[x**1]
    exp2 = ydict[x**2]
    exp3 = ydict[x**3]

    sc3 = sp.solve(sp.Eq(exp3, 1))

    exp2 = exp2.subs('c3', sc3[0])
    sc2 = sp.solve(sp.Eq(exp2, 0))

    exp1 = exp1.subs('c2', sc2[0])
    exp1 = exp1.subs('c3', sc3[0])
    sc1 = sp.solve(sp.Eq(exp1, 0))

    exp0 = exp0.subs('c1', sc1[0])
    exp0 = exp0.subs('c2', sc2[0])
    exp0 = exp0.subs('c3', sc3[0])
    sc0 = sp.solve(sp.Eq(exp0, 0))

    yc = sc3[0]*x**3 + sc2[0]*x**2 + sc1[0]*x + sc0[0]
    y = yp + yc

    pprint.pprint("yp = " + str(yp))
    pprint.pprint("yc = " + str(yc))
    pprint.pprint("y = " + str(y))
    return


#Q3
x = sp.symbols('x')
expr = pow(x, 5) + sp.sin(x)

dexpr1 = sp.diff(expr, x, 1)
dexpr2 = sp.diff(expr, x, 2)
dexpr3 = sp.diff(expr, x, 3)
dexpr4 = sp.diff(expr, x, 4)

pprint.pprint(dexpr1)
pprint.pprint(dexpr2)
pprint.pprint(dexpr3)
pprint.pprint(dexpr4)


x = sp.symbols('x')
expr = 1 / (pow(1 + x, 3))


nthderivatives = []

for i in range(1, 100):
    orderi = sp.diff(expr, x, i)
    nthderivatives.append(orderi)
pprint.pprint(expr)

expr = expr.subs(x, 7/22)
maclaurin = expr
for i in range(0, 99):
    maclaurin = maclaurin + nthderivatives[i]*pow(x, i) / sp.factorial(i)
    maclaurin = maclaurin.subs(x, 7/22)

pprint.pprint(maclaurin)


x = sp.symbols('x')
expr = (x + 1)*(x + 2)*(x + 3)
exprexpanded = sp.expand(expr)
pprint.pprint(exprexpanded)

expr = x**4 + (8 * x**3) + (6 * x**2)
factorized = sp.factor(expr)
fact1 = factorized / x**2

pprint.pprint(factorized)
pprint.pprint(sp.factor(fact1))
