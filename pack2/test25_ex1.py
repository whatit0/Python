'''
커피는 한 잔에 200원
100원 넣고 커피를 요구하면 요금 부족 메시지 출력
400원 넣고 2잔 요구하면 두 잔 출력
500원 넣고 1잔 요구하면 300원 반납

--출력 형태 --
동전을 입력하세요 : 400
몇 잔을 원하세요 : 2
커피 2잔과 잔돈 0원
'''


class Machine:
    cupCount = 1
    def __init__(self):
        self.coinin = CoinIn()

    def showData(self):
        self.cupCount = int(input('몇 잔을 원해 : '))
        coin = int(input('동전을 입력 : '))
        price = self.coinin.coin * self.cupCount
        if price == coin:
            print('커피' + str(self.cupCount) +'잔과 잔돈' + str(price - coin) + '원')
        elif price > coin:
            print('요금이 부족합니다')
        elif price < coin:
            print('커피' + str(self.cupCount) +'잔과 잔돈' + str(coin - price) + '원')


class CoinIn:
    coin = 200
    change = 0
    def __init__(self):
        pass

    def cluc(self):
        pass

if __name__ == '__main__':
    Machine().showData()

'''

# 커피는 200원
class Machine:
    cupCount = 1
    def __init__(self):
        self.coin = CoinIn()


    def showData(self):

        coin = int(input("동전을 입력하세요 : "))
        self.cupCount = int(input("몇 잔을 원하세요 : "))
        result = coin - self.coin.culc(self.cupCount)
        if result < 0:
            print("요금 부족")
        else:
            print("커피 {}잔과 잔돈 {}원".format(self.cupCount, result))

class CoinIn:

    coin = 0
    change = 0

    def culc(self, cupCount):
        self.change = cupCount * 200
        return self.change


if __name__ == '__main__':
    Machine().showData()
'''




