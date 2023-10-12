# 변수의 생존 범위 : global, local
# Local > Enclosing function > Global < Builtin
from dask.array.random import choice

player = '국가대표' # 전역변수 (모듈의 어디서든 공유 가능)

def funcSports():
    name = '신기루'    # 지역변수(함수 내에서만 유효)
    player = '지역대표' # 로컬에 우선순위가 더 높기 때문에 이게 찍힘
    print(name, player)
    
funcSports()


print()
a = 1; b = 2; c = 3
print('출력1 -- a:{}, b:{}, c:{}'.format(a,b,c))
def outerfunc():
    a = 4
    b = 5
    def innerfunc():
        global c    # 지역변수에서 전역변수가 됨
        nonlocal b  # innerfunc가 아니라 outerfunc 지역변수가 됨
        #c = 6
        print('출력2 -- a:{}, b:{}, c:{}'.format(a,b,c))
        c = 6
        b = 7
    innerfunc()
    print('출력3 -- a:{}, b:{}, c:{}'.format(a,b,c))
    
outerfunc()
print('출력4 -- a:{}, b:{}, c:{}'.format(a,b,c))


print('\n인수와 매개변수 키워드 매칭 ----------')
def showGugu(start, end=5):   # 파라미터에 초기치를 줄 수 있음
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력', end=' ')
    print()
    
showGugu(2, 9)  # 위치 매개변수(인수와 매개변수가 순서대로 대응)
showGugu(2)     # 기본값 매개변수(매개변수의 기본값이 없으면 초기치를 이용)
showGugu(start=2, end=3)    # 키워드 매개변수(인수와 매개변수의 이름이 같으면 됨) 
showGugu(end=3, start=2)    # 얘도 이름만 같으면 순서가 바뀌어도 됨
showGugu(2, end=4)
#showGugu(start=2, 4)    SyntaxError: positional argument follows keyword argument
#showGugu(end=3, 2)    얘도 마찬가지로 SyntaxError


print()
# 가변 매개변수 : 인수의 갯수가 동적
# *a, b = [1,2,3,4,5]
def fu1(*ar): # parameter에 pack연산을 줄 수도 있다.
    print(ar)
    for a in ar:
        print('밥: ' + a)
        
fu1('공기밥', '주먹밥')
fu1('공기밥', '주먹밥', '돈까스')

def fu2(bap, *ar): # parameter에 pack연산을 줄 수도 있다.
# def fu2(*ar, bap): 에러발생
    print(bap)
    print(ar)
    for a in ar:
        print('밥: ' + a)
        
fu2('공기밥', '주먹밥')
fu2('공기밥', '주먹밥', '돈까스')
    

print()
def selectCalc(choice, *ar):
    if choice == '+':
        imsi = 0
        for i in ar:
            imsi += i
    elif choice == '*':
        imsi = 1
        for i in ar:
            imsi *= i
    return imsi
    
print(selectCalc('+', 1,2,3,4,5))   # tuple 자료를 넘기는거임
print(selectCalc('*', 1,2,3,4,5))

# dict를 인수로 전달 / 앞에서 한 dict 사용법을 다시 보고 오자
def fu3(w, h, **etc):
    print('몸무게:{}, 키:{}'.format(w, h))
    print(etc)

fu3(66, 177, irum='홍길동')
fu3(77, 178, irum='고길동', nai=22)

print()
def fufinal(a,b,*c,**d):
    print(a, ' ', b)
    print(c)
    print(d)
    
fufinal(1, 2)
fufinal(1, 2, 3, 4, 5)
fufinal(1, 2, 3, 4, 5, m=6, n=7)









