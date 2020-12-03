import matplotlib.pyplot as plt
import numpy as np


def main():
    # 通过random模块的normal函数产生1000个正态分布的样本
    data = np.random.normal(10.0, 5.0, 1000)
    # 绘制直方图(直方的数量为10个)
    plt.hist(data, 10)
    plt.show()


if __name__ == '__main__':
    main()
