import socket
#获取本机电脑名
from util.log_util import logd

myname = socket.getfqdn(socket.gethostname(  ))
#获取本机ip
myaddr = socket.gethostbyname(myname)

def printIpInfo():
    print('-----------------------------')
    print("IP："+myaddr)
    print('-----------------------------')