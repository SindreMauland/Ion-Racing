from tkinter import *
import os
import can
from recieve import start
from tkinter import ttk
from recieve import messages
start()
os.system("sudo ip link set can0 type can bitrate 426328")
os.system("sudo ifconfig can0 up")

can0 = can.interface.Bus(channel = "can0",bustype="socketcan")
MS_DELAY = 100


def progress():


    messages()
    from recieve import a

    Tsal = Label(text=a ,bg="green", width=200, height=5)
    Tsal.place(relx=0.5,rely=0.07, anchor="n")
    speedometer.after(MS_DELAY, progress)
speedometer = Tk(className="Speedometer")


speedometer.configure(background='black')

    #####################################################
    #Speedometer vindu


    

speedometer.after(MS_DELAY, progress)



speedometer.mainloop()
