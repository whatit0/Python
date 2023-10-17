# thread를 이용해 날짜 및 시간 출력
import time

now = time.localtime()
print(now)
print('오늘은 {0}년 {1}월 {2}일 {3}요일'.format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_wday))
print('현재 {0}시 {1}분 {2}초'.format(now.tm_hour, now.tm_min, now.tm_sec))  # 월:0 ~ 일:6

print('-------------------------')
import threading

def calender_show():
    now = time.localtime()
    print('오늘은 {0}년 {1}월 {2}일 {3}요일'.format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_wday))
    print('현재 {0}시 {1}분 {2}초'.format(now.tm_hour, now.tm_min, now.tm_sec))  # 월:0 ~ 일:6

def myRun():
    while True:
        now2 = time.localtime()
        if now2.tm_min == 48:break
        calender_show()
        time.sleep(1)

# th = threading.Thread(target=calendar_show)
th = threading.Thread(target=myRun)
th.start()

th.join()