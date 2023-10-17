# 단순 서버 : 접속 상태 확인용으로 1개의 접속만 처리

from socket import *
serversock = socket(AF_INET, SOCK_STREAM)   # socket(소켓 종류, 소켓 유형)
serversock.bind(('127.0.0.1', 8888))    # tuple타입의 아규먼트 (호스트명, 포트번호)
serversock.listen(1)    # 클라이언트와 동시 연결 정보 수 (1 ~ 5)
print('서버 서비스 중........')

conn, addr = serversock.accept()    # 연결 대기(Blocking)
print('clent addr : ', addr)
print('from client message : ', conn.recv(1024).decode())
conn.close()    # client와 통신하는 socket
serversock.close()
