# 자료형
# int, float, bool, complex : 객체 값 하나를 참조 / Immutable 객체(수정 불가) a=5 -> a=3은 객체 참조이지 수정이 아님
# str, list, tuple, set, dict : 묶음형 객체 값 참조


# str - 문자열 자료형 : 순서 있음(인덱싱, 슬라이싱 가능), 변경 불가
s = 'sequence'
# 문자열 관련 함수
print('길이 : ', len(s))
print('포함 횟수 : ', s.count('e'))
print('검색 위치 : ', s.find('e'), s.find('e', 3), s.rfind('e'))  # 0부터 시작, rfind는 뒤에서 부터

ss = 'mbc'
print('mbc', ss, id(ss))    # id는 해시코드, 객체의 고유 주소 값을 반환
ss = 'abc'
print('mbc', ss, id(ss))    # 수정 불가, 객체 참조

print(s, s[0], s[-7])   # 인덱싱
print(s, s[0:5], s[-7:-5], s[5:], s[:5], s[::2], s[0:7:3])    # 슬라이싱 / s[::2]는 건너띄기
print(s[0:5] + 'good')
print()
sss = ' mbc kbs sbs  '
print(sss)
print(sss.strip())   # 좌우 공백 자르기
print(sss.lstrip()) # 좌우 공백
print(sss.rstrip()) # 오른쪽 공백
ssss = sss.split(sep=' ')
print(ssss)
s5 = sss.replace('kbs', '공영방송') # 치환
print(s5)


print('list------------------')
# list : 배열과 유사하게 사용, 중복 자료 허용, 여러 종류의 값을 기억, 순서o, 변경o
a = [1,2,3]
print(a, type(a))
b = [10, a, 12.3, 'good', False]
print(b)
c = list();
print(c, type(c))
print()
family = ['준수', '예진', '정혜']
family.append('준호')     # 추가
family.insert(0, '민규')  # 삽입
family.extend(['tom', 'oscar'])
family += ['지원', '국인']
family.remove('tom')    # 삭제
# family.clear()    다 날리기
print(family, len(family), family[0])

print()
aa = [1,2,3,['a', 'b', 'kbs'],4,5]  # 중첩 리스트
print(aa, aa[0], aa[0:3])
print(aa[3], ' ', aa[3][2])

aa.remove(2)    # 값에 의한 삭제
del aa[3]       # 순서에 의한 삭제
print(aa)

print()
bb = aa     # 주소를 치환 : 같은 객체를 참조, 얕은 복사
print(aa, ' ', bb, ' ', id(aa), id(bb))    
bb[0] = 'nice'
print(aa, ' ', bb)

import copy
cc = copy.deepcopy(aa) # 주소 지환 : 새로운 공간이 확보, 깊은 복사
print(aa, ' ', cc, ' ' , id(aa), id(cc))
print(aa == cc, aa is cc)   # 내용은 같으나 주소는 다름
cc[0] = '쉬고 할까'
print(aa, ' ', cc)

print()
print('자료 구조 : stack, queue')
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop()   # 스택 구조로 LiFo 처리 
print(sbs)
sbs.pop()
print(sbs)

print('\n')
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop(0) # queue 구조로 LiFO 처리 
print(sbs)
sbs.pop(0)
print(sbs)
    
    
    
    











