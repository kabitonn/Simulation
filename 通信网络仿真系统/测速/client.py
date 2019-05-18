# -*- coding: UTF-8 -*-



import time

import socket

import protocol





def senddata(s):

    data = {

        '1': 1,

        '2': 2.22,

        '3': 3.33,

        '4': 4.44,

        '5': 5.55,

        '6': 6.66,

        '7': 7.77,

        '8': 8.88,
        '9': 1.11,

        '10': 2.22,

        '11': 3.33,

        '12': 4.44,

        '13': 5.55,

        '14': 6.66,

        '15': 7.77

        

    }

    byte = protocol.pack(**data)

    s.send(byte)



def sendempty(s):

    data = {

        '1': 0,

        '2': 0,

        '3': 0,

        '4': 0,

        '5': 0,

        '6': 0,

        '7': 0,

        '8': 0,
        '9': 1.11,

        '10': 2.22,

        '11': 3.33,

        '12': 4.44,

        '13': 5.55,

        '14': 6.66,

        '15': 7.77

    }

    byte = protocol.pack(**data)

    s.send(byte)





def client():

    host = '192.168.5.6'

    port = 8888



    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))



    # 发送间隔

    interval = 0.001

    for x in range(0,100000):

        for i in range(0,5):

            time.sleep(interval)

            sendempty(s)

        time.sleep(interval)

        senddata(s)

        for i in range(0,5):

            time.sleep(interval)

            sendempty(s)



    s.close()



if __name__ == '__main__':

    client()