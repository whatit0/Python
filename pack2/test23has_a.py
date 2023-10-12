# 클래스의 포함관계 : 구긴이네 냉장고(객체)에 음식(객체) 담기

class Fridge:
    isOpened = False    # 냉장고 문 개폐 여부
    foods = []  # 음식물 담기용 리스트

    def open(self):
        self.isOpened = True
        print('냉장고 문을 열었습니다')

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)    # 포함관계 / list에 데이터 넣을땐 append
            print('냉장고 속에 음식 넣기 완료')
            self.list()
        else:
            print('냉장고 문이 닫혀서 음식을 넣을 수 없습니다')

    def close(self):
        self.isOpened = False
        print('냉장고 문 닫아주세요')

    def list(self):
        for f in self.foods:
            print('-', f.name, f.expiry_date)
        print()


# 음식물 클래스
class FoodData:
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date


# 실행
fr = Fridge()
apple = FoodData('사과', '2023-11-05')
fr.put(apple)

fr.open()
fr.put(apple)
fr.close()
print('----------')
cola = FoodData('콜라', '2025-10-05')
fr.open()
fr.put(cola)
fr.close()







