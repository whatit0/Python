# 클래스의 상속
class Animal:       # 부모 클래스
    def __init__(self):
        print('Animal 생성자')
    def move(self):
        print('움직이는 생물')

class Dog(Animal):      # ()안에 부모 클래스를 넣으면 상속 받아짐 / 자식 클래스
    def __init__(self):
        print('멍멍이 생성자')
    def my(self):
        print('난 멍멍이야')

dog1 = Dog()    # Dog의 생성자가 없으면 부모의 생성자를 부르고 있으면 Dog 생성자를 부르고 끝
dog1.my()
dog1.move()

print()
class Horse(Animal):
    pass

horse1 = Horse()
horse1.move()