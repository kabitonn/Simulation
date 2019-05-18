# -*- coding: UTF-8 -*-



import struct



protocol = {

    'keys': [str(i+1) for i in range(15)],

    'rule': 'Q14d'

}



def pack(**data):

    try:

        packet = tuple([data[key] for key in protocol['keys']])

        byte = struct.pack(protocol['rule'], *packet)

    except:

        print '[Packaging Error]'

    else:

        return byte



def unpack(byte):

    try:

        packet = struct.unpack(protocol['rule'], byte)

    except :

        print "[Unpacking Error]"

    else:

        return packet



if __name__ == '__main__':

    data = {

        '1': 1.11,

        '2': 2.22,

        '3': 3.33,

        '4': 4.44,

        '5': 5.55,

        '6': 6.66,

        '7': 7.77,

        '8': 8.88

    }



    data = {

        '1': 0,

        '2': 0,

        '3': 0,

        '4': 0,

        '5': 0,

        '6': 0,

        '7': 0,

        '8': 0

    }



    byte = pack(**data)

    print byte



    data = unpack(byte)

    print data



    if byte == '\x00'*64:

        pass



