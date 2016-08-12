# -*-coding:utf-8 -*-
from socket import *
import sys
from threading import *
from time import ctime

# if len(sys.argv) < 3:
#     HOST = 'localhost'
#     PORT = 51423
# else:
#     HOST = sys.argv[1]
#     PORT = int(sys.argv[2])

BUFSIZ = 1024
HOST = 'localhost'
PORT = 51423
ADDR = (HOST, PORT)
USERNAME = 'CLIENT'


def handlesend(tcpCliSock):
    while True:
        msg = raw_input('> ')
        while not msg:
            msg = raw_input('Message Can Not be Empty! Enter Your Message Again, please:')

        # if msg == '.logout':
        #     tcpCliSock.close()
        send_data = '[{time}] From <{user}>: {msg}'.format(time=ctime(), user=USERNAME, msg=msg)
        tcpCliSock.send(send_data)
    tcpCliSock.close()

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

# 建立发送消息的线程
s = Thread(target=handlesend, args=[tcpCliSock])
s.setDaemon(1)
s.start()

while True:
    rdata = tcpCliSock.recv(BUFSIZ)
    print rdata
tcpCliSock.close()

