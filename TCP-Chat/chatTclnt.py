from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

# USERNAME = raw_input('Enter Your Username, please:')
USERNAME = 'Client'

while True:
    msg = raw_input('> ')      # data: Stream that will send to TCP-Server
    while not msg:
        msg = raw_input('Message Can Not be Empty! Enter Your Message Again, please> ')
    data = 'From {user}: {msg}'.format(user=USERNAME, msg=msg)
    tcpCliSock.send('[{time}] {data}'.format(time=ctime(), data=data))       # .send(): send Stream to TCP-Server
    data = tcpCliSock.recv(BUFSIZ)      # .recv(): receive response from TCP-Server
    # if not data:
    #     break
    print data

tcpCliSock.close()
