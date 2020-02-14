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


r_float = re.compile(r'[-+]?\d+\.\d+')
r_int = re.compile(r'[-+]?\d+')
p2 = re.compile(r'[a-zA-Z]')

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
sio.flush()

floats=[0,0]

line = sio.readline()
Nech = 1500
values = np.empty((Nech,6))
parsedint = np.empty((Nech,6*2+2))
print(values)

i=0
while line != '':
    line = sio.readline()
    # print(line)
    parsedValue = [float(i) for i in r_float.findall(line)]
    parsedValueInt = [int(i) for i in r_int.findall(line)]
    print(parsedValueInt)

    Letters = [i for i in p2.findall(line)]
    # print(Letters)
    values[i,0] = parsedValue[0]#mesureG
    values[i,1] = parsedValue[1]#mesureD
    values[i,2] = parsedValue[2]#commandeG
    values[i,3] = parsedValue[3]#commandeD
    values[i,4] = parsedValue[4]#consigneG
    values[i,5] = parsedValue[5]#consigneD
    parsedint[i,0] = parsedValueInt[12]
    parsedint[i,1] = parsedValueInt[13]
    i+=1
    if i==Nech:
        break;
    print(i)

ser.close()             # close port


# affichage
fig, axs = plt.subplots(2, 1, sharex=True)
axs[0].plot(values[:,0])
axs[0].plot(values[:,4])
axs[0].set_ylabel('vitesse G (mm.s^-1)')
axs[0].grid(True)

axs[1].plot(values[:,2])
axs[1].plot(parsedint[:,0])
axs[1].set_xlabel('time (ech)')
axs[1].set_ylabel('commande G')
axs[1].grid(True)
fig.tight_layout()



fig2, axs2 = plt.subplots(2, 1, sharex=True)
axs2[0].plot(values[:,1])
axs2[0].plot(values[:,5])
axs2[0].set_ylabel('vitesse D (mm.s^-1)')
axs2[0].grid(True)

axs2[1].plot(values[:,3])
axs2[1].plot(parsedint[:,1])
axs2[1].set_xlabel('time (ech)')
axs2[1].set_ylabel('commande D')
axs2[1].grid(True)
fig2.tight_layout()

plt.show()

np.save("Values6",values)
