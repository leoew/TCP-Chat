# -*- coding:utf-8 -*-
import socket
import traceback
from threading import *
from time import ctime

HOST = ''
PORT = 51423     # 监听所有的接口
USERNAME = 'SERVER'

# 建立套接字
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind((HOST, PORT))
tcpSerSock.listen(1)


# 接受消息的线程
def handlerecv(clientsock):
    print "New child", currentThread().getName()
    print "Got connection from", clientsock.getpeername()
    while True:
        data = clientsock.recv(4096)
        if not len(data):
            break
        print data
    clientsock.close()


# 发送消息的线程
def handlesend(clientsock):
    while True:
        msg = raw_input("> ")
        while not msg:
            msg = raw_input('Message Can Not be Empty! Enter Your Message Again, please:')

        # if msg == '.logout':
        #     clientsock.close()
        data_send = '[{time}] From <{user}>: {msg}'.format(time=ctime(), user=USERNAME, msg=msg)

        clientsock.sendall(data_send)
    # 关闭连接
    clientsock.close()

print 'wait for connection...'
print 'Enter ".logout" to quit.'
while True:
    try:
        tcpCliSock, addr = tcpSerSock.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    t = Thread(target=handlerecv, args=[tcpCliSock])
    t.setDaemon(1)
    t.start()

    r = Thread(target=handlesend, args=[tcpCliSock])
    r.setDaemon(1)
    r.start()
