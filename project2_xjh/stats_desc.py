# -*- coding = utf-8 -*-
# @Time: 2023/11/29 14:50
# @Author: Jiahao Xu
# @File：stats_desc.py
# @Software: PyCharm

import numpy as np
from scipy.stats import kurtosis, skew


def factor_stats(factor_data, factor):
    """
    计算因子历史值的描述统计信息
    :param factor_data: 因子历史值的dataframe
    :param factor: 因子名称
    :return dict: 包含均值、标准差、中位数、峰度和偏度的字典
    """
    factor_values = factor_data[factor].values

    stats = {}
    stats['mean'] = np.mean(factor_values)
    stats['std'] = np.std(factor_values)
    stats['median'] = np.median(factor_values)
    stats['kurtosis'] = kurtosis(factor_values)
    stats['skewness'] = skew(factor_values)

    return stats
