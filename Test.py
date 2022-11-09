from tkinter import *
import os
import can
from tkinter import ttk
import subprocess


MS_DELAY = 10


def progress():
    proc = subprocess.Popen('python /Users/sindremauland/Downloads/testest.py',
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            )
    output = proc.stdout.name
    Tsal = Label(text=output, bg="green", width=200, height=5)
    Tsal.place(relx=0.5, rely=0.07, anchor="n")
    speedometer.after(MS_DELAY, progress)


speedometer = Tk(className="Speedometer")


speedometer.configure(background='black')

#####################################################
# Speedometer vindu


speedometer.after(MS_DELAY, progress)


speedometer.mainloop()
