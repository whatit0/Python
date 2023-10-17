# jikwon 테이블을 대상으로 사번과 이름을 입력(로그인)해 해당 자료가 있다면
# 해당 직원이 근무하는 부서 직원을 직급별 오름차순으로 모두 출력. 직급이 같으면 이름별 오름차순 출력
# 출력 형태 : 사번, 이름, 부서명, 직급, 성별
#             5   홍길동  총무부 대리  남
#          인원수 : * 명
# 다음으로 해당 직원이 관리하는 고객자료 출력
# 출력형태 : 고객번호 고객명 고객전화 나이
#             3    신기해  111-1111 23
#             관리 고객수 : *명
import MySQLdb
import pickle
with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def chul():
    try:
        conn = MySQLdb.connect(**config)
        #print(conn)
        cursor = conn.cursor()

        #buser_no = input('부서번호 입력 : ')
        jikwon_no = input('사번 입력 : ')
        jikwon_name = input('직원 이름 입력 : ')
        sql = '''
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen from jikwon 
        join buser on buser_num = buser_no  
        where buser_num = (select buser_num from jikwon where jikwon_no={0} and jikwon_name="{1}") 
        order by jikwon_jik, jikwon_name
        '''.format(jikwon_no, jikwon_name)
        # print(sql)
        cursor.execute(sql)
        datas = cursor.fetchall()
        print('사번, 이름, 부서명, 직급, 성별')
        for row in datas:
            print('%s %s %s %s %s' %row)
        print('인원수 : ', len(datas), '명')
        print()

        if len(datas) == 0:
            print(jikwon_name + '직원은 없어요')
            return  # sys.exit()도 가능

        sql = '''
        select gogek_no, gogek_name, gogek_tel, cast(2023 -((left(gogek_jumin, 2))+1900)as signed integer) from gogek 
        inner join jikwon on gogek_damsano = jikwon_no 
        where gogek_damsano = (select jikwon_no from jikwon where jikwon_no={0} and jikwon_name="{1}")
        '''.format(jikwon_no, jikwon_name)

        cursor.execute(sql)
        datas2 = cursor.fetchall()
        print('고객번호 고객명 고객전화 나이')
        for row2 in datas2:
            print('%s %s %s %s' % row2)
        print('인원수 : ', len(datas2), '명')

        if len(datas) == 0:
            print(jikwon_name + '은 담당 고객이 없어요')
            return  # sys.exit()도 가능

    except Exception as e:
        print('err : ', e)

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    chul()