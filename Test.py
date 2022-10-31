from tkinter import *
import os
import can
from testest import update
from tkinter import ttk
MS_DELAY = 10


def progress():

    from testest import a
    update()


    Tsal = Label(text=a ,bg="green", width=200, height=5)
    Tsal.place(relx=0.5,rely=0.07, anchor="n")
    speedometer.after(MS_DELAY, progress)
speedometer = Tk(className="Speedometer")


speedometer.configure(background='black')

    #####################################################
    #Speedometer vindu


    

speedometer.after(MS_DELAY, progress)



speedometer.mainloop()
