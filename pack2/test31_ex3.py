# 다중 상속 연습
class Animal:
    def move(self):
        pass

class Dog(Animal):
    name = '구름이'

    def move(self):
        print('구름이는 두 달에 한 번씩 미용실에 갑니다')

class Cat(Animal):
    name = '땅땅이'

    def move(self):
        print('땅땅이는 한 달에 한 번씩 PC방에 갑니다')
        print('밤에는 눈빛이 빛나요')


class Wolf(Dog, Cat):
    pass

class Fox(Cat, Dog):
    def move(self):
        print('여우는 사람을 홀려요')

    def FoxMethod(self):
        print('여우 고유 메소드입니다')


dog = Dog()
print(dog.name)
dog.move()
print()
cat = Cat()
print(cat.name)
cat.move()

print('------------------------')
wolf = Wolf()
print(wolf.name)
wolf.move()
print()
fox = Fox()
print(fox.name)
fox.move()
fox.FoxMethod()
print(Wolf.__mro__) # 클래스 탐색 순서 확인 / Wolf -> Dog -> Cat -> Animal -> Object 순서
print(Fox.__mro__)

print('-----------------')
sbs = wolf
sbs.move()
print()
sbs = fox
sbs.move()

print('-----------------')
animals = (dog, cat, wolf, fox)
for a in animals:
    a.move()
    print()
