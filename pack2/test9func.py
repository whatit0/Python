# 함수 : 반복소스의 단순화를 목표로, 여러 개의 수행문을 하나의 이름으로 묶은 실행단위
# 내장함수
from astropy.units import aa
from _ctypes_test import func
print(sum([3,4,5]))
print(bin(8))
print(int(1.5), float(3), str(5) + '오')
print(round(1.3), round(1.6))

import math
print(math.ceil(1.3), math.ceil(1.6))   # 올림
print(math.floor(1.3), math.floor(1.6)) # 버림

x = [10,20,30]
y = ['a', 'b']
for i in zip(x,y):
    print(i)
    

print()
# 사용자 정의 함수
# def 함수명(parameter, ...):
#     ...
#     [return <반환값>]

def func1():
    print('fucn1 수행')
    # return 생략 가능

func1()
print('딴짓 하다가')
func1()    
imsi = func1()
print(imsi) # return을 명시하지 않아서 None을 리턴
    

print()    
def func2(para1, para2):    # 파라미터(매개변수)
    result = para1 + para2
    aa = func3(result)
    return aa

def func3(result):
    if result % 2 == 1:
        return  # 그냥 리턴하면 None를 리턴
    else:
        return result
    
print(func2(3, 4))   # 아규먼트(인수)
print(func2(3, 5))
print(func2, id(func2))     # 0x000001E38FC75A80(실제 주소), 2076881410688(해시코드)
    
    
print()
def swap(a, b):
    return b, a     # 이건 return을 두개를 하는게 아니라 (b, a)인거다. 집합으로 넘어간 것

a = 10; b = 20
print(swap(a, b))


print()
def func4():    
    print('func4 처리')
    def func5():    # 함수안에 함수 선언 가능
        print('내부 함수 처리')   
    func5()
func4()


# if 조건식 안에 함수 사용
print()
def isodd(para):
    return para % 2 == 1

mydict = {x:x*x for x in range(0,11) if isodd(x)}
print(mydict)







    