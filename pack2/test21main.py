import pack2.test21Singer

def process():
    rose = pack2.test21Singer.Singer()     # 인스턴스 된거임
    print('타이틀 송 : ', rose.title_song)
    rose.sing()
    rose.title_song = '로제 찬양가'
    rose.co = 'YG'
    print('소속사가 ' + rose.co + '인 가수의 노래 ' + rose.title_song)

    print()
    jisu = pack2.test21Singer.Singer()
    print('타이틀 송 : ', jisu.title_song)
    jisu.sing()
    # print('소속사가 ' + jisu.co + '인 가수의 노래 ' + jisu.title_song) - error
    print(id(pack2.test21Singer.Singer), id(jisu))  # 2469638664096 2469638664096 / ()가 있고 없고가 다르다, 차이점을 알아보자
    # ()가 있고 없고의 차이점은 jisu변수는 Singer 클래스의 인스턴스o / blackpink변수는 Singer 클래스 자체를 할당하여 인스턴스 생성x

    print()
    blackpink = pack2.test21Singer.Singer   # Singer 인스턴스의 주소를 가지고 와서 blackpink한테 넘겨준거임 / ()가 없으면 주소를 넘겨준거임
    print(id(pack2.test21Singer.Singer), id(blackpink)) # 2469638664096 2469650489040
    print('타이틀 송 : ', blackpink.title_song)
    # blackpink.sing() - error
    # jisu는 Singer 클래스의 인스턴스이므로 클래스내에 정의된 sing() 메서드를 호출o /


# 따라서 blackpink.sing()을 호출하면 에러가 발생합니다. 이것은 클래스 자체에 대한 메서드 호출이 아니라 클래스 인스턴스에 대한 메서드 호출이어야 합니다.
# 클래스 자체에 대한 메서드 호출은 클래스 메서드라고도 알려져 있으며, 이를 호출하려면 클래스의 정의 내에서 @classmethod 데코레이터를 사용하여 메서드를 정의해야 합니다.
# 그렇지 않으면 클래스 자체에 대한 메서드 호출은 에러를 발생시킵니다.
# 따라서 blackpink에서 에러가 발생하는 이유는 클래스 자체에 대한 메서드 호출이 제대로 정의되지 않았기 때문입니다.
# 클래스 자체에 대한 메서드를 호출하려면 클래스 내에서 @classmethod 데코레이터를 사용하여 메서드를 정의해야 합니다.



    


if __name__ == '__main__':
    process()