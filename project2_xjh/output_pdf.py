# -*- coding = utf-8 -*-
# @Time: 2023/12/5 16:24
# @Author: Jiahao Xu
# @File：output_pdf.py
# @Software: PyCharm

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from visualization import visualization
from stats_desc import factor_stats


def save_plots_to_pdf(dataframe, plots, output_path):
    """
    将描述性统计和可视化结果输出为pdf
    :param dataframe: 描述性统计结果
    :param plots: 可视化结果列表
    :param output_path: pdf输出路径
    """
    with PdfPages(output_path) as pdf:
        fig, ax = plt.subplots()
        ax.axis('off')  # Hide the axis
        table = ax.table(cellText=dataframe.values, colLabels=dataframe.columns, cellLoc='center', loc='center')
        table.auto_set_font_size(True)
        table.scale(1, 1.5)
        pdf.savefig(fig)
        
        for plot in plots:
            pdf.savefig(plot, bbox_inches = 'tight',pad_inches = 0.5, dpi=3000)

if __name__ == '__main__':
    # 样例
    factor_data = []
    output_path = "C:/Users/Sendoh/PycharmProjects/" + factor + ".pdf"
    df = factor_stats(factor_data, factor)
    plots = visualization(factor_data, factor, factor2)
    save_plots_to_pdf(df, plots, output_path)
