# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# python pandas groupby
# 그룹연산
# 성별 성적 평균, 학년별 성적 최고점수, 부서별 평균 연봉
# groupby 메서드 처리 가능

import pandas as pd
from pandas import Series, DataFrame

pd.read_csv("./data/kimchi_test.csv", encoding='cp949')
kimchi = pd.read_csv("C:/Users/kth96/Desktop/code/data/kimchi_test.csv", encoding='cp949')

#      판매년도  판매월    제품   판매처     수량       판매금액
# 0    2013    1  총각김치  대형마트  27916  233968900
# 1    2013    1  총각김치   백화점  11971   99796735
# 2    2013    1  총각김치   편의점   1603    2264200
# 3    2013    2  총각김치  대형마트  23057  194593960
# 4    2013    2  총각김치   백화점  11678  103106940
# ..    ...  ...   ...   ...    ...        ...
# 427  2016   11   무김치   백화점  16818  213580462
# 428  2016   11   무김치   편의점   1849    2718207
# 429  2016   12   무김치  대형마트  40806  351917006
# 430  2016   12   무김치   백화점  11877  139476205
# 431  2016   12   무김치   편의점   1890    2767080

# [432 rows x 6 columns]

kimchi.groupby?

kimchi.groupby(by=None, # 그룹핑 할 컬럼(기준)
    axis: 'Axis' = 0,   # 그룹핑 연산 방향
    level: 'Level | None' = None, # 멀티 인덱스 일 경우, 특정 레벨의 값을 그룹핑 컬럼으로 사용
    
# 예제) 제품별, 판매처 별(김치별) 수량 총 합
kimchi.groupby(by=['제품']).sum()
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001772C01A100>

'''
        판매년도  판매월       수량         판매금액
제품                                     
무김치   290088  936  2142764  20036782345
열무김치  290088  936  2147999  20295676819
총각김치  290088  936  2411653  23300688286
'''

kimchi.groupby(by=['제품','판매처']).sum()
kimchi.groupby(by=['제품','판매처'])['수량'].sum()
'''
제품    판매처 
무김치   대형마트    1550027
      백화점      510114
      편의점       82623
열무김치  대형마트    1491864
      백화점      567129
      편의점       89006
총각김치  대형마트    1649486
      백화점      658442
      편의점      103725
Name: 수량, dtype: int64
'''

kimchi.groupby(by='제품')['수량','판매금액'].sum()
kimchi.groupby(by='제품')[['수량','판매금액']].sum()  # 두개를 받기 때문에 두번 감싸야 한다!!

# 멀티인덱스
kimchi_2 = kimchi.groupby(by=['제품','판매처'])['수량'].sum()

# 예제) 제품별, 판매처별(김치별) 수량 총 합, 평균
kimchi.groupby(by=['제품','판매처'])['수량'].agg(['sum','mean']) 
'''
               sum          mean
제품   판매처                        
무김치  대형마트  1550027  32292.229167
     백화점    510114  10627.375000
     편의점     82623   1721.312500
열무김치 대형마트  1491864  31080.500000
     백화점    567129  11815.187500
     편의점     89006   1854.291667
총각김치 대형마트  1649486  34364.291667
     백화점    658442  13717.541667
     편의점    103725   2160.937500
'''

# agg : 여러 함수를 동시에 전달

# 예제) 제품별, 판매처별(김치별) 수량 판매금액 총합, 평균
kimchi.groupby(['제품','판매처'])[['수량','판매금액']].agg(['sum','mean'])
'''
                수량                       판매금액              
               sum          mean          sum          mean
제품   판매처                                                   
무김치  대형마트  1550027  32292.229167  14243851204  2.967469e+08
     백화점    510114  10627.375000   5675796839  1.182458e+08
     편의점     82623   1721.312500    117134302  2.440298e+06
열무김치 대형마트  1491864  31080.500000  14272706507  2.973481e+08
     백화점    567129  11815.187500   5897836502  1.228716e+08
     편의점     89006   1854.291667    125133810  2.606954e+06
총각김치 대형마트  1649486  34364.291667  16512153282  3.440032e+08
     백화점    658442  13717.541667   6639524485  1.383234e+08
     편의점    103725   2160.937500    149010519  3.104386e+06

'''

# 예제) 제품별, 판매처별(김치별) 수량은 총합, 판매금액 평균만 >> dict() 사용
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg({'수량':'sum','판매금액':'mean'})
'''
                수량          판매금액
제품   판매처                        
무김치  대형마트  1550027  2.967469e+08
     백화점    510114  1.182458e+08
     편의점     82623  2.440298e+06
열무김치 대형마트  1491864  2.973481e+08
     백화점    567129  1.228716e+08
     편의점     89006  2.606954e+06
총각김치 대형마트  1649486  3.440032e+08
     백화점    658442  1.383234e+08
     편의점    103725  3.104386e+06
'''

# 멀티 레벨을 갖는 경우의 groupby 연산

kimchi_2  
type(kimchi_2)
kimchi_2.groupby(level=0).sum() # 제품별 총합
kimchi_2.groupby(level='제품').sum()
kimchi_2.groupby(level=1).sum() # 판매처별 총합
