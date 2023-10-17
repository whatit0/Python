# with 구문
# with 명령문 as 변수명: ~
# 어떤 블록에 진입하고 나올 때 지정된 객체(context manager)로 하여금 그 시작과 끝에서 어떤 처리를 할 수 있다.
# file i/o에서 with문을 사용하면 close()를 자동으로 해준다.

try:
    # 파일로 저장하기
    with open('test38.txt', 'w', encoding='utf-8') as obj1:
        obj1.write('파이썬으로 문서 저장\n')
        obj1.write('with 구문을 사용\n')
        obj1.write('명시적으로 close()를 할 필요 없다')
    print('저장 성공')

    # 파일 읽기
    with open('test38.txt', 'r', encoding='utf-8') as obj2:
        print(obj2.read())

except Exception as e:
    print('파일 처리 오류 : ', e)


print('\n피클링(일반 객체 및 복합 객체 file i/o) - object type으로 저장')
import pickle   # pickle을 사용 시 객체들을 파일로 저장할 수 있다
try:
    dictData = {'tom':'111-1111', '길동':'222-2222'}  # 일반 객체
    listData = ['파이썬', '자바']    # 일반 객체
    tupleData = (dictData, listData)    # 복합 객체
    print(tupleData)

    print('--------------')
    with open('hello.obj', mode='wb') as f1:   # write bindary / bind로 저장하기 때문에 txt 사용x
        pickle.dump(tupleData, f1)  # 저장은 dump, 읽기는 load
        pickle.dump(listData, f1)
    print('피클을 이용한 객체 저장')

    print('--읽기--------')   # first in first out / FIFO 구조
    with open('hello.obj', mode='rb') as f2:
        a, b = pickle.load(f2)
        print(a)
        print(b)
        c = pickle.load(f2)
        print(c)

except Exception as e:
    print('파일 처리 오류2 : ', e)