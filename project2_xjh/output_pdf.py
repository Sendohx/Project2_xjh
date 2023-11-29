# -*- coding = utf-8 -*-
# @Time: 2023/11/29 16:24
# @Author: Jiahao Xu
# @File：output_pdf.py
# @Software: PyCharm

import io
import pdfkit
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from visualization import plot_trend, plot_distribution, plot_correlation
from stats_desc import factor_stats


def generate_report(factor_data, factor):
    """
    生成因子检测工具的pdf
    :param factor_data: 包含因子数据的DataFrame，其中一列为因子历史值
    :param factor: 因子名称
    """
    pdf_output = io.BytesIO()

    with PdfPages(pdf_output) as pdf:
        # 描述统计结果
        stats = factor_stats(factor_data, factor)
        pdf.savefig(figure=plt.figure())
        for key, value in stats.items():
            plt.text(0.1, 0.9, f"{key}: {value}", transform=plt.gca().transAxes, fontsize=12, va='top')
            pdf.savefig()

        # 可视化结果
        plot_trend(factor_data, factor)
        pdf.savefig()
        plt.close()

        plot_distribution(factor_data, factor)
        pdf.savefig()
        plt.close()

        plot_correlation(factor_data)
        pdf.savefig()
        plt.close()

        pdf_output.seek(0)
        pdfkit.from_file(pdf_output, 'C:/Users/Sendoh/PycharmProjects/project2_xjh' + f'{factor}_report.pdf')

    if __name__ == '__main__':
        # 样例
        dict = {}
        df = pd.DataFrame(dict)
        factor = 'xxx'

        generate_report(df, factor)