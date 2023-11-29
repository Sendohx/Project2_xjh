# -*- coding = utf-8 -*-
# @Time: 2023/11/29 15:12
# @Author: Jiahao Xu
# @File：visualization.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import seaborn as sns


def plot_trend(factor_data, factor):
    """
    绘制因子的时序趋势图
    :param factor_data: 包含因子数据的DataFrame，其中一列为因子历史值
    :param factor: 因子名称
    """
    x = factor_data['date']  # 假设日期列的名称为'日期'
    y = factor_data[factor]  # 假设因子列的名称为'因子列名'

    plt.plot(x, y)
    plt.xlabel('date')
    plt.ylabel(factor)
    plt.title(factor + '_trend')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def plot_distribution(factor_data, factor):
    """
    绘制因子的连续数值离散化直方图和箱体图
    :param factor_data: 包含因子数据的DataFrame，其中一列为因子历史值
    :param factor: 因子名称
    """
    factor_values = factor_data[factor].values  # 假设因子列的名称为'因子列名'

    # 绘制直方图
    plt.figure(figsize=(10, 6))
    sns.histplot(factor_values, kde=True)
    plt.xlabel(factor)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

    # 绘制箱体图
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=factor_values)
    plt.xlabel(factor)
    plt.ylabel('factor_values')
    plt.title('Boxplot')
    plt.grid(True)
    plt.show()


def plot_correlation(factor_data):
    """
    绘制因子的相互关联图和相关性强度图
    :param factor_data: 包含因子数据的DataFrame, 例：指数因子dataframe：日期，因子1，因子2，...
    """
    correlations = factor_data.sort_values('date').corr()

    # 绘制因子的相互关联图
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlations, annot=True, cmap='coolwarm')
    plt.title('因子相互关联图')
    plt.show()

    # 绘制相关性强度图
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlations, annot=True, cmap='coolwarm', mask=correlations == 1)
    plt.title('因子相关性强度图')
    plt.show()
