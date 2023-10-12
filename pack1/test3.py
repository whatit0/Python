print('tuple--------------------------------')
# tuple : list와 유사하나 읽기 전용(list 보다 처리 속도가 빠름) - 순서o, 수정x
# t = ('a', 'b', 'c')
t = 'a', 'b', 'c'   # 괄호 안써도 인정
print(t, type(t), len(t))
print(type(tuple()))
print(t[0])
# t[0] = 'k'    tuple은 치환 불가이다 / 'tuple' object does not support item assignment
li = list(t)    # 형변환
li[0] = 'k'
t = tuple(li)
print(t, type(t))

# p = (1) 이렇게 하면 집합형이 아니라 Integer임
p = (1,)    # 이렇게 해야 인정
print(p, type(p))


print()
print('set------------------------------------------------')
# set type : 순서x, 수정x, 중복 불가
a = {1, 2, 3, 1, 2, 3}  # 중복 불가
print(a, type(a))
print(type(set()))
# print(a[0])   순서x / 'set' object is not subscriptable
# a[0] = 10    수정 불가(인덱싱이 불가하므로 수정도 불가)

b = {3, 4}
print(a.union(b))   # 합집합
print(a.intersection(b))    # 교집합
print(a - b, a | b, a & b)  # 차, 합, 교집합

print()
b.update({6, 7})    # 원소 추가 / 원술은 추가안하나??
b.update((8, 9))    # tuple
b.update([9, 10])   # list 다 가능
print(b)

b.discard(7)    # 값에 의한 삭제
b.remove(8)     # 값에 의한 삭제
b.discard(7)    # 값에 의한 삭제인데 해당 값이 없으면 스킵
# b.remove(8)     # 값에 의한 삭제인데 해당 값이 없으면 에러
print(b)

li = ['국인', '배고파', '점심']
s = set(li)
li = list(s)
print(li)


print()
print('dict--------------------------------------------')
# dict type : 키:값의 형태로 쌍을 이룸, 순서x, 키를 이용해 값을 조회
mydic = dict(k1=1, k2='123', k3=3.4)
print(mydic, type(mydic))   # key는 문자열, 순서있다고 착각x(순서 없음)

dic = {'파이썬':'뱀', '자바':'커피', '스프링':'봄', '숫자':[1,2,3]}
print(dic, type(dic), len(dic))
print(dic['자바'])    # 키로 값을 참조
# print(dic['커피'])    KeyError: '커피' / key를 가지고 value를 찾아내는거임
print(dic['스프링'])
dic['자바'] = '프로그래밍언어'   # 해당 키로 값을 수정
print(dic)
dic['오라클'] = '예언자'  # 추가
print(dic)
del dic['오라클']  #삭제
dic.pop('숫자')   #삭제
print(dic)
print(dic.keys())
print(dic.values())















