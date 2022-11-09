from tkinter import *
import os
import can
from tkinter import ttk
import subprocess
from recieve import messages
import os


os.system("sudo ip link set can0 type can bitrate 500000")
os.system("sudo ifconfig can0 up")
can0 = can.interface.Bus(channel = "can0",bustype="socketcan")


MS_DELAY = 10


def progress():
    messages()
    from recieve import a
    print(a)
    Tsal = Label(text=a, bg="green", width=200, height=5)
    Tsal.place(relx=0.5, rely=0.07, anchor="n")
    speedometer.after(MS_DELAY, progress)


speedometer = Tk(className="Speedometer")


speedometer.configure(background='black')

#####################################################
# Speedometer vindu


speedometer.after(MS_DELAY, progress)


speedometer.mainloop()
