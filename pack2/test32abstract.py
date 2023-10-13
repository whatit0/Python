# 추상 클래스 : 추상 메소드를 한 개라도 가지고 있다면 추상 클래스가 된다.
from abc import abstractmethod, ABCMeta

class AbstractClass(metaclass=ABCMeta):     # 추상 클래스 - 객체 생성x
    @abstractmethod # 추상 메소드로 지정
    def abcMethod(self):
        pass
    
    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드')

# parent = AbstractClass()  # err / 추상 클래스는 객체 생성x, 부모로써 의미만 있음
''' 똑같이 에러
class Child1(AbstractClass):
    pass

c1 = Child1()
'''

class Child1(AbstractClass):
    name = '난 Child1'
    def abcMethod(self):
        print('Child1에서 추상 메소드를 오버라이드함 : 순전히 강요 때문에')

c1 = Child1()   # 오버라이드하고 나니깐 에러가 안 뜬다
print(c1.name)
c1.abcMethod()
c1.normalMethod()
print()

class Child2(AbstractClass):
    def abcMethod(self):        # 오버라이드 강요
        print('Child2에서 추상 메소드를 재정의함')
        print('추상의 마법에서 벗어남')

    def normalMethod(self):     # 오버라이드 선택
        print('추상 클래스의 일반 메소드를 재정의함')


c2 = Child2()
c2.abcMethod()
c2.normalMethod()


print('\n----------------')
good = c1
good.abcMethod()
good.normalMethod()
print()
good = c2
good.abcMethod()
good.normalMethod()