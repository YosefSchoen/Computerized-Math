import numpy as np
import matplotlib.pyplot as plt


def numerical_derivative(data, order):
    x = data[0]
    y = data[1]
    N = len(x)

    print(x)
    print(y)

    print(x[:-1])

    dy	= []

    if(order==1):
        coeffs		= [-1,1]
        for n in range(0,N-1):
            h		= x[n+1]-x[n]
            dy		= dy + [ ( coeffs[0]*y[n] + coeffs[1]*y[n+1] )/h ]

    if(order==2):
        coeffs	= [-3./2.,2.,-1./2.]
        for n in range(0,N-2):
            h		= x[n+1]-x[n]
            dy		= dy + [ ( coeffs[0]*y[n] + coeffs[1]*y[n+1] + coeffs[2]*y[n+2])/h ]

    if(order==3):
        coeffs		= [-11./6.,3.,-3./2.,1./3.]
        for n in range(0,N-3):
            h		= x[n+1]-x[n]
            dy		= dy + [ ( coeffs[0]*y[n] + coeffs[1]*y[n+1] + coeffs[2]*y[n+2]+ coeffs[3]*y[n+3])/h ]

    if(order==4):
        coeffs		= [-25./12.,4.,-3., 4./3., -1./4.]
        for n in range(0,N-4):
            h		= x[n+1]-x[n]
            dy		= dy + [ ( coeffs[0]*y[n] + coeffs[1]*y[n+1] + coeffs[2]*y[n+2]+ coeffs[3]*y[n+3]+ coeffs[4]*y[n+4])/h ]

    if(order==5):
        coeffs		= [-137./60.,5.,-5., 10./3., -5./4., 1./5.]
        for n in range(0,N-5):
            h		= x[n+1]-x[n]
            dy		= dy + [ ( coeffs[0]*y[n] + coeffs[1]*y[n+1] + coeffs[2]*y[n+2]+ coeffs[3]*y[n+3]+ coeffs[4]*y[n+4] + coeffs[5]*y[n+5])/h ]

    if(order==6):
        coeffs		= [-49./20.,6.,-15./2.,20./3., -15./4.,6./5.,-1./6.]
        for n in range(0,N-6):
            h		= x[n+1]-x[n]
            dy		= dy + [ ( coeffs[0]*y[n] + coeffs[1]*y[n+1] + coeffs[2]*y[n+2]+ coeffs[3]*y[n+3]+ coeffs[4]*y[n+4]+ coeffs[5]*y[n+5]+ coeffs[6]*y[n+6])/h ]

    return dy


data = np.array(np.loadtxt("HW3_data.dat.txt"))

xs = data[0]
ys = data[1]

fig = plt.figure()

x_pow_2 = [5000.*pow(x1, 2.) for x1 in xs]
x_pow_3 = [500.*pow(x1, 2.) for x1 in xs]
x_pow_4 = [50.*pow(x1, 4.) for x1 in xs]
x_pow_5 = [5.*pow(x1, 5.) for x1 in xs]
x_pow_6 = [pow(x1, 6.) for x1 in xs]


plt.loglog(xs, ys, color='red', label='data')
plt.loglog(xs, x_pow_2, color='yellow', lw=1, label='x^2')
plt.loglog(xs, x_pow_3, color='green', lw=1, label='x^3')
plt.loglog(xs, x_pow_4, color='cyan', label='x^4')
plt.loglog(xs, x_pow_5, color='blue', label='x^5')
plt.loglog(xs, x_pow_6, color='magenta', label='x^6')
plt.legend()

plt.savefig('Q2_a.pdf')
fig.clear()


newData = numerical_derivative(data, 6)
xsd = data[0]
ysd = data[1]

xd_pow_2 = [5000.*pow(x1, 2.) for x1 in xsd]
xd_pow_3 = [500.*pow(x1, 2.) for x1 in xsd]
xd_pow_4 = [50.*pow(x1, 4.) for x1 in xsd]
xd_pow_5 = [5.*pow(x1, 5.) for x1 in xsd]
xd_pow_6 = [pow(x1, 6.) for x1 in xsd]

plt.loglog(xsd, ysd, color='red', label='data')
plt.loglog(xsd, xd_pow_2, color='yellow', lw=1, label='x^2')
plt.loglog(xsd, xd_pow_3, color='green', lw=1, label='x^3')
plt.loglog(xsd, xd_pow_4, color='cyan', label='x^4')
plt.loglog(xsd, xd_pow_5, color='blue', label='x^5')
plt.loglog(xsd, xd_pow_6, color='magenta', label='x^6')
plt.legend()

plt.savefig('Q2_c.pdf')
fig.clear()
