# 다중 상속
class Tiger:
    data = '호랑이는 영어로 타이거'

    def cry(self):
        print('호랑이는 어흥어흥')

    def eat(self):
        print('호랑이는 상남자처럼 육식파')


class Lion:
    def cry(self):
        print('사자는 어떻게 울지?')

    def hobby(self):
        print('사자는 sns를 좋아한대')

class Liger1(Tiger, Lion):  # 다중 상속
    pass

obj1 = Liger1()
obj1.cry()  # 다중 상속에서 먼저 적은 클래스가 우선 순위
obj1.eat()
obj1.hobby()
print(obj1.data)

print('\n-------------------')
def hobby():
    print('모듈의 멤버인 함수')

class Liger2(Lion, Tiger):
    data = '라이거는 호랑이와 사자의 새끼'

    def play(self):
        print('라이거 고유 메소드')

    def hobby(self):
        print('라이거는 헬창이래')

    def showHobby(self):
        self.hobby()
        super().hobby()
        print(self.data + ', ' + super().data)


obj2 = Liger2()
obj2.cry()
obj2.showHobby()