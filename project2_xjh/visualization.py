# -*- coding = utf-8 -*-
# @Time: 2023/11/29 15:12
# @Author: Jiahao Xu
# @File：visualization.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def visualization(factor_data, factor, factor2):
    """
    绘制因子的时序趋势图
    :param factor_data: 包含因子数据的DataFrame，其中一列为因子历史值
    :param factor: 因子名称,例 ‘sigma’
    :param factor2: 其他参与相关性分析的因子，例 ['a','b','c']
    """
    # sns.set(style='ticks', palette='deep')
    # sns.reset_defaults()
    plt.rcParams['font.size'] = 17
    plots = []
       
    # 因子 及 标的价格 趋势图
    factor_data['date'] = pd.to_datetime(factor_data['date'], format='%Y%m%d') 
    x = factor_data['date'] 
    y1 = factor_data[factor]  
    y2 = factor_data['close']
    
    fig1 = plt.figure(figsize=(30, 10))
    plt.plot(x,y1,'y-', label=factor)
    plt.ylabel(factor)
    #plt.tick_params('y',colors='y')
    plt.xticks(rotation=45)

    plt.twinx()
    plt.plot(x,y2,'r-',label='benchmark')
    plt.ylabel('benchmark_price')
    #plt.tick_params('y',colors='r')
    plt.xticks(rotation=45)
    plt.legend(loc='best')

    plt.title(factor + '_trend')
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(20))
    plt.grid(True)
    plt.tight_layout()
    plots.append(fig1)
    
   
    # 绘制频率直方图
    factor_values = factor_data[factor].values
    fig2 = plt.figure(figsize=(20, 6))
    sns.histplot(factor_values, kde=True)

    ## 在直方图上绘制中位数和均值的垂直线
    median = np.median(factor_values)
    mean = np.mean(factor_values)
    plt.axvline(median, color='r', linestyle='-', label='median')
    plt.axvline(mean, color='orange', linestyle='-', label='mean')
    plt.legend()
    
    plt.xlabel(factor)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)
    plt.tight_layout()
    plots.append(fig2)


    # 绘制箱线图
    df = factor_data[factor].describe().round(4).reset_index()
    fig3, ax = plt.subplots()
    ax.axis('off')  # Hide the axis
    table = ax.table(cellText=df.values, cellLoc='center', loc='center')
    table.auto_set_font_size(True)
    table.scale(1, 1.5)
    plots.append(fig3)
    
    fig4 = plt.figure(figsize=(20, 6)) 
    #factor_data[factor].plot.box(title=factor +"_Boxplot", whis=2.0)
    sns.boxplot(x=factor_values)
    #plt.ylabel('factor_values')
    plt.grid(True)
    plt.tight_layout() 
    plots.append(fig4)
  
  
    # 绘制因子的相互关联图(pairplot,pdf显示不出来)
    fig5 = plt.figure(figsize=(30,10), subplotpars=5)
    sns.pairplot(factor_data, y_vars= [factor], x_vars=factor2,kind='reg', diag_kind='auto').fig.set_size_inches(20,6)
    plt.tight_layout()
    plots.append(fig5)
  
  
    # 绘制因子的相互关联图(scatterplot)
    # factor_lists = factor_data[[factor] + factor2]
    # num_cols = len(factor_lists)
    # num_rows = num_cols
    # 
    # fig_sca, ax = plt.subplots(num_rows, num_cols, figsize=(12, 12))
    # for i in range(num_rows):
    #     for j in range(num_cols):
    #         # 绘制散点图
    #         sns.scatterplot(data=factor_lists, x=columns[j], y=columns[i], ax=ax[i, j])

    #plt.tight_layout()
    #plots.append(fig_sca)
    
    
    # 绘制相关性强度图
    correlations = factor_data[[factor]+ factor2].corr()
    fig6 = plt.figure(figsize=(10, 8))
    sns.heatmap(correlations, mask=correlations == 1, annot=True, cmap='coolwarm',center=0,fmt=".2f", linewidths=0.5, cbar_kws={"shrink": 0.8})
    plt.title('Correlation')
    plt.xticks(rotation=45)
    plt.tight_layout() 
    plots.append(fig6)
  
    return plots
