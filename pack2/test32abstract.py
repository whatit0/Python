# 추상 클래스 : 추상 메소드를 한 개라도 가지고 있다면 추상 클래스가 된다.
from abc import abstractmethod, ABCMeta

class AbstractClass(metaclass=ABCMeta):     # 추상 클래스 - 객체 생성x
    @abstractmethod
    def abcMethod(self):
        pass