# coding: utf-8
import serial
import re
import io
import numpy as np
import matplotlib.pyplot as plt

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
Nech = 300
values = np.empty((Nech,6))
print(values)

i=0
while line != '':
    line = sio.readline()
    print(line)
    parsedValue = [float(i) for i in p.findall(line)]
    print(parsedValue)

    Letters = [i for i in p2.findall(line)]
    # print(Letters)
    values[i,0] = parsedValue[0]#alpha
    values[i,1] = parsedValue[1]#rho
    i+=1
    if i==Nech:
        break;
    print(i)

ser.close()             # close port


# affichage
fig, axs = plt.subplots(2, 1, sharex=True)
axs[0].plot(values[:,0])
axs[0].set_ylabel('linear')
axs[0].set_xlabel('time(ech)')
axs[0].grid(True)

axs[1].plot(values[:,1])
axs[1].set_ylabel('angular')
axs[1].set_xlabel('time(ech)')
axs[1].grid(True)
fig.tight_layout()

plt.show()
