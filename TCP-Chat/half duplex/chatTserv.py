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

print 'waiting for connection...'
tcpCliSock, addr = tcpSerSock.accept()
print '...connected from: ', addr
print 'Enter ".logout" to quit.'

while True:
    data = tcpCliSock.recv(BUFSIZ)      # .recv(): receive stream that comes from TCP-Client
    print data
    msg = raw_input('> ')
    while not msg:
        msg = raw_input('Message Can Not be Empty! Enter Your Message Again, please:')
    if msg == '.logout':
        break
    data_send = '[{time}] From <{user}>: {msg}'.format(time=ctime(), user=USERNAME, msg=msg)
    tcpCliSock.send(data_send)      # .send(): send response to TCP-Client

tcpCliSock.close()

tcpSerSock.close()


