# 서버 서비스 계속 유지
import socket
import sys

HOST = '192.168.0.22'
PORT = 7878

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversock.bind((HOST, PORT))
    serversock.listen(5)
    print('서버 서비스 진행 중.........')

    while True:
        conn, addr = serversock.accept()
        print('client info : ', addr[0], addr[1])
        print(conn.recv(1024).decode())     # 메시지 수신 후 출력

        # 메시지 송신
        conn.send(('from server : ' + str(addr[1]) + ' 서버가 전송함').encode('utf-8'))

except socket.error as err:
    print('err : ', err)
    sys.exit()
finally:
    pass