# 사용자 정의 모듈 call
from modueltest.test14etc2 import Gop
print('뭔가를 하다가..... 다른 모듈 호출')

# 같은 패키지 내의 모듈 읽기
import pack2.test14other

print('score : ', pack2.test14other.score)
print(pack2.test14other.__file__)
print(pack2.test14other.__name__)

list1 = [1,2]
list2 = [3,4]
pack2.test14other.listHap(list1, list2)

def abc():
    if __name__ == '__main__':
        print('여기가 진짜 메인 모듈이야')
abc()

print()
pack2.test14other.kbs()
from pack2.test14other import kbs, mbc, score
kbs()
mbc()
print(score)


# 다른 패키지 내의 모듈 읽기
import modueltest.test14etc
modueltest.test14etc.Hap(5, 3)

from modueltest.test14etc import Hap, Cha
Hap(3, 2)
Cha(5, 2)

Gop(3,2)

import test14etc2
test14etc2.Gop(5, 3)
from test14etc2 import Nanugi
Nanugi(5, 2)








