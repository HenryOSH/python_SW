# da_4_1_matplotlib.py

import matplotlib.pyplot as plt
import numpy as np

def plot_1():
    print(plt.style.available)


    x = np.arange(10)
    y = x + np.random.randint(-10, 10, len(x))

    with plt.style.context('bmh'):
        plt.subplot(1, 2, 1)
        plt.plot(x, y)


        plt.subplot(1, 2, 2)
        plt.bar(x, y)




    plt.show()


# 퀴즈
# 그래프 스타일 전체를 5행 6열 형태로 표시하세요.
def plot_2():
    x = np.arange(10)
    y = x + np.random.randint(-10, 10, len(x))
    i=1
    for style in plt.style.available:
        with plt.style.context(style):
            plt.subplot(5, 6, i)
            plt.plot(x, y)
            i+=1


    plt.show()


# plot_1()
# plot_2()

def plot_3():
    x = np.arange(100)

    plt.scatter(x,x,c=x)
    plt.show()

def plot_4():
    jet = plt.get_cmap('jet')

    print(jet(0))
    print(jet(255))

plot_4()
