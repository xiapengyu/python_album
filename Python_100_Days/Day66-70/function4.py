import matplotlib.pyplot as plt
import numpy as np


def main():
    # 将样本数量减少为50个
    x_values = np.linspace(0, 2 * np.pi, 50)
    # 设置绘图为2行1列活跃区为1区(第一个图)
    plt.subplot(2, 1, 1)
    plt.plot(x_values, np.sin(x_values), 'o-b')
    # 设置绘图为2行1列活跃区为2区(第二个图)
    plt.subplot(2, 1, 2)
    plt.plot(x_values, np.sin(2 * x_values), '.-r')
    plt.show()


if __name__ == '__main__':
    main()