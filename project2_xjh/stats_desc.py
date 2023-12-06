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
    :return df: 包含均值、标准差、中位数、峰度和偏度的dataframe
    """
    factor_values = factor_data[factor].values

    stats = {}
    stats['mean'] = np.round(np.mean(factor_values), decimals=4)  #保留四位小数
    stats['std'] = np.round(np.std(factor_values),decimals=4)
    stats['median'] = np.round(np.median(factor_values),decimals=4)
    stats['kurtosis'] = np.round(kurtosis(factor_values),decimals=4)
    stats['skewness'] = np.round(skew(factor_values),decimals=4)
    
    df = pd.DataFrame.from_dict(stats, orient='index', columns=[factor])
    df.index.name = 'Stats'
    df.reset_index(inplace=True)

    return df
