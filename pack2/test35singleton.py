# singleton pattern

class Singletonclass:
    inst = None

    def __new__(cls):   # 객체 생성을 담당. init에 의해 초기화됨
        if cls.inst is None:
            cls.inst = object.__new__(cls)
        return cls.inst

    def aa(self):
        print('난 메소드야')

class SubClass(Singletonclass):     # 싱글톤 클래스를 상속 받는 클래스는 싱글톤 객체 생성o / 주소가 같아짐
    pass

s1 = SubClass()
s2 = SubClass()
print(id(s1), id(s2))   # 1769202259920 1769202259920 / 주소가 같음

s1.aa()
s2.aa()

print('--------------')
# 클래스의 멤버 변수를 고정
class Ani:
    __slots__ = ['name', 'age']

    def printData(self):
        print(self.name, self.age)

a = Ani()
a.name = '늑대'
a.age = 5
a.printData()