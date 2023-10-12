# 반복문 for
# for target in object: ...

for i in [1,2,3,4,5]:
    print(i, end=' ')
    
print()
for i in {1,2,3,4,5}:
    print(i, end=' ')
    
print()
for i in (1,2,3,4,5):
    print(i, end=' ')
    
print()
soft = {'java':'웹용언어', 'python':'만능언어', 'js':'웹용스크립트'}
for i in soft.items():
    # print(i)    # ('java', '웹용언어')
    print(i[0] + '^^;' + i[1])
    
for k, v in soft.items():
    print(k)
    print(v)

print()
for aa in soft.keys():
    print(aa, end=' ')

print()
for bb in soft.values():
    print(bb, end=' ')

print()
numbers = [1,3,5,7,9]
tot = 0
for a in numbers:
    tot += a
print('합은 ' + str(tot) + ', 평균은 ' + str((tot / len(numbers))))


print()
li = ['a', 'b', 'c']
for k, d in enumerate(li):
    print(k, d)
    
    
print()
for n in [2, 3]:
    print('---{}단--'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{}*{}={}'.format(n, i, n*i), end=' ')
    print()
    

print()
datas = [1,2,3,4,5]
for i in datas:
    if i == 2:continue
    if i == 4:break
    print(i, end=' ')
else:
    print('for 정상 종료')
    
    
print()
jumsu = [95, 70, 60, 55, 100]   # 70점 이상만 합격 처리
num = 0
for jum in jumsu:
    num += 1;
    if jum <70:continue
    print('%d번째 합격'%num)
    
    
print()
print('for + 정규 표현식 연습 ----------')
import re
ss = '''
팔레스타인 무장 정파 하마스가 이스라엘을 공격하면서 북한제 로켓 발사기를 사용한 정황이 포착됐다. 북한 노동당 기관지 노동신문은 수백명의 민간인이 희생된 이스라엘을 비난했다.
미국 자유아시아방송(RFA)은 9일(현지시간) ‘워 누아르(War Noir)’를 필명으로 활동하는 군사 전문 블로거의 분석을 인용해 “민간인을 무차별적으로 살상‧납치한 하마스 무장대원들이 북한제 무기를 사용한 것으로 추정된다”고 보도했다.
이 블로거는 하마스의 이스라엘 남부 기습 공격 이튿날인 지난 8일 SNS 플랫폼 엑스(옛 트위터)에 “영상에 촬영된 하마스 대원 중 1명이 북한에서 제작된, (다른 국가에서) 흔하게 사용되지 않는 F-7 고속 파편 로켓을 보유한 장면을 볼 수 있다”고 적었다.
이 블로거는 영상에서 발췌한 사진 2장도 공유했다. 이 영상은 하마스가 이스라엘을 기습 공격했던 지난 7일 이스라엘계 독일 국적의 22세 여성 샤니 루크를 납치에 트럭에 실어 가자지구로 진입한 장면을 담고 있다.
이 블로거는 영상에서 발췌한 사진 2장도 공유했다. 이 영상은 하마스가 이스라엘을 기습 공격했던 지난 7일 이스라엘계 독일 국적의 22세 여성 샤니 루크를 납치에 트럭에 실어 가자지구로 진입한 장면을 담고 있다.
이 영상은 하마스가 이스라엘을 기습 공격했던 지난 7일 이스라엘계 독일 국적의 22세 여성 샤니 루크를 납치에 트럭에 실어 가자지구로 진입한 장면을 담고 있다.
'''
print(type(ss))
ss2 = re.sub(r'[^가-힣\s]', '', ss)
print(ss2)
ss3 = ss2.split(' ')
print(ss3)  # ['\n팔레스타인', '무장', '정파', ...

cou = {}    # 단어의 발생 횟수를 dict로 저장
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1
print(cou)


print()
for ss in ['111-1234', '일이삼-이이이이', '234-6789']:
    if re.match(r'\d{3,4}-\d{4}$', ss):
        print(ss, '전화번호 맞아요')
    else:
        print(ss, '전화번호 아닌듯')


print()
# 리스트 컴프리헨션(List Comprension)은 직관적으로 리스트를 생성하는 방법입니다
# 대괄호 "[", "]"로 감싸고 내부에 for문과 if 문을 사용하여 반복하며 조건에 만족하는 것만 리스트로 생성할 수 있습니다
a = 1,2,3,4,5,6,7,8,9,10
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)
print(list(i for i in a if i % 2 == 0))


print()
i1 = [3,4,5]
i2 = [0.5, 1, 2]
result = []
for a in i1:
    for b in i2:
        result.append(a + b)
print(result)
print('-----')
datas = [a + b for a in i1 for b in i2]     # 이렇게 표현할 수 있다는 거임
print(datas)


print()
temp = [1,2,3]
for i in temp:
    print(i, end=' ')
print()
print([i for i in temp])    # list
print({i for i in temp})    # set / 빼내고싶은대로 


print()
datas = [1,2,'a',True,3]
li = [i * i for i in datas if type(i) == int]
print(li)

datas = {1,1,2,2,3,2,1}     # set type이라 중복x
imsi = {i * i for i in datas}
print(imsi)


print()
id_name = {1:'tom', 2:'oscar'}
print(id_name)
name_id = {val:key for key, val in id_name.items()}
print(name_id)


print()
aa = [(1,2),(3,4),(5,6)]
for a, b in aa:
    print(a + b)
    
    
# sum([1,2,3])
print('과일 값 계산 --------')
price = {'사과':5000, '감':500, '배':1000}  # 오늘 과일 시세
guest = {'사과':3, '감':2}
bill = sum(price[f] * guest[f] for f in guest)
print('고객이 구매한 과일 총액은 {}원'.format(bill))


print('---range 함수------------')
print(list(range(1, 11, 2)))
print(list(range(-10, -100, -20)))
print(set(range(1, 11, 2)))
print(tuple(range(1, 11, 2)))


print()
for i in range(6):  # 0 이상 6미만 증가치1
    print(i, end=' ')
    

print()
tot = 0
for su in range(1, 11):
    tot += su
print('결과 : ' + str(tot))
print("내장함수 : " + str(sum(range(1, 11))))

for _ in range(6):
    print('들자')
    
for i in range(1, 10):
    print('{0}*{1}={2}'.format(2, i, 2*i))


print()
# 문자1 : 2 ~ 5단 출력
for i in range(2, 6):
    for j in range(1, 10):
        print('{0}*{1}={2}'.format(i, j, i*j), end=' ')
    print()

print()
# 문2 : 1 ~ 100 사이의 정수 중 3의 배수이면서 5의 배수의 합 출력
ii = 0
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        ii += i
print(ii)
    
print()
# 문3 : 주사위를 두 번 던져 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
sum1 = 0
for i in range(1,7):
    for j in range(1,7):
        sum1 = i + j
        if sum1 % 4 == 0:
            print('주사위1:' + str(i) + ' ' + '주사위2:' + str(j) + ' ' + '합은:' + str(sum1))

import random

for _ in range(1, 37):
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    if (n1 + n2) % 4 == 0:
        print(n1, n2)