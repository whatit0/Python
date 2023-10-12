'''
여러 줄
주석
'''
# 한 줄 주석
print('환영합니다. 파이썬 세상 만세')

var1 = '안녕';    # '안녕', "안녕" 같음 / 줄 안 맞추면(들여쓰기) 에러
print(var1)     # 참조형 변수 : 인스턴스의 주소를 기억 / 파이썬 2.x대는 print, 3.x대는 print()로 사용
var1 = 5; print(var1)

a = 10
b = 20.5
c = b   # 주소를 치환
print(a, b, c)
print('주소 : ', id(a), id(b), id(c))
print(a is b, a == b)   # is : 주소 비교, == : 값 비교
print(b is c, b == c)

print()
a = [1, 2]
b = a
c = [1, 2]
print(a is b, a == b)
print(a is c, a == c)

print()
A = 1; a = 2;   # 변수는 대소문자를 구분
print(A, ' ', a)

print()
import keyword  # 설치는 되었으나 메모리에 로딩되지 않은 모듈 로딩하기
print('예약어 목록 : ', keyword.kwlist)  # 예약어는 사용자 정의 이름으로 사용하면 안됨

print()
print(10, oct(10), hex(10), bin(10))    # 10 0o12 0xa 0b1010
print(10, 0o12, 0xa, 0b1010)

print('자료형 확인')
print(5, type(5))           # int
print(5.1, type(5.1))       # float
print(5+6j, type(5+6j))     # complex
print(True, type(True))     # bool
print('a', type('a'))       # str
print('묶음형 자료형 ---')
print((1,), type((1,)))     # tuple / ,를 빼면 int(Integer)이 됨, 아마 숫자 여러 개 적으라는 뜻인듯
print([1], type([1]))       # list
print({1}, type({1}))       # set
print({'key':1}, type({'key':1}))   # dict


print('\n연산자 둘러보기 ---------')
v1 = 3  # 치환
v1 = v2 = v3 = 3
print(v1, v2, v3)

print('a', end=',') # 그냥 쓰면 println과 같고 end=를 하면 옆으로 옴
print('b')

v1 = 1,2,3;
print(v1)   # tuple 자동으로 다같이 묶여짐

v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2                     # 얘네는 왜 순서를 바꿔도 값이 같은지가 궁금하니깐 시간날 때 따로 찾아보자
print(v1, v2)

print('값 할당 packing')
*v1, v2 = 1,2,3,4,5  # 각 각에 변수에 어떤 숫자를 할당할지 모르니깐 에러가 떨어짐
v1, *v2 = 1,2,3,4,5  # 하지만 *를 쓰면 남은 숫자를 걔가 다 가져 감
print(v1, v2)

v1, *v2, v3 = 1,2,3,4,5 # *를 두 개 할당하는건 상식적으로 불가능
print(v1, v2, v3)

# print에 대해
print(format(1.5678, '10.3f'))
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))     # %를 쓸땐 %%
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))      # 중괄호를 쓸땐 format를 사용
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))


# 10월10일 파이썬 2일차
print('-------------------')
# 산술, 관계, 논리, 기타 연산
print(5 + 3, 5- 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 5 ** 3)
#     8    2    15  1.66..7(실수) 1(정수나누기) 2(나머지) 125(거듭제곱)
print(divmod(5, 3))
print(3 + 4 * 5, (3 + 4) * 5)   # 연산 우선 순위 : 소괄호 () > 산술(*, / > +, - ) > 관계 > 논리 > 치환

print(5 > 3, 5 == 3, 5 != 3)
print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 >= 3))
print('문자열 더하기 연산 ', end=':')
print('가을 ' + '하늘')
print("*"*20)   # 문자열 20번 찍기

print('누적')
a = 10
a = a + 1
a += 1
# a++ 증감연산자 x
print('a : ', a)
print('부호 변경 : ', a, -a, --a, +a, ++a, a * -1)  # -랑 * -1로 음수로 변경 가능

print('boolean : ', bool(False), bool(0), bool(0.0), bool(None), bool(""), bool([]), bool({}), bool(set())) # 파이썬에선 전부다 false / 부정형, 0, 값이 없음
print('boolean : ', bool(True), bool(1), bool(0.1), bool("kbs"), bool([1]), bool({1}), bool(set((1,)))) # 이건 다 true

print()
print('aa\tb')  # 'escape 문자 \ 어쩌구@@'
print('aa\nb')
print('aa\bb')
print(r'aa\tb') # 소문자 r을 붙히면 이스케이프로 인정하지 않고 순수 데이터로 인정한다
print(r'aa\nb')
print(r'aa\bb')

# python coding 규칙 : pep~ / https://cafe.daum.net/flowlife/RUrO/35











