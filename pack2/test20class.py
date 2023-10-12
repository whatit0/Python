# class 멤버 호출 관련

kor = 100

def abc():
    print('모듈의 멤버 함수')

class MyClss:

    kor = 90
    def abc(self):
        print('abc 메소드')

    def show(self):
        # kor = 80
        # print(self.kor)
        print(kor)  # 변수 호출 순서 : 지역 변수 > 모듈 변수
        self.abc()  # method를 호출
        abc()   # 함수를 호출

my = MyClss()
my.show()

from pack2.test20other import Our
print(Our.a)

print('our1 ---')
Our1 = Our()
print(Our1.a)
Our1.a = 2
print(Our1.a)

print('our2 ---')
Our2 = Our()
print(Our2.a)   # Our1의 a값이 Our2에 영향을 주지 않는다 / 공유 멤버의 a를 바꾼게 아니라 Our1의 인스턴스 a의 값을 바꾸었기 때문에

