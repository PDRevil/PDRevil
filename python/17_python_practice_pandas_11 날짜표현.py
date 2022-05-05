# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:22:41 2021

@author: kth96
"""
# 17. 날짜표현
# 월별, 일별, 요일별 집계
# 현재 날짜 - 입사일자 = 근무일자

# 현재 날짜

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from datetime import datetime
datetime.now()

d1 = datetime.now()
type(d1)

d1.year
d1.month
d1.day

# 2. 날짜 파싱
d2='2022/01/01'
d2.year
# AttributeError: 'str' object has no attribute 'year'

# datetime.strptime(date_string, format)
# 벡터 연산이 안됨

datetime.strptime(d2, '%Y/%m/%d')
# datetime.datetime(2022, 1, 1, 0, 0)

datetime.strptime('09/12/25', '%m/%d/%y') # 2025년 09월 12일 해석
# datetime.datetime(2025, 9, 12, 0, 0)

# Series 벡터 연산 불가
s1 = Series(['2022/01/01','2022/01/02','2022/01/03'])
datetime.strptime(s1, '%Y/%m/%d')
# TypeError: strptime() argument 1 must be str, not Series
s1.map(lambda x: datetime.strptime(x, '%Y/%m/%d'))
'''
0   2022-01-01
1   2022-01-02
2   2022-01-03
dtype: datetime64[ns]
'''

# 2) pd.to_datetime
# 벡터 연산가능
s1
type(s1)
pd.to_datetime(s1, infer_datetime_format=True)
s2 = pd.to_datetime(s1, infer_datetime_format=True)
type(s1)
'''
0   2022-01-01
1   2022-01-02
2   2022-01-03
dtype: datetime64[ns]
'''
pd.to_datetime(s2, format="%Y/%m/%d")

s3 = pd.DataFrame({'date' : ['01-05-21','01-06-21','01-07-21',]})
s3.dtypes
s3

# 3) 날짜 포맷 변경 datetime.strftime(string format time)
# 요일 추출(날짜에서 요일을 return 하도록 날짜 출력 형식 변경)
# (연/월/일) --> (월/일/연) 순서로 변경
# (주의) 날짜 포맷 변경 한 후 return 데이터 타입은 무조건 문자

d1 = datetime.now()
d1
datetime.strftime(d1, '%a') # 요일 리턴(축약형) 'Wed'
datetime.strftime(d1, '%A') # 요일 리턴(완전체) 'Wednesday'
datetime.strftime(d1,'%m-%d,%Y') # '12-29,2021'


datetime.strftime(d1, '%Y') # 연도 리턴 (완전체) '2021'
datetime.strftime(d1, '%y') # 연도 리턴 (축약형) '21'

s2
datetime.strftime(s2, '%Y')
# TypeError: descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'Series' object
s2.map(lambda x: datetime.strftime(x, '%Y'))
'''
0    2022
1    2022
2    2022
dtype: object
'''

## 4) 날짜 연산***
d1        # 현재 날짜
d1+100    # 동작 안함

# 오늘 날짜로부터 100일 뒤 날짜 리턴 불가(타입 에러) 
# TypeError: unsupported operand type(s) for +: 'datetime.datetime' and 'int'

# 1) offset

from pandas.tseries.offsets import Day, Hour, Second
d1 + Day(100)
# Timestamp('2022-04-08 11:43:02.701570')

# 2) timedelta (날짜와의 차이)

from datetime import timedelta
d1 + timedelta(100)
# datetime.datetime(2022, 4, 8, 11, 43, 2, 701570)
# 오늘 일자부터 100일 뒤 리턴해줌

# 3) (실무용) DateOffset ***(추천)
d1 + pd.DateOffset(months = 4)
# Timestamp('2022-04-29 11:43:02.701570')

# 5. 날짜 - 날짜
d1 - datetime.strptime(d2, '%Y/%m/%d')
# datetime.timedelta(days=-3, seconds=42182, microseconds=701570)
d3 = d1 - datetime.strptime(d2, '%Y/%m/%d') 

d3.days
d3.seconds

# [연습문제]
# 요일별 통화건 수 총합

deli = pd.read_csv("./data/delivery.csv", encoding='cp949')
deli.dtypes
'''
일자       int64
시간대      int64
업종      object
시도      object
시군구     object
읍면동     object
통화건수     int64
dtype: object
'''
deli.head()
deli.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 119189 entries, 0 to 119188
Data columns (total 7 columns):
 #   Column  Non-Null Count   Dtype 
---  ------  --------------   ----- 
 0   일자      119189 non-null  int64 
 1   시간대     119189 non-null  int64 
 2   업종      119189 non-null  object
 3   시도      119189 non-null  object
 4   시군구     119189 non-null  object
 5   읍면동     119189 non-null  object
 6   통화건수    119189 non-null  int64 
dtypes: int64(3), object(4)
memory usage: 6.4+ MB
'''
deli.describe()
'''
                 일자            시간대           통화건수
count  1.191890e+05  119189.000000  119189.000000
mean   2.018021e+07      15.576362       9.916486
std    8.234111e+00       5.321848      13.904536
min    2.018020e+07       0.000000       5.000000
25%    2.018021e+07      13.000000       5.000000
50%    2.018021e+07      17.000000       5.000000
75%    2.018022e+07      19.000000       7.000000
max    2.018023e+07      23.000000     229.000000

'''
deli.boxplot()

# 날짜 파싱

deli
deli['일자']
type(deli['일자'])
pd.to_datetime(deli['일자'])
pd.to_datetime(deli['일자'], format = '%Y%m%d')
deli['일자'] = pd.to_datetime(deli['일자'], format = '%Y%m%d')

# 요일 리턴
datetime.strftime(deli['일자'],'%A')
# TypeError: descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'Series' object
deli['일자'].map(lambda x:datetime.strftime(x,'%A'))
deli['요일'] = deli['일자'].map(lambda x:datetime.strftime(x,'%A'))
'''
0          Thursday
1          Thursday
2          Thursday
3          Thursday
4          Thursday
   
119184    Wednesday
119185    Wednesday
119186    Wednesday
119187    Wednesday
119188    Wednesday
'''

# 요일별로 그룹화
deli.groupby(deli['요일'])['통화건수'].sum()
'''
요일
Friday       162037
Monday       142157
Saturday     196429
Sunday       196096
Thursday     150316
Tuesday      158544
Wednesday    176357
Name: 통화건수, dtype: int64
'''
total = deli.groupby(deli['요일'])['통화건수'].sum()
total[['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']]


# 일자별 통화건수
deli.groupby('일자')['통화건수'].sum()
