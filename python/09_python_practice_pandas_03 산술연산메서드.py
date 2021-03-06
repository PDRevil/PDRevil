# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:06:58 2021

@author: kth96
"""

import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(1,17).reshape(4,4))

dir(df1)

df1
df1.sum(axis=0)
df1.sum(axis=1)

df1.iloc[:,0].sum()
df1.iloc[:,0].mean()

df1.iloc[0,0] = np.nan
df1.iloc[:,0].mean()
# skipna = True (default) 자동으로 NaN 무시하고 연산

# 평균값(최대 또는 최소) 대치
df1.iloc[:,0].mean()
[df1.iloc[:,0].isnull()]  # 조건
# [0     True
#  1    False
#  2    False
#  3    False
#  Name: 0, dtype: bool]
df1.iloc[:,0][df1.iloc[:,0].isnull()] = df1.iloc[:,0].mean()

df1[df1.isnull()]
df1[df1.notnull()] # 데이터프레임 전체에서 NaN값 확인

df1.iloc[:,0].var() # 10.666666666666666 >> 분산
df1.iloc[:,0].std() # 3.265986323710904 >> 표준편차
df1.iloc[:,0].min() # 5.0 >> 최소값
df1.iloc[:,0].max() # 13.0
df1.iloc[:,0].median() # 9.0 >> 중앙값


(df1.iloc[:,0] >= 10).sum() # 1 >> 조건에 만족하는개수 확인
