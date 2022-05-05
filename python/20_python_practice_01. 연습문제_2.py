# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:13:10 2022

@author: kth96
"""

run my_modules

# card.csv 파일 읽기

import pandas as pd

pd.read_csv('./data/card.csv', encoding = 'cp949')
card = pd.read_csv('./data/card.csv', encoding = 'cp949')
# NUM을 인덱스로 사용

card = card.set_index('NUM')

# 문제) 일자별 총 지출 금액을 구해서, 마지막 컬럼에 추가
# (천 단위 구분 기호 제거 후 숫자 컬럼 변경하시오)

# 행/세, 열/가 (행은 세로방향, 열은 가로방향)
card.sum()
card.sum(axis=0) # default : axis=0 세로 방향
card.sum(axis=1)
# axis=1 : 서로 다른 열끼리(가로방향) sum() 합해라
# 문자 타입이라 문자별 결합

'hi'+'PDRevil'

# ','문자 제거 >>> 숫자 변경
# 천단위 구분기호 제거 >> 숫자 컬럼 변경

'19,400'.replace(',','') # '19400'
int('19,400'.replace(',',''))
'19,400'.replace(',','').astype('int')
# 문자열에 사용 불가(array, Series, DataFrame 사용 가능)

f1 = lambda x : int(x.replace(',',''))
card = card.applymap(f1)
card

# applymap : 2차원 데이터셋(DataFrame)에 함수 적용 위해 사용

# int('19,400'.replace(',',''))
# 이 행위(형변환 함수)를 전체에 적용할 때 사용

# 일자별 총합 (새로운 열 생성)
card['총합'] = card.sum(axis=1)
card


# [참고 -  위 함수를 특정 컬럼에 대해 적용]

card_new = pd.read_csv('./data/card.csv', encoding = 'cp949')
card_new = card_new.set_index('NUM')

# -식료품 컬럼에만 적용
f2 = lambda x : int(x.replace(',',''))
card_new['식료품'].applymap(f2)
# 1차원 데이터 셋(Series) 에 적용 불가
card_new['식료품'] = card_new['식료품'].map(f2)

card_new['의복'] = card_new['의복'].str.replace(',','')
# 여전히 dtype은 object(객체)

card_new['의복'] = card_new['의복'].str.replace(',','').astype('int')
# 일괄적으로 적용하려면 astype() 사용할 것

card_new['책값'].replace(',','')
# 값 치환 메서드(특정 값과 정확히 일치하는 것을 변경하거나 삭제)
# ','와 완전히 일치하는 값을 변경 또는 삭제

card_new['책값'].replace('28,000','')

# 2) 일자별로 각 품목별 지출 비율을 출력하세요(%로 출력하세요)
card = pd.read_csv('./data/card.csv', encoding = 'cp949')
card = card.set_index('NUM')

f1 = lambda x : int(x.replace(',',''))
card = card.applymap(f1)
card

# 첫번째 행에 대해 확인
card.iloc[0,:]
card.iloc[0,:].sum() # 첫째 날 지출 총 합
(card.iloc[0,:] / card.iloc[0,:].sum())*100


# 식료품         8.629893
# 의복         63.612100
# 외식비         3.825623
# 책값         12.900356
# 온라인소액결제     2.491103
# 의료비         8.540925
# Name: 1, dtype: float64

# apply 메서드 이용, 각 일자별로 적용 (썩은물(?) 전용)
f2 = lambda x : (x / x.sum())*100
card.apply(f2, axis=1) # 가로 방향

# 결과 해석
# 의복비가 지출이 심함 (일자별 지출 중 의복비 비중이 50% 이상)
# insight (통찰) 의복비 비중을 줄일 필요성이 있음(주관적 의견)

# 형(데이터 타입) 변환 : 함수, astype 메서드
# 적용함수 : map 함수, map 메서드, apply 메서드, applymap 메서드
# 치환함수 : 문자열 메서드, 벡터화 내장된 문자열 메서드, 값 치환
# 색인
# 컬럼 추가, 컬럼 내용 변경

# 문제 각 구매 마다 포인트 확인하고, POINT 컬럼 생성
# POINT 는 주문금액 50000 마만 1%, 5만 이상 10만 미만 2%, 10만 이상 3%
# 문제 풀이 포인트 : 조건에 따른 치환 혹은 연산

df1 = pd.read_csv('./data/ex_test1.csv', encoding = 'cp949')

if df1("주문금액") < 50000:
    df1['주문금액']*0.01

#if 문은 여러 개의 T/F (boolean) 연산 불가

result = []

for i in df1['주문금액']:
    if i < 50000:
        result.append(i * 0.01)
    elif i < 100000:
        result.append(i * 0.02)
    else:
        result.append(i * 0.03)
        
# print(result)
print(np.round(result,2))

df1['point'] = np.round(result,2)
df1['point']
df1

# sol2) np.where(벡터 연산 가능한 조건 연산 함수)
# sql에서 copy 함
# sql : select * from db_name where 조건절
# np.where(조건, 참 리턴, 거짓 리턴)

# np.where(df1['주문금액']< 50000, df1['주문금액']*0.01, df1['주문금액']*0.02)
np.where(df1['주문금액']<50000,           # 첫번째 조건
         df1['주문금액']*0.01,            # 첫번째 조건이 참이면 연산
         np.where(df1['주문금액']<100000, # 두번째 조건
                  df1['주문금액']*0.02,   # 두번째 조건이 참이면 연산
                  df1['주문금액']*0.03))  # 두번째 조건이 거짓이면 연산

# 첫번째 조건이 거짓이면, 새로운 조건 추가

df1['point'] = np.where(df1['주문금액']<50000,           # 첫번째 조건
                         df1['주문금액']*0.01,            # 첫번째 조건이 참이면 연산
                         np.where(df1['주문금액']<100000, # 두번째 조건
                                  df1['주문금액']*0.02,   # 두번째 조건이 참이면 연산
                                  df1['주문금액']*0.03))
# 2. 회원번호별 총 주문금액과 총 포인트 금액 확인
df1.groupby('회원번호')[['주문금액','point']].sum()

# [연습문제 - Y 값을 서로 다른 숫자로 변경]
# 출제의도 : 조건에 따른 치환

df2 = DataFrame({'Y':['a','a','b','b','c','a','a','b'],
                 'x1' : [1,2,4,4,6,3,5,4],
                 'x2' : [10,30,43,34,43,43,94,32]})

df2

# 하나 씩 사용자가 치환(정수 인덱스)
df2['Y'].replace({'a':0, 'b':1, 'c':2})

# 자동 변환 함수
from sklearn.preprocessing import LabelEncoder

m_lb=LabelEncoder()
m_lb.fit_transform(df2['Y'])
# array([0, 0, 1, 1, 2, 0, 0, 1])

# [연습문제 - 조건에 따른 값의 수정]
# df2에서 x1이 5 이상일 경우, x1 평균으로 수정(최빈값, 중앙값, 최소값)

df2['x1'][df2['x1']>=5]
# 4    6
# 6    5
# Name: x1, dtype: int64

df2.loc[df2['x1']>=5, 'x1'] # 추천

df2
m1 = df2['x1'].mean()
m2 = df2['x1'].median()
m3 = df2['x1'].mode() # 최빈값
m4 = df2['x1'].mode()[0] # 하나의 상수로 리턴
m5 = df2['x1'].min() # 최소값
m6 = df2['x1'].max()

import statistics as stat
stat.mode(df2['x1']) # 4 : 하나의 상수로 리턴해줌

df2
df2.loc[df2['x1']>=5, 'x1']
df2.loc[df2['x1']>=5, 'x1'] = m3 # 최빈값으로 치환하겠다
# NA로 수정됨

df2.loc[df2['x1']>=5, 'x1'] = m4
df2
