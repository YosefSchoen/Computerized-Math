import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------------------------------#
#
# The following line of code imports the file "data.dat" as 2D array of floats,
#
# i.e. data = [ [x0,x1,....,xN] , [y0,y1,...., yN] ]
#
# data[0] is a 1D array with all the x values and data[1] is a 1D array with the y values of the function
#
# -----------------------------------------------------------------------------------------------------------------------#
def numerical_derivative(data, order):
    x = data[0]
    y = data[1]
    N = len(x)
    dy = []

    if order == 1:
        for n in range(0, N-1):
            h = x[n+1]-x[n]
            dy = dy + [(-y[n] + y[n+1])/h]

    if order == 2:
        for n in range(0, N-2):
            h = x[n+1]-x[n]
            dy = dy + [((-3./2.)*y[n] + 2.*y[n+1] + (-1./2.)*y[n+2])/h]

    if order == 3:
        for n in range(0, N-3):
            h = x[n+1]-x[n]
            dy = dy + [((-11./6.)*y[n] + 3.*y[n+1] + (-3./2.)*y[n+2] + (1./3.)*y[n+3])/h]

    if order == 4:
        for n in range(0, N-4):
            h = x[n+1]-x[n]
            dy = dy + [((-25./12.)*y[n] + 4. * y[n+1] - 3. * y[n+2] + (4./3.)*y[n+3] + (-1./4.)*y[n+4])/h]

    if order == 5:
        for n in range(0, N-5):
            h = x[n+1]-x[n]
            dy = dy + [((-137./60.)*y[n] + 5.*y[n+1] - 5.*y[n+2] + (10./3.)*y[n+3]-5./4.*y[n+4] + 1./5.*y[n+5])/h]

    if order == 6:
        for n in range(0, N-6):
            h = x[n+1]-x[n]
            dy = dy + [((-49./20.)*y[n] + 6.*y[n+1] - 15./2.*y[n+2] + 20./3.*y[n+3] - 15./4.*y[n+4] + 6./5.*y[n+5]-1./6.*y[n+6])/h]

    return dy


def plot():
    x = data[0]
    y = data[1]
    fig = plt.figure(num=None, dpi=80, figsize=(6,6), facecolor='w', edgecolor='k')
    plt.plot(x,y,color='blue',lw=1,label='choose a label for the legend')
    plt.xlabel('x', fontsize = 12)
    plt.ylabel('y',fontsize = 12)

    # best 0 #upper right 1 #upper left 2 #lower left 3 #lower right #center left 6 #center right 7 #lower center 8 #upper center 9 #center 10
    plt.legend(loc=0)
    plt.savefig('my_plot.pdf')
    fig.clear()
    return


data = np.array(np.loadtxt("HW2_data.dat"))
N_dy_O2 = numerical_derivative(data, 2)

x0 = [0, 5, 10]
N = len(data[0])
N1 = len(N_dy_O2)

for i in range(0, N1):
    for j in x0:
        if data[0][i] == j:
            print(N_dy_O2[i])
#plot()

