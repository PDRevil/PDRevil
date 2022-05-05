# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 13:23:28 2021

@author: kth96
"""

# pandas 정렬 sort()

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

pwd # present working directory 현 위치 폴더(디렉토리)

pd.read_csv('C:/Users/kth96/Desktop/code/data/emp.csv')
pd.read_csv('./data/emp.csv')

import os
os.getcwd() # get corrent working directory(현재 작업 폴더)

#  sort() 정렬
# 1. sort_index
# - Sreies, DataFrame 호출 가능
# - index, column 재배치

emp = pd.read_csv('./data/emp.csv')

#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000

emp.ename

emp['ename']

# 0    smith
# 1    allen
# 2     ford
# 3    grace
# 4    scott
# 5     king
# Name: ename, dtype: object
# 요청 결과를 Series로 변환

emp.idx = emp['empno']
emp.idx
emp.iloc[:,1:]

# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# 5    6
# Name: empno, dtype: int64

emp.set_index('ename')

#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# scott      5      30  4100
# king       6      20  4000

emp = emp.set_index('ename')

emp.sort_index(ascending=False) # 내림차순 정렬

#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# scott      5      30  4100
# king       6      20  4000
# grace      4      10  4200
# ford       3      20  4300
# allen      2      10  4500

emp.sort_index(ascending=True) # 기본값. 오름차순 정렬

#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# king       6      20  4000
# scott      5      30  4100
# smith      1      10  4000

emp.sort_index(axis=0)

#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# king       6      20  4000
# scott      5      30  4100
# smith      1      10  4000

emp.sort_index(axis=1) # 컬럼 순 정렬

#        deptno  empno   sal
# ename                     
# smith      10      1  4000
# allen      10      2  4500
# ford       20      3  4300
# grace      10      4  4200
# scott      30      5  4100
# king       20      6  4000



2. sort_values
# - Series, DataFrame 호출 가능 
# - 본문의 값(value) 으로 정렬 (Series, DataFrame 특정 칼럼 순서대로)

emp.sort_values(by='sal')

#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# king       6      20  4000
# scott      5      30  4100
# grace      4      10  4200
# ford       3      20  4300
# allen      2      10  4500

emp.sort_values(by='sal', ascending=False)

#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# ford       3      20  4300
# grace      4      10  4200
# scott      5      30  4100
# smith      1      10  4000
# king       6      20  4000

# 부서별, 연봉 수준

emp.sort_values(by=['deptno','sal'])

#        empno  deptno   sal
# ename                     
# smith      1      10  4000
# grace      4      10  4200
# allen      2      10  4500
# king       6      20  4000
# ford       3      20  4300
# scott      5      30  4100

emp.sort_values(by=['deptno','sal'], ascending=[True,False])

#        empno  deptno   sal
# ename                     
# allen      2      10  4500
# grace      4      10  4200
# smith      1      10  4000
# ford       3      20  4300
# king       6      20  4000
# scott      5      30  4100

