# 에러의 종류
# syntex : 문법 오류
# logic : 프로그램 실행 중에 발생하는 오류로 프로그램이 비정상적으로 종료되는 오류
# exception : 예외란 코드를 실행하는 중에 발생하는 오류 -> try ~ except문 사용

def divide(a, b):
    return a / b

print('뭔가를 하다가.....')
'''
# c = divide(5, 2)
c = divide(5, 0)    # ZeroDivisionError: division by zero
print(c)
'''
try:
    #c = divide(5, 2)
    c = divide(5, 0)    # 여기서 에러가 떨어졌기 때문에 밑에는 실행x
    print(c)

    aa = [1,2]
    print(aa[0])
    #print(aa[2])    # IndexError: list index out of range

    f = open(r'c:/work/abc.txt')    # FileNotFoundError: [Errno 2] No such file or directory: 'c:/work/abc.txt'
    print('계속')

except ZeroDivisionError:
    print('두번째 숫자는 0을 주지 말자')
except IndexError as e:
    print('참조 범위 오류 : ', e)
except Exception as err:    # 기타 나머지 오류들.. / 제로디비전이랑 인덱스보다 얘를 먼저 적으면 얘가 어그로를 다 먹어버림, 순서를 가지고 싶으면 얘를 마지막으로 작성
    print('에러 발생 : ', err)
finally:
    print('에러 유무에 상관없이 반드시 수행')

print('프로그램 종료')    # 에러가 떨어지면 여길 안만남


