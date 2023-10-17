# 키보드로 부서번호를 입력받아, 해당 부서의 자료 출력
import MySQLdb
import pickle

with open(r'mydb.dat', 'rb') as obj:
    config = pickle.load(obj)

def start():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        #print(cursor)

        buser_no = input('부서번호 입력:')
        #buser_no = '10'
        sql = '''
            select jikwon_no, jikwon_name, buser_num, jikwon_pay, jikwon_jik, jikwon_gen
            from jikwon
            where buser_num={0}
        '''.format(buser_no)
        cursor.execute(sql)
        datas = cursor.fetchall()
        #print(datas)
        #print(len(datas))

        if len(datas) == 0:
            print(buser_no + '번 부서는 없어요')
            return      # sys.exit()도 가능
        for jikwon_no, jikwon_name, buser_num, jikwon_pay, jikwon_jik, jikwon_gen in datas:
            print(jikwon_no, jikwon_name, buser_num, jikwon_pay, jikwon_jik, jikwon_gen)

        print('인원수 : ' + str(len(datas)))

    except Exception as e:
        print("err : ", e)

    finally:
        cursor.close()
        conn.close()

if __name__=='__main__':
    start()