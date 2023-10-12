# 모듈의 멤버 중 클래스
# 클래스는 새로운 이름 공간을 지원하는 단위로 메소드와 변수라는 멤버를 지닌다.
# 클래스는 이름 공간과 클래스가 생성하는 인스턴스 이름 공간을 각 각 가진다.
# 접근지정자는 없다.(전부 public) / 메소드 오버로딩도 없다.

class TestClass:    # 클래스의 header 부분이며 이하 소스는 body 영역이 된다.
    aa = 1          # 멤버 변수는 클래스 내에서 전역 / 클래스나 함수 등등 존재만 하고 내용이 필요없을 땐 pass를 쓰면 됨
    
    def __init__(self):     # 메소드의 첫 파라미터는 self이다 / this처럼 생각하면 됨
        print('생성자')      # 생성자 - 클래스가 진행되기전에 클래스의 초기화 작업을 수행

    def __del__(self):
        print('소멸자')      # 소멸자 - 클래스가 진행되면서 마지막에 작업을 수행

    def printMsg(self):     # 멤버 메소드
        name = '한국인'      # 지역 변수
        print(name)
        print(self.aa)

test = TestClass()  # 생성자 호출 후 인스턴스가 만들어짐
print(test.aa)
# method call
test.printMsg()     # 방법1 : Bound method call / 객체 변수의 이름으로 부를 시 객체 변수를 쓰면 인수로 자동 들어가짐
TestClass.printMsg(test)    # 방법2 : UnBound method call / 얜 클래스 이름으로 부르고 객체 변수를 직접 넣음
print()
print(isinstance(test, TestClass))  # True
print(type(1))
print(type(test))
print(id(test), id(TestClass))

del test    # 인스턴스 삭제