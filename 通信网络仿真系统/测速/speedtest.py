# -*- coding: UTF-8 -*-

import time
import socket
import protocol

num = 0

def deal(c):
    byte = c.recv(2048)
    global num
    if byte:
        # 忽略全0数据
        if byte == '\x00'*len(byte):
            pass
        else:
            message = protocol.unpack(byte)
            num += 1
            print num,message

    # 保持连接
    return True

def server():
    host = '127.0.0.1'
    port = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    print 'waiting for connection...'
    c, addr = s.accept()
    print 'connected from:', addr

    is_connection = True
    while is_connection:
        is_connection = deal(c)

    s.close()


if __name__ == '__main__':
    server()
