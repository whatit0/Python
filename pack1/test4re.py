# 정규 표현식 : 특정한 규칙을 가진 문자열의 집합을 표현하기 위해 쓰이는 형식 언어
import re

ss = "1234 abc가나다abcABC_1234555_6python si fun파이썬 만세"
print(ss)
print(re.findall(r'123', ss))
print(re.findall(r'가나', ss))

print(re.findall(r'[1,2,5]', ss))
print(re.findall(r'[1,2,5]+', ss))  # 반복 관련 메타문자 + : 1회 이상
print(re.findall(r'[0-9]+', ss))    # 문자 집합[] / 숫자 이외가 나오면 멈춤
print(re.findall(r'[^0-9]+', ss))   # 문자 집합 [^]은 부정(여집합)
print(re.findall(r'\d+', ss))       # 특수문자 \d / 숫자만 1개 이상, 다른거랑 똑같음
print(re.findall(r'\D+', ss))       # 소문자, 대문자는 반대 / 숫자 이외만 나와라
print(re.findall(r'[0-9]{2}', ss))  # {n} n회
print(re.findall(r'[0-9]{2,3}', ss))    # 두글자 또는 세글자 
print(re.findall(r'[가-힣,a-z,A-Z]+', ss))
print(re.findall(r'^1234', ss))     # 문자 집합체에서 ^를 쓰면 부정이지만 문자열 맨 앞에 쓰면 시작
print(re.findall(r'만세$', ss))       # 문자열 끝

print()
ss = '''
<a href="abc1.html">abc1</a>
<a href="abc2.html">abc1</a>
<a href="abc3.html">abc1</a>
'''
print(ss) 
result = re.findall(r'href="(.*)"', ss)  # 큰 따음표안에는 작은 따음표, 작은 따음표안에는 큰 따음표
print(result)

print()
p = re.compile('the', re.IGNORECASE)    # flag 사용하기
print(p.findall('The dog the dog'))     # 소문자, 대문자 상관없이 가져 옴

s = """My name is tom
I am happy"""
print(s)
p = re.compile('^.+', re.MULTILINE)
print(p.findall(s))





