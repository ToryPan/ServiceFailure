import pandas as pd
import numpy as np
import random

# 预处理数据
data_big = pd.read_excel('data/dwxy_2w_correctPlatform_newUpdateFeb.xls',index_col='id')
# 文本长度
data_big_noshort = data_big[data_big['summary_len']>=20]
# 将包含有大部分标点符号的文本去除
data_big_noshort['chart_count'] = data_big_noshort['summary'].apply(lambda x: (x.count('。')+
                                                                   x.count('！')+x.count('？')+
                                                                   x.count('!')+x.count('?'))/len(x))
data_big_noshort_nochart = data_big_noshort[data_big_noshort['chart_count']<=0.4]

# 其他数据预处理使用excel进行
data_big = pd.read_excel('data/data.xls',index_col='id')

# 随机选择500条数据进行编码
index_label = random.choices([i for i in range(24183)],500)
index_res = list(set([i for i in range(24183)]) - set( index_label))
data_label = data_big .iloc(index_label)
data_res = data_big .iloc(index_res)
data_label.to_excel('data_label.xls')
data_res.to_excel('data_res.xls')

# 划分训练数据集
from sklearn.model_selection import train_test_split
data_label:pd.DataFrame = data_label.sample(frac=1.0)  
rows, cols = data_label.shape
split_index_1 = int(rows * 0.15)
data_test:pd.DataFrame = data_label.iloc[0: split_index_1, :]
data_train:pd.DataFrame = data_label.iloc[split_index_1: rows, :]

