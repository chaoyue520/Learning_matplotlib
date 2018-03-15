#!/usr/bin/python
#-*- coding:utF-8 -*-

import matplotlib
import seaborn as sns
import numpy as np

"""
Anscombes quartet（安斯库姆四重奏）

1: 四组基本的统计特征一致的数据，但是由他们绘制出的图表则截然不同
2: 每一组数据都包含了11个点(x,y)
3: 构建该数据主要是为了说明分析数据前绘制图表的重要性，以及离群值对统计的影响之大


"""

# load data
anscombe_df = sns.load_dataset('anscombe')

import pandas as pd 
anscombe_df=pd.read_table('anscombe_quartet.txt',header=True,sep=',')
anscombe_df.head()


# 数据统计特性
anscombe_df.groupby('dataset').agg([np.mean, np.var])


# 数据相关性
a=[]
for i in list(set(anscombe_df.dataset)):
    b=anscombe_df[anscombe_df.dataset==i].corr()
    a.append(b.iloc[1,0])

print a


# 作图
# 研究在不同dataset下下，x与y的回归关系
sns.set(style="ticks")
sns.lmplot(x="x"
         , y="y"
         , col="dataset" # 同hue，将数据按照不同分组着色
         , hue="dataset" # 通过指定一个分组变量, 将原来的y~x关系划分成若干个分组
         , data=anscombe_df
         , col_wrap=2 # 控制每行子图数量，2表示一行摆放两个子图
         , ci=None # 回归线是否添加置信区间
         , palette="muted" # 调色板，可用参数包括Set2，muted等
         , size=4 # size控制子图高度
         , scatter_kws={"s": 50, "alpha": 1} # s表示散点图的大小，alpha表示散点图的颜色
         )

# 保存出表到本地
import matplotlib.pyplot as plt
plt.savefig('quartet.png', format='png')