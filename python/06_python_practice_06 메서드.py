# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:32:13 2021

@author: kth96
"""

# 문자열 메서드
# 문자열 처리와 관련된 메서드

# 1. 기본 메서드 : 벡터 연산 불가 (매 원소마다 반복 불가)

'abc'.upper()
'a/b/c'.split('/')
'a/b/c'.split('/')[1]

l1=['abc','def']
l2=['a/b/c','d/e/f']

l1.upper() #불가
l2.split() #불가

list(map(lambda x: x.upper(),l1))
['ABC', 'DEF']

list(map(lambda x: x.split(),l2))

# pandas 메서드 : 벡터화 내장(매 원소마다 반복 가능)
# Series, DataFrame

# 1) split

from pandas import Series, DataFrame

l1
Series(l1)
# 0    abc
# 1    def
# dtype: object

s1 = Series(l1)

l2
# ['a/b/c', 'd/e/f']
Series(l2)
# 0    a/b/c
# 1    d/e/f
# dtype: object
s2=Series(l2)

s2.str.split('/')
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

# 2) 대소 치환
s1
# 0    abc
# 1    def
# dtype: object

s1.str.upper()
s1.str.lower()
s1.str.title()

# 3) replace *중요하다....
s1.str.replace('a','A')
# 0    Abc
# 1    def
# dtype: object

s1.str.replace('a','') # 매우 중요..
# 0     bc
# 1    def
# dtype: object

# 천단위 구분기호 처리

s3 = Series(['1,200','3,000','4,000'])
s3.sum()

s3 = s3.str.replace(',','').astype('int').sum()
s3

# 4) 패턴 확인 : startwith, endwith, contains
s1
# 0    abc
# 1    def
# dtype: object
s1.str.startswith('a')
# 0     True
# 1    False
# dtype: bool
s1[s1.str.startswith('a')] # s1 각 원소에서 'a'로 시작하는 원소 추축
# 0    abc
# dtype: object
s1[s1.str.endswith('c')] # s1 각 원소에서 'c'로 끝나는 원소 추출
s1[s1.str.contains('e')] # s1 각 원소에서 'e'를 포함하는 원소 추출

# 문자열 크기 len()
s1.str.len()
# 0    3
# 1    3
# dtype: int64

# count 포함 개수
Series(['aabbbb','abcdadd']).str.count('a')
# 0    2
# 1    2
# dtype: int64

# 제거 함수 (공백, 문자)
Series(['     cd      ','        df         '])
Series(['     cd      ','        df         ']).str.strip()
# 0    cd
# 1    df
# dtype: object
Series(['     cd      ','        df         ']).str.strip().str.len()

s1
# 0    abc
# 1    def
# dtype: object

s1.str.strip('a') # 문자열 제거
Series(['aaabaaabcd','abcdaa']).str.strip('a')
# 문자열 제거(중간값 삭제 불가)
# 0    baaabcd
# 1        bcd
# dtype: object
Series(['aaabaaabcd','abcdaa']).str.replace('a','')
# 문자열 제거 (중간값 삭제 가능)

# find(위치값 return)
s3 = Series(['kth960302@naver.com','abcdef@naver.com'])
s3.str.find('@')
s3

s3.str.split('@')[0]
# 문자열 색인(추출)
'abcde'[0:3] # 문자열 색인
s3[0:3] # Series에서 1번째, 2번째, 3번째 원소 추출
s3.str[0:3] # Series에서 각 원소마다 1번째, 2번째, 3번째 원소 추출

# 이메일 아이디 추출
# 방법1
en = s3.str.find('@')
list(map(lambda x, y : x[0:y], s3, en))
# 방법2
list(s3.map(lambda x: x[:x.find('@')]))

# s3.str[0:s3.str.find('@')]
# 방법 3
s3.map(lambda x: x[:x.find('@')])

# pad : 문자열 삽입

s1.str.pad(5,             # 자리수
           'Left',        # 삽입 방향
           '!')           # 삽입 글자
s1

s1.str.pad(5,'left','!')
# 0    !!abc
# 1    !!def
# dtype: object

s1.str.pad(5,'right','^')

s5 = Series(["김치","치즈"])
s5.str.pad(4, 'right', '^')

# 문자열 결합
'a' + 'b'
'a'*3

s6= Series(['abc','def','123'])
s6.str.cat()
s6.str.cat(sep=',')
s6.str.cat(sep='/')

s7 = Series([['a','b','c'],['d','e','f']])
s7
s7.str.join(sep='') # Series 내 각 원소 내부의 문자열을 결합(공백)
s7.str.join(sep=',') # Series 내 각 원소 내부의 문자열을 결합(,)


# 번외

s7 = Series(['a','b','c'],['d','e','f']) #(내부 리스트화 하지 않음)
s7 = Series(['a','b','c'],['d','e','f'])

Series(['a','b','c'],index = ['drwill','zzuyu','hyory'])
Series(['a','b','c'],['drwill','zzuyu','hyory'])



s7 = Series(['a','b','c'],['d','e','f'],['g','h','i'],['j','k''l'])
s7


s3
for i in s3:
    s3.split('@').index[0:]

s3.str.split('@')

lo= s3.str.find('@')
s3.str[0:lo]

s3 = Series(['kth960302@naver.com','abcdef@naver.com'])
s3
for index, value in s3.items():
    print(f"index : {index}, e-mail ID : {value}")
    
for index, value in s3.items():
    print(f"순번 : {index}, e-mail ID : {value.split('@')[0]}")

