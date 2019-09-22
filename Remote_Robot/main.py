import tkinter as tk
import serial
import re
import time

class positionFrame():
    def __init__(self, Frame, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        self.frame = tk.Frame(Frame, borderwidth = 2, relief = tk.GROOVE)

        self.label_x = tk.Label(self.frame , text = str(self.x), fg = 'navy')
        self.label_y = tk.Label(self.frame , text = str(self.y), fg = 'navy')
        self.label_theta = tk.Label(self.frame , text = str(self.theta), fg = 'navy')

    def pack(self):
        self.label_x.pack()
        self.label_y.pack()
        self.label_theta.pack()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Remote Robot Control")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
    # canvas
        self.subwindow_1 = tk.Frame(self.master, borderwidth = 2, relief = tk.GROOVE)
        self.subwindow_1.pack(side = tk.LEFT)

        self.canvas = tk.Canvas(self.subwindow_1, width=3200/3, height=2200/3, background='yellow')
        self.canvas.pack()

    #commands and infos
        self.subwindow_2 = tk.Frame(self.master, borderwidth = 2, relief = tk.GROOVE)
        self.subwindow_2.pack(side = tk.RIGHT)

        label_RobotPosition = positionFrame(self.subwindow_2, 0, 0, 0)
        label_RobotPosition.pack()

        #menu
        # self.menu = PanedWindow(self.master, orient=VERTICAL)


ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM9'
ser.timeout = 1
ser.setDTR(False)
ser.open()


line = ser.readline()
print(line.decode('utf-8'), end = '')
while line != None:
    line = ser.readline()
    print(line.decode('utf-8'), end = '')
ser.close()             # close port


# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()


# s = "X15.30 Y53.15, T3.1415"
#
# p = re.compile(r'\d+\.\d+')
# floats = [float(i) for i in p.findall(s)]
# print(floats)
#
# p2 = re.compile(r'[a-zA-Z]')
# Letters = [i for i in p2.findall(s)]
# print(Letters)
