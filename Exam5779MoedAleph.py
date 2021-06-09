from sympy import*
import math as m
import numpy as np
import matplotlib.pyplot as plt


# Question 2
print("Question2")
x, pi = symbols('x, pi')

expr = 1 / (x + (pi/2))**3
print(expr)

derivs = []
for i in range(0, 6):
	nthderiv = diff(expr, x, i + 1)
	derivs.append(nthderiv)

mclaurin = expr.subs(x, 0)

for i in range(0, 6):
	mclaurin = mclaurin + (derivs[i].subs(x, 0) * (x**(i+1)) / m.factorial(i+1))

print("mclaurin series is: " + str(mclaurin))

mclaurin = mclaurin.subs(x, 1/10)
mclaurin = mclaurin.subs('pi', m.pi)
print("for x = 1/10: " + str(mclaurin))
print("\n\n")

# Question 4
print("Question 4")
def f(x, y):
	return (5*x) / ((x**2) + 4)


#initial conditions
xi = 1
xf = 2
yi = 1

#step value
h = (xf - xi) / 10000

x = xi
y = yi

xList = [x]
yList = [y]

while x < xf - h:
	y = y + f(x, y)*h
	x = x + h
	
	xList.append(x)
	yList.append(y)


x, c = symbols('x c')
expr = (5*x) / ((x**2) + 4)
integ = Integral(expr, x)
antideriv = integ.doit()
c = 1 - antideriv.subs(x, 1)
print("f'(x) = " + str(expr))
print("f(x) = " + str(antideriv + c))

y = yi
yAlist = []

for i in xList:
	yAlist.append(antideriv.subs(x, i) + c)

reldiff = []
for i in range(0, len(xList)):
	reldiff.append(yAlist[i] - yList[i])


fig = plt.figure(num=None, dpi=80, figsize=(6,6), facecolor='w', edgecolor='k')
plt.plot(xList,yList,color='blue',lw=1,label='n')
plt.plot(xList,yAlist,color='red',lw=1,label='a')

plt.xlabel('x', fontsize = 12)
plt.ylabel('y',fontsize = 12)

# best 0 #upper right 1 #upper left 2 #lower left 3 #lower right #center left 6 #center right 7 #lower center 8 #upper center 9 #center 10
plt.legend(loc=0)
plt.savefig('q4.pdf')
fig.clear()

fig = plt.figure(num=None, dpi=80, figsize=(6,6), facecolor='w', edgecolor='k')
plt.plot(xList,reldiff,color='blue',lw=1,label='rd')
plt.xlabel('x', fontsize = 12)
plt.ylabel('y',fontsize = 12)
plt.legend(loc=0)
plt.savefig('q4rd.pdf')
fig.clear()

print("\n\n")


#Question 5
print("Question 5")

x = symbols('x')
expr = x**8 - 35*x**7 - 916*x**6 + 24182*x**5 + 170205*x**4 - 3514491*x**3 - 10590858*x**2 + 78685992*x - 64774080
exprfact = factor(expr)
print("f(x) = " + str(expr))
print("f(x) = " + str(exprfact))

roots = solveset(exprfact, x)
print("roots = " + str(roots))

print("\n\n")


#Question 6
print("Question 6")

x, y, z, = symbols('x y z')
m = Matrix(([5, 31, 12, 18], [51, -6, 14, 26], [-8, 39, -21, 22]))
sol = linsolve(m, (x, y, z))

print(m)
print("solution = " + str(sol))

