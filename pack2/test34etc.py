from abc import abstractmethod, ABCMeta
class Employee(metaclass=ABCMeta):
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
        print('이름:{},나이:{}'.format(self.irum, self.nai), end=' ')



