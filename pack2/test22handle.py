# 완성품 부품으로 핸들 클래스
class PohamHandle:
    quantity = 0    # 회전량

    def leftTurn(self, quantity):
        self.quantity = quantity
        return'좌회전'

    def rightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'


class PohamEngin:
    pass
