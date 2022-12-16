# da_2_4_matplotlib_basic.py

import matplotlib.pyplot as plt
import numpy as np

# plt.plot([2, 3, 4])
# plt.plot([2, 3, 4], 'rx')

def plot_1():
    x = range(2,7)
    y= range(5)



    plt.plot(x, y)
    plt.plot(x, y,'k>')
    plt.show()

# 퀴즈
# y = x^2  그래프를 그려보세요.
def plot_2():


    x = np.arange(-10,11,0.5)
    plt.plot(x, x**2,'ro')
    plt.show()

# plot_1()

# plot_2()


# 데스모스에서 그렸던 로그 그래프 4개를 그려주세요
def plot_4():
    x = np.arange(0.000001,10,0.001)
    plt.plot(x, np.log(x))
    plt.plot(x, -np.log(x))
    plt.plot(-x, np.log(x))
    plt.plot(-x, -np.log(x))

    plt.show()


# plot_4()

def plot_5():
    x = np.arange(0.000001, 10, 0.001)

    plt.subplot(2, 2, 4)
    plt.plot(x, np.log(x), 'r')
    plt.subplot(2, 2, 2)
    plt.plot(x, -np.log(x), 'g')

    plt.figure(figsize=[5,10])
    plt.subplot(2, 2, 3)
    plt.plot(-x, np.log(x), 'b')
    plt.subplot(2, 2, 1)
    plt.plot(-x, -np.log(x), 'y')

    plt.show()



# plot_5()



# 퀴즈 나머지 데이터를 고 사이에다 낑겨 넣으세요.


def plot_6():
    men = [34, 21, 43, 50 ,47]
    women = [43, 53, 28, 39, 41]


    x = np.arange(len(men))*2

    plt.bar(x, men, width=0.3)
    plt.bar(x+0.5, women, width=0.3)
    plt.show()

plot_6()

