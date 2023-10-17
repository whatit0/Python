# 멀티 채팅 프로그램 : socket, thread 사용
# 클라이언트

import socket
import threading
import sys

# 파이썬의 표준 출력은 버퍼링이 됨
def handleMessage(socket):
    while True:
        data = socket.recv(1024)
        if not data:continue
        print(data.decode('utf-8'))
        # print(data.decode('utf-8'), flush=True)

sys.stdout.flush()  # 현재 버퍼에 저장된 내용을 출력 장치로 내보내고 버퍼를 비움 / 버퍼를 비우지 않으면 꽉 차서 메시지를 못받을수도 있음

name = input('채팅명 입력:')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('192.168.0.16', 5555))
cs.send(name.encode('utf-8'))

th = threading.Thread(target=handleMessage, args=(cs,))
th.start()

while True:
    msg = input()
    sys.stdout.flush()
    if not msg:continue
    cs.send(msg.encode('utf-8'))
cs.close()



