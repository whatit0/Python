'''
'''
# 추상

from abc import ABCMeta, abstractmethod

class Friend(metaclass=ABCMeta):    # 추상 클래스
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def hobby(self):
        pass

    def printName(self):
        print('이름은 ' + self.name)

class John(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr = addr

    def hobby(self):
        print(self.addr + ' 거리를 산책함')

    def printAddr(self):
        print('주소는 ' + self.addr)


class Cris(Friend):

    def __init__(self, name, addr):
        super().__init__(name)
        self.addr = addr

    def hobby(self):
        print(self.addr + '에서 노는걸 좋아함')
        print(self.addr + '에 오래 전부터 살고 있다.')


john = John('미스터 존', '역삼1동')    # john은 John이 아니라 하나의 객체 / 인스턴스
john.printName()
john.printAddr()
john.hobby()
print()
cris = Cris("크리스 님", '역삼2동')
cris.printName()
cris.hobby()
print('-----------')
fri = john
fri.hobby()
print()
fri = cris
fri.hobby()