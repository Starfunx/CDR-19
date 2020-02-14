# coding: utf-8
import re
import serial
import matplotlib.pyplot as plt
# import time
import io

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM11'
ser.timeout = 1
ser.setDTR(False)
ser.open()
ser.reset_input_buffer()

p = re.compile(r'[-+]?\d+\.\d+')
p2 = re.compile(r'[a-zA-Z]')

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
sio.flush()

floats=[0,0]

line = sio.readline()
while line != '':
    line = sio.readline()
    print(line)
    floatsnm1 = floats
    floats = [float(i) for i in p.findall(line)]
    # print(floats)

    Letters = [i for i in p2.findall(line)]
    # print(Letters)



    plt.axis('equal')
    if len(floats) >= 2:
        plt.plot([floatsnm1[0],floats[0]],[floatsnm1[1],floats[1]],'k')
    plt.pause(0.001)
plt.show()
ser.close()             # close port
