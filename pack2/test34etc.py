from abc import abstractmethod, ABCMeta
class Employee(metaclass=ABCMeta):      # employee는 원형 멤버는 없고 전부 self를 타고 각 각의 인스턴스에 가지고 있음
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def data_print(self):
        pass

    def irumnai_print(self):
        print('이름:{}, 나이:{}'.format(self.irum, self.nai), end='')



