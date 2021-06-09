import matplotlib.pyplot as plt
import numpy as np



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def my_series(x):
    n_max = 100
    x1 = 1

    for n in range(1, n_max):
        x1 = x1 + pow(x, n)

    return x1


def plot():
    x = np.arange(0.1, 0.5, 0.01)
    y = [1./(1.-z) for z in x]
    y1 = [my_series(z) for z in x]

    fig = plt.figure(num=None, dpi=80, figsize=(6, 6), facecolor='w', edgecolor='k')
    plt.plot(x, y, color='blue', lw=4, label='series')
    plt.plot(x, y1, color='red', lw=2, label='my_series')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)

    # best 0 #upper right 1 #upper left 2 #lower left 3 #lower right #center left 6 #center right 7 #lower center 8 #upper center 9 #center 10
    plt.legend(loc=0)
    plt.savefig('my_plot_file_name.pdf')
    fig.clear()

    return


plot()
