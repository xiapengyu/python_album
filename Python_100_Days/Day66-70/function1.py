from matplotlib import pyplot


def main():
    # 保存x轴数据的列表
    x_values = [x for x in range(1, 11)]
    # 保存y轴数据的列表
    y_values = [x ** 2 for x in range(1, 11)]
    # 设置图表的标题以及x和y轴的说明
    pyplot.title('Square Numbers')
    pyplot.xlabel('Value', fontsize=18)
    pyplot.ylabel('Square', fontsize=18)
    # 设置刻度标记的文字大小
    pyplot.tick_params(axis='both', labelsize=16)
    # 绘制折线图
    pyplot.plot(x_values, y_values, 'xr')
    pyplot.show()


if __name__ == '__main__':
    main()
