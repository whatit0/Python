# class : 멤버로 변수와 메소드를 포함한 집합체. 객체 중심의 독립적인 프로그래밍이 가능함. OOP 구현
class Car:
    handle = 0
    speed = 0

    def __init__(self, name, speed):
        self.name = name    # 자바랑 달리 멤버 변수가 없어도 자바의 this처럼 self로 사용 가능
        self.speed = speed

    def ShowData(self):
        km = '킬로미터'
        msg = '속도 : ' + str(self.speed) + km
        return msg

print(Car.handle)
# Car.showData()

# car 클래스 객체에 handle, speed, init()은 공유 멤버

car1 = Car('tom', 80)
print('car1 : ', car1.handle, car1.name, car1.speed, car1.ShowData())   # 0 tom 80
car1.color = '보라'   # car1 객체에 color 변수가 추가
print('car1 : ', car1.color)

print()
car2 = Car('james', 100)    # 새로운 인스턴스로 car2가 추가
print('car2 : ', car2.handle, car2.name, car2.speed, car2.ShowData())

print()
print(Car.handle, car1.handle, car2.handle)
print(Car.speed, car1.speed, car2.speed)
print(car1.color)
# print(car2.color), print(Car.color) 이거 두개는 에러, color는 car1만 가지고 있음

print(Car, car1, car2)
print(id(Car), id(car1), id(car2))
print(car1.__dict__)    # 각 객체의 멤버를 확인
print(car2.__dict__)

print('메소드-----------------')
print('car1 : ', car1.ShowData())   # car1의 객체 주소가 ShowData()에 담겨짐
print('car2 : ', car2.ShowData())

car1.speed = 55
car2.speed = 88
print('car1 : ', car1.ShowData())
print('car2 : ', car2.ShowData())

print()
Car.handle = 1  # 공유 멤버는 원형 클래스의 변수를 바꿔주면 됨
print('car1 : ', car1.handle, car1.name, car1.speed)   # 1 tom 80
print('car2 : ', car2.handle, car2.name, car2.speed)


















