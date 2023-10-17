# jikwon 테이블을 대상으로 사번과 이름을 입력(로그인)해 해당 자료가 있다면
# 해당 직원이 근무하는 부서 직원을 직급별 오름차순으로 모두 출력, 직급이 같다면 이름별 오름차순 출력
# 출력 형태 : 사번, 이름, 부서명, 직급, 성별
# 다음으로 해당 직원이 관리하는 고객 자료 출력
# 출력 형태 : 고객번호, 고객명, 고객전화, 나이
import MySQLdb
import pickle
with open('mydb.dat', 'rb') as obj:
    config = pickle.load(obj)


def start():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        jikwon_no = input('사번 입력:')
        jikwon_name = input('이름 입력:')
        sql = '''
                select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen from jikwon 
                join buser on buser_num = buser_no  
                where buser_num = (select buser_num from jikwon where jikwon_no={0} and jikwon_name="{1}") 
                order by jikwon_jik, jikwon_name
                '''.format(jikwon_no, jikwon_name)

        cursor.execute(sql)
        datas = cursor.fetchall()

        if len(datas) == 0:
            return
        for r in cursor:
            print(r[0], r[1], r[2], r[3], r[4])
        print('인원수 : ' + str(len(datas)))

        sql = '''
                select gogek_no, gogek_name, gogek_tel, cast(2023 -((left(gogek_jumin, 2))+1900)as signed integer) from gogek 
                inner join jikwon on gogek_damsano = jikwon_no 
                where gogek_damsano = (select jikwon_no from jikwon where jikwon_no={0} and jikwon_name="{1}")
                '''.format(jikwon_no, jikwon_name)

        cursor.execute(sql)
        datas2 = cursor.fetchall()

        print("\n-고객 정보-")
        if len(datas2) == 0:
            print(jikwon_name + '의 담당 고객은 없습니다')
            return
        for gogek_no, gogek_name, gogek_tel, gogek_jumin in datas2:
            print(gogek_no, gogek_name, gogek_tel, gogek_jumin)
        print('인원수 : ' + str(len(datas2)))

    except Exception as e:
        print("err : ", e)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    start()
