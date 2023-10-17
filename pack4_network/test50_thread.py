# Thread간 자원 공유 : 충돌 방지 - 동기화
import threading, time

g_count = 0     # 전역변수는 자동으로 thread의 공유 자원이 됨

lock = threading.Lock()

def threadCount(id, count):
    global g_count  # 전역변수
    for i in range(count):  # 지역변수
        lock.acquire()  # 임의의 스레드가 공유 자원 사용시 다른 스레드는 대기 상태가 됨 (중복 방지)
        print('id %s ==> count:%s, g_count:%s'%(id, i, g_count))
        g_count = g_count + 1
        lock.release()  # 대기 상태를 해제

for i in range(1, 6):
    threading.Thread(target=threadCount, args=(i, 5)).start()
    
time.sleep(1)
print('최종 g_count : ', g_count)
print('프로그램 종료')