# coding: utf-8
import serial
import time
import io
from kbhit import *

def pos(x, y):
    return '\x1b['+ str(y)+';'+str(x)+'H'
def color(R,G,B):
    return '\x1B[38;2;'+str(R)+';'+str(G)+';'+str(B)+'m'

# serial communication parameters
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM8'
ser.timeout = 1
ser.setDTR(False)
ser.open()
ser.reset_input_buffer()

kb = KBHit()

line = ''
commandLine = ''

end = False
while not end:
    # print(commandLine,end='',flush = True)
    while kb.kbhit():
        c = kb.getch()
        if c:
            print(color(255,255,255)+c,end='',flush = True)
            if ord(c) == 27: # ESC
                end = True
            commandLine = commandLine + c
            if ord(c) == 13:
                commandLine = commandLine+'\n'
                ser.write(commandLine.encode('utf-8'))
                commandLine = ''

    c = ser.read().decode('utf-8')
    if c:
        line = line + c
        if c == '\n':
            print(color(250,10,0) + line, end='')
            # print(color(255,255,0)+pos(30,10)+line, end='')
            line = ''

        # c = ser.read().decode('utf-8')

kb.set_normal_term()
