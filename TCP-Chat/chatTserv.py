# -*- coding: utf-8 -*-
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

# USERNAME = raw_input('Enter Your USERNAME, please:')
USERNAME = 'Server'

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from: ', addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)      # .recv(): receive stream that comes from TCP-Client
        print data
        # if not data:
        #     break
        msg = raw_input('> ')
        while not msg:
            msg = raw_input('Message Can Not be Empty! Enter Your Message Again, please> ')
        data = 'From {user}: {msg}'.format(user=USERNAME, msg=msg)
        tcpCliSock.send('[{time}] {data}'.format(time=ctime(), data=data))      # .send(): send response to TCP-Client

    tcpCliSock.close()

tcpSerSock.close()


