# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 15:18:55 2021

@author: kth96
"""

# 22. scailing_스케일링

# 변수 스케일링(표준화)

# 설명변수의 서로 다른 범위를 동일한 범주 내 비교하기 위한 작업 
# - 거리 기반 모델
#   ex) knn, clustering, PCA, SVM, NN 모델 등에 필요
# - 각 설명변수의 중요도를 정확하게 비교하기 위해 요구됨 
# - 이상치에 덜 민감하게 조정

# 스케일링의 종류 

# 1) Standard Scailing
# - 평균을 0, 표준편차 1 로 맞추는 작업

# 2) MinMax Scailing
# - 최소값 0, 최대값 1 로 맞추는 작업

# 3) Robust Scailing
# - 중앙값 0, IQR 1 로 맞추는 작업

# scailing module 불러오기
from sklearn.preprocessing import StandardScaler as standard
from sklearn.preprocessing import MinMaxScaler as minmax

# iris data loading
from sklearn.datasets import load_iris

load_iris()['data']
iris_x = load_iris()['data']
load_iris()['target']
iris_y = load_iris()['target']

# 1) standard scailing (표준화 : (x-xbar) / sigma )
(iris_x - iris_x.mean(axis = 0))/ iris_x.std(axis=0)
# [ 6.86617933e-02, -1.31979479e-01,  7.62758269e-01,
#   # 7.90670654e-01]]

df1 = (iris_x - iris_x.mean(axis = 0))/ iris_x.std(axis=0)
df1.min() # -2.43394714190809
df1.max() # 3.0907752482994253

# 함수 사용
m_sc = standard()
m_sc.fit(iris_x) # fit : 데이터를 모델에 적합하게 해주는 함수
m_sc.transform(iris_x) # transform : 변환
 # [ 6.86617933e-02, -1.31979479e-01,  7.62758269e-01,
   # 7.90670654e-01]])

# 2) min max scailing (x-x.min())/(x.max()-x.min())

(iris_x - iris_x.min(0)) / (iris_x.max(0)-iris_x.min(0))
df2 = (iris_x - iris_x.min(0)) / (iris_x.max(0)-iris_x.min(0))
df2.max() # 1.0
df2.min() # 0.0

# 함수 사용
mm = minmax()
mm.fit(iris_x) # MinMaxScaler()
df2 = mm.transform(iris_x)

df2.max() #1.0
df2.min() #0.0



# train/test 로 분리되어진 데이터를 표준화
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y)

# 1) train_x, test_x 동일한 기준으로 스케일링 (good)
m_scl = minmax()
m_scl.fit(train_x)

train_m_scl = m_scl.transform(train_x)
test_m_scl = m_scl.transform(test_x)

train_m_scl.min(0) # array([0., 0., 0., 0.])
train_m_scl.max(0) # array([1., 1., 1., 1.])

test_m_scl.min(0)  # array([0.13888889, 0.08333333, 0.03508772, 0.04166667])  # 0이 아님
test_m_scl.max(0)  # array([0.94444444, 0.83333333, 1.03508772, 0.95833333])  # 1이 아님

# -------------------------------------------------------------

# 2) train_x, test_x 서로 다른 기준으로 스케일링 (bad)
m_sc2 = minmax()
m_sc3 = minmax()

m_sc2.fit(train_x) # train data도 fit 시킴
m_sc3.fit(test_x)  # test data도 fit시킨

train_m_sc2 = m_sc2.transform(train_x)
test_m_sc2 = m_sc3.transform(test_x)

train_m_sc2.min() # 0.0 
train_m_sc2.max() # 1.0

test_m_sc2.min() # 0.0
test_m_sc2.max() # 1.0

# scaling 시각화
# 1) figure, subplot 생성
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,3)

# 2) 원본 data의 산점도
import mglearn

ax[0].scatter(train_x[:,0], train_x[:,1], c=mglearn.cm2(0), label='train')
ax[0].scatter(test_x[:,0], test_x[:,1], c=mglearn.cm2(1), label='test')
ax[0].legend()
ax[0].set_title('raw data')


# 3) 올바른 스케일링 data의 산점도(train_x_sc1, test_x_sc1)
ax[1].scatter(train_sc1[:,0], train_sc1[:,1], c=mglearn.cm2(0), label='train')
ax[1].scatter(test_sc1[:,0], test_sc1[:,1], c=mglearn.cm2(1), label='test')
ax[1].legend()
ax[1].set_title('good scaing data')



# (4) 잘못된 스케일링 data의 산점도(train_x_sc2, test_x_sc2)
ax[2].scatter(train_sc_2[:,0], train_sc_2[:,1], c=mglearn.cm2(0), label='train')
ax[2].scatter(test_sc_2[:,0], test_sc_2[:,1], c=mglearn.cm2(1), label='test')
ax[2].legend()
ax[2].set_title('bad scaling data')
