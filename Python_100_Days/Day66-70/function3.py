import matplotlib.pyplot as plt
import numpy as np


def main():
    x_values = np.linspace(0, 2 * np.pi, 1000)
    plt.plot(x_values, np.sin(x_values), '--b')
    plt.plot(x_values, np.sin(2 * x_values), '--r')
    plt.show()


if __name__ == '__main__':
    main()