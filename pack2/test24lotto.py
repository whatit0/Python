import random

class LottoBall:
    def __init__(self, num):
        self.num = num

class LottoMachine:
    def __init__(self):
        self.ballList = []
        for i in range(1, 46):
            self.ballList.append(LottoBall(i))  # 포함관계

    def selectBall(self):
        for a in range(45):
            print(self.ballList[a].num, end=' ')


class LottoUI:
    def __init__(self):
        self.machine = LottoMachine()   # 클래스의 포함관계

    def playLotto(self):
        input('로또 볼을 뽑으려면 엔터키를 누르세요')
        selectedBalls = self.machine.selectBall()
        for ball in selectedBalls:
            print('%d'%ball.num)

if __name__ == '__main__':
    LottoUI().playLotto()
