# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:14:08 2021

@author: kth96
"""
# 1월10일 시험에 절반 출제

# 판다스 연습문제

df1 = pd.read_csv("./data/cancer_test.csv")
df1.columns
df1.dtypes

df1.head()
df1.info()
df1.describe()

# 1. radius_mean, texture_mean, texture_se, smoothness_se
# NA인 행을 제거한 후 총 행의 수 리턴

df1['radius_mean'].isnull().sum()    # NA --> 4
df1['texture_mean'].isnull().sum()   # NA --> 4
df1['texture_se'].isnull().sum()     # NA --> 4
df1['smoothness_se'].isnull().sum()  # NA --> 4

vbool = df1['radius_mean'].isnull() & df1['texture_mean'].isnull() & df1['texture_se'].isnull() & df1['smoothness_se'].isnull()
vbool.sum() # 컬럼 4개가 모두 NA인 행의 수

df1
df1.loc[vbool,:] # 컬럼 4개가 모두 NA인 행 확인
'''
           id diagnosis  ...  symmetry_worst  fractal_dimension_worst
285   8912521    Benign  ...          0.2505                  0.06431
290  89143602    Benign  ...          0.2272                  0.08799
294    891716    Benign  ...          0.2369                  0.06922
299    892399    Benign  ...          0.2227                  0.06777
'''

df1.shape  # (569, 32)
df1.shape[0] # 행의 갯수
df1.shape[1] # 열의 갯수

df1.shape[0]-vbool.sum() # 565 --> not null 행 수

print(df1.shape[0]-vbool.sum())

#
df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how='all')
df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how='all').shape[0]
nrow = df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how='all').shape[0]
print(nrow)

# 2. concavity_mean 의 standard scaling(표준화) 후, 결과가 0.1 이상인 값의 개수 출력
# standard scaling(표준화) = (원 데이터 - 평균) / 표준편차
# minmax scaling = (원 데이터 = 최소) / (최대-최소)

df1.columns
vscale = (df1['concavity_mean']-df1['concavity_mean'].mean()) / df1['concavity_mean'].std()

'''
0      2.650542
1     -0.023825
2      1.362280
3      1.914213
4      1.369806
  
564    1.945573
565    0.692434
566    0.046547
567    3.294046
568   -1.113893
Name: concavity_mean, Length: 569, dtype: float64
'''

(vscale > 0.1).sum() # 207

# 이상치 건 수 확인
# 3. texture_se 의 상위 10% 값(NA를 제외한 건수의 10%)을 이상치로 가정한다.
#    10%를 제외한 값의 최대값으로 수정하세요. 평균을 소수점 둘째자리로 반올림하여 출력

# 이상치 건수 확인
df1['texture_se'].dropna()
'''
0      0.9053
1      0.7339
2      0.7869
3      1.1560
4      0.7813
 
564    1.2560
565    2.4630
566    1.0750
567    1.5950
568    1.4280
Name: texture_se, Length: 565, dtype: float64
'''
df1['texture_se'].shape
df1['texture_se'].dropna().shape[0] # 565  :NA값이 빠진 값의 수

nx = int(np.trunc(df1['texture_se'].dropna().shape[0] * 0.1)) # 56 :
type(nx) # int(정수)

np.trunc?
a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
np.trunc(a)
# array([-1., -1., -0.,  0.,  1.,  1.,  2.])
# 소수점 아래 부분을 제거

# 이상치를 제외한 나머지 >> 평균
df1['texture_se'].rank(ascending = False, method = 'first')
vrank = df1['texture_se'].rank(ascending = False, method = 'first')

vrank
'''
0      393.0
1      474.0
2      448.0
3      265.0
4      451.0
 
564    221.0
565     19.0
566    292.0
567    107.0
568    159.0
Name: texture_se, Length: 569, dtype: float64
'''

df1.loc[vrank > nx, 'texture_se'] # 정상치 데이터
vmax = df1.loc[vrank > nx, 'texture_se'].max() # 정상치 데이터 최대값

df1.loc[~(vrank > nx), 'texture_se']
df1.loc[vrank <= nx, 'texture_se'] # 이상치 데이터
df1['texture_se'].sort_values(ascending=False)[:nx]

# 이상치 데이터를 Vmax(정상치 데이터 최대값) 치환

df.loc[vrank <= nx, 'texture_se'] = vmax

round(df1['texture_se'].mean(), 2)

# 참고 

_df = pd.DataFrame(
    {'name': ['KIM', 'LEE', 'SMITH','BROWN', 'MILLER'],
     'age': [24, 32, 43, 24, np.nan]})

'''
     name   age
0     KIM  24.0
1     LEE  32.0
2   SMITH  43.0
3   BROWN  24.0
4  MILLER   NaN

'''
# 동점자 처리 기준 5가지

_df['rank_average'] = _df['age'].rank(method='average') # default
'''
0    1.5
1    3.0
2    4.0
3    1.5
4    NaN
Name: age, dtype: float64
'''
_df['rank_min'] = _df['age'].rank(method='min')
'''
0    1.0
1    3.0
2    4.0
3    1.0
4    NaN
Name: age, dtype: float64
'''
_df['rank_max'] = _df['age'].rank(method='max')
'''
0    2.0
1    3.0
2    4.0
3    2.0
4    NaN
Name: age, dtype: float64
'''
_df['rank_first'] = _df['age'].rank(method='first')
'''
0    1.0
1    3.0
2    4.0
3    2.0
4    NaN
Name: age, dtype: float64
'''
_df['rank_dense'] = _df['age'].rank(method='dense')
'''
0    1.0
1    2.0
2    3.0
3    1.0
4    NaN
Name: age, dtype: float64
'''
# dense는 min과 유사, 그룹 간 순위 1 씩 증가

_df
'''
     name   age  rank_average  rank_min  rank_max  rank_dense  rank_first
0     KIM  24.0           1.5       1.0       2.0         1.0         1.0
1     LEE  32.0           3.0       3.0       3.0         2.0         3.0
2   SMITH  43.0           4.0       4.0       4.0         3.0         4.0
3   BROWN  24.0           1.5       1.0       2.0         1.0         2.0
4  MILLER   NaN           NaN       NaN       NaN         NaN         NaN
'''

_df['age'].rank(method='first')
'''
0    1.0
1    3.0
2    4.0
3    2.0
4    NaN
Name: age, dtype: float64
'''

_df['age'].rank(method='first', ascending=False)
'''
0    3.0
1    2.0
2    1.0
3    4.0
4    NaN
Name: age, dtype: float64
'''

# 4. symmetry_mean의 결측치를 최소값으로 수정한 후 평균을 소수점 둘째자리로
#    반올림하여 출력

df1['symmetry_mean'].min() # '-' 문자열이 포함되어있음

from numpy import nan as NA
df1['symmetry_mean'].replace('-', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('-', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('.', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('pass', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('<=', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].astype('float')

# 최소값 확인
vmin = df1['symmetry_mean'].min()

# 결측치 수정
df1['symmetry_mean'].fillna(vmin)
df1['symmetry_mean'] = df1['symmetry_mean'].fillna(vmin)

# 평균 확인
print(round(df1['symmetry_mean'].mean(), 2) # 0.18 (2는 소수점 자리수 표시)
