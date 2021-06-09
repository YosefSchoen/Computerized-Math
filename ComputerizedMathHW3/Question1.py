import math as m
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

from sympy import*
x, y = symbols('x y')
init_printing(use_unicode=True)
integ = Integral(1/sqrt(1-x**2), x)
pprint(integ)
print('\n\n')
pprint(integ.doit())
print('\n\n')

def f(x, y):
    slope = 1 / m.sqrt(1 - m.pow(x, 2))
    return slope


h = 1e-4
x_i = 0.
x_f = 1.
N = int((x_f - x_i)/h)
y_i = 0.

x = x_i
y = y_i

xList = [x]
yList = [y]

while x < x_f - h:
    y = y + (h * f(x, y))
    x = x + h

    yList.append(y)
    xList.append(x)

ys_aList = []

for i in xList:
    if i > 1:
        i = 1
    ya = m.asin(i)
    ys_aList.append(ya)

fig = plt.figure(num=None, dpi=80, figsize=(6, 6), facecolor='w', edgecolor='k')

plt.plot(xList, yList, color='blue', lw=2, label='num. sol.')
plt.plot(xList, ys_aList, color='red', lw=2, dashes=[10, 10], label='analy. sol.')

plt.margins(0, 0.1)

plt.xlabel(r'$x$', fontsize=12)
plt.ylabel(r'$y$', fontsize=12)

# best		0	#upper right	1	#upper left	2	#lower left	3	#lower right	4	#right		5
# center left	6	#center right	7	#lower center	8	#upper center	9	#center		10

plt.legend(loc=0, borderaxespad=0.4, fontsize=12, handlelength=2, ncol=1, fancybox=True, shadow=True,  frameon=True).set_title('leg. title',  prop={'size': 12})

plt.savefig('euler_method_plot1.pdf', bbox_inches='tight')
fig.clear()

# --------------------------------------------------------------------------------------------#


fig = plt.figure(num=None, dpi=80, figsize=(6, 6), facecolor='w', edgecolor='k')

rel_diff = [0]
for i in range(1, len(xList)):
    a = yList[i]
    b = ys_aList[i]
    if a == 0:
        continue
    rel_diff.append(abs((a-b)/a))

plt.semilogy(xList, rel_diff, color='blue', lw=4, label='rel.diff.')

plt.margins(0, 0.1)


plt.xlabel(r'$x$', fontsize=12)
plt.ylabel(r'$y$', fontsize=12)

# best		0	#upper right	1	#upper left	2	#lower left	3	#lower right	4	#right		5
# center left	6	#center right	7	#lower center	8	#upper center	9	#center		10

plt.legend(loc=0, borderaxespad=0.4, fontsize=12, handlelength=2, ncol=1, fancybox=True, shadow=True, frameon=True).set_title('leg. title',  prop={'size': 12})

plt.savefig('euler_method_rel_diff_plot.pdf', bbox_inches='tight')
fig.clear()

# --------------------------------------------------------------------------------------------#

x = x_i
y = y_i

xList = [x]
yList = [y]

while x < x_f - h:
    k1 = f(x, y)
    k2 = f(x+h/2., y+h/2.*k1)
    k3 = f(x+h/2., y+h/2.*k2)
    k4 = f(x+h/2., y+h*k3)
    y = y + h*(k1/6.+k2/3.+k3/3.+k4/6.)
    x = x + h

    yList.append(y)
    xList.append(x)


fig = plt.figure(num=None, dpi=80, figsize=(6, 6), facecolor='w', edgecolor='k')

plt.plot(xList, yList, color='blue', lw=2, label='num. sol. order. 4.')
plt.plot(xList, ys_aList, color='red', lw=2, dashes=[10, 10], label='analy. sol.')

plt.margins(0, 0.1)

plt.xlabel(r'$x$', fontsize=12)
plt.ylabel(r'$y$', fontsize=12)

# best		0	#upper right	1	#upper left	2	#lower left	3	#lower right	4	#right		5
# center left	6	#center right	7	#lower center	8	#upper center	9	#center		10

plt.legend(loc=0, borderaxespad=0.4, fontsize=12, handlelength=2, ncol=1, fancybox=True, shadow=True,  frameon=True).set_title('leg. title',  prop={'size': 12})

plt.savefig('euler_method_plotO4.pdf', bbox_inches='tight')
fig.clear()

rel_diff = [0]
for i in range(1, len(xList)):
    a = yList[i]
    b = ys_aList[i]
    if a == 0:
        continue
    rel_diff.append(abs((a-b)/a))

plt.semilogy(xList, rel_diff, color='blue', lw=4, label='rel.diff.')

plt.margins(0, 0.1)


plt.xlabel(r'$x$', fontsize=12)
plt.ylabel(r'$y$', fontsize=12)

# best		0	#upper right	1	#upper left	2	#lower left	3	#lower right	4	#right		5
# center left	6	#center right	7	#lower center	8	#upper center	9	#center		10

plt.legend(loc=0, borderaxespad=0.4, fontsize=12, handlelength=2, ncol=1, fancybox=True, shadow=True, frameon=True).set_title('leg. title',  prop={'size': 12})

plt.savefig('euler_method_rel_diff_O4_plot.pdf', bbox_inches='tight')
fig.clear()

