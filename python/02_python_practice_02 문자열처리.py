# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:25:10 2021

@author: kth96
"""

# 함수와 메소드
# 함수 : 함수(대상)
# 메서드: 대상. 메소드

# 대소 치환
v1 = 'abcde' #문자(string)
v1.upper()   #대문자 치환
'ABCDE'.lower() #소문자 치환
'abc def'.title() # camel 표기법 (단어의 첫글자만 대문자로 표시)

# 색인(문자열 추출)
'abcd'[0]
'abcd'[-2]
'abcd'[0:3]

# ex) '031)345-0834' 에서 지역번호만 추출
vtel = '031)345-0834'
vtel[0:3]

# 문자열의 시작, 끝 여부 확인
# v1.startswith(prefix,   # 시작 값 확인 문자
#               start,    # 확인할 시작 위치
#               end)      # 확인할 끝 위치

v1
v1.startswith('b')
v1.startswith('b',1)
v1[1:].startswith('b')

# v1.endswith(suffix,
#             start,
#             end)

v1
v1.endswith('e')
v1.endswith('E')

# 앞 뒤 공백 또는 문자 제거
'abc' == 'abc' # ''와''가 같다면
' abc '.strip() # 양쪽 공백 제거
'abc'.strip('a') # 문자 제거
'abaca'.strip('a') # 양 끝의 문자만 제거(중간 글자 삭제 불가)

' abcd'.lstrip() # 왼쪽 공백 또는 글자 제거
' abcd '.rstrip() #오른쪽 공백 또는 글자 제거

# 치환
# 'abcabc'.replace(old,  # 찾을 문자열
#                 new)  # 바꿀 문자열

'abcabc'.replace('a','A')
'abcabc'.replace('ab','AB')
'abcabc'.replace('ab','')

# 문자열 분리
# v1.split(sep) # 분리 구분기호
'a/b/c/d'.split('/') #/를 기준으로 구분
'a/b/c/d'.split('/')[1]
'a/b/c/d'.split('/')[0:2]

# 위치값 리턴
# 'abcd'.find(sub,     # 위치값을 찾을 대상
#             stard,   # 찾을 위치(시작점)
#             end)     # 찾을 위치(끝점)

v1
v1.find('b')

# ex. 전화번호에서 지역번호 추출하려고 함. 
# ')' 위치 확인해서 그 이전까지 추출
vtel 
vnum = vtel.find(')')
vtel[0:vnum]
vtel[:vnum]

# 포함 횟수
'abcabcabc'.count('a')

# 형 확인
type(v1) # 데이터 타입 확인
v1.isalpha() # 문자 확인
v1.isnumeric() # 숫자 확인

# 대소문자 확인
v1.isupper()
v1.islower()

# 문자열 결합
'a' + 'b'

# 문자열 길이
len(v1)
3/len(v1)

# 연습문
vname='revil'
vemail='kth960302@naver.com'
jumin = '960302-1111111'

# 1. 이름의 두번째 글자가 m인지 여부 확인
vname[1] == 'm'
vname[1] == 'r'

# 2. vemail에서 이메일 아이디만 추출
vemail[0:9]

emname = vemail.find('@')
vemail[:emname]

# 3. 주민번호에서 여자인지 확인 (참고: 1: 남자 2: 여자)

jumin
jumin.split('-')[1][0] == '2'
jumin.split('-')[1][0]
# '960302-1111111'
list(jumin.split('-'))
# ['960302', '1111111']
jumin[7] == '2'


