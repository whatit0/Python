# thread의 활성화, 비활성화
import threading

bread_plate = 0     # 빵 접시 : 공유 자원
lock = threading.Condition()    # Lock을 위한 조건변수 / lock말고 condition을 사용 가능

class Maker(threading.Thread):
    def run(self):
        global bread_plate
        for _ in range(30):     # for 다음 변수 쓸 생각이 없다면 _를 사용한다
            lock.acquire()  # 공유 자원 충돌 방지 목적
            while bread_plate >= 10:
                print('빵 생산 초과로 대기')
                lock.wait()     # thread의 비활성화

            bread_plate += 1
            print('빵 생산 수 : ', bread_plate)
            lock.notify()  # thread의 활성화
            lock.release()  # lock 해제

class Consumer(threading.Thread):
    def run(self):
        global bread_plate
        for _ in range(30):
            lock.acquire()
            while bread_plate < 1:
                print('빵이 없어 기다림.........')
                lock.wait()

            bread_plate -= 1
            print('빵 소비 후 남은 수 : ', bread_plate)
            lock.notify()
            lock.release()


mak = []; con = []
for i in range(5):
    mak.append(Maker())

for i in range(5):
    con.append(Consumer())


for th1 in mak:
    th1.start()

for th2 in con:
    th2.start()

for th1 in mak:
    th1.join()
for th2 in con:
    th2.join()
print('프로그램 종료')