
import numpy as np
import matplotlib.pyplot as plt
def gradient_descent():
    x = np.arange(-100,100,1)
    y = (x-10)**2
    plt.plot(x,y)
    plt.show()
    old = 0
    new = 9
    step = 0.01
    precision = 0.00001

    while abs(new -old) > precision:
        old = new
        new = new - step*derivative(new)
    print new
def derivative(x):
    return 2*(x-10)

if __name__ == '__main__':
    gradient_descent()