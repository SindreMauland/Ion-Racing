# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:54:50 2022

@author: trymr
"""

from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
MS_DELAY = 10


def progress():
    pb["value"]=c
#####################################################
#Speedometer vindu
speedometer = Tk(className="Speedometer")

speedometer.attributes('-fullscreen', True)

speedometer.configure(background='black')
#####################################################
#Tsal status

pb= ttk.Progressbar(
    speedometer,
    orient="vertical",
    mode="determinate",
    length=400)
pb.place(relx=0.05,rely=0.5)
x=0
a=0
b=0
c=0
def update():
    global x
    global a
    global b
    global c
    
    if x>100:
        Tsal = Label(bg="red", width=200, height=5)
        Tsal.place(relx=0.5,rely=0.07, anchor="n")
    if x<100:
        Tsal = Label(bg="green", width=200, height=5)
        Tsal.place(relx=0.5,rely=0.07, anchor="n")
    #Temperatur
    temperature1 = Label(text=b, font=("Century Gothic", 80), bg="black", fg="White")

    temperature1.place(relx=0.7, rely=0.9, anchor="sw")
    progress()
    #Batteri Status HV
    batteristatus = Label(text=b, font=("Century Gothic", 80), bg="black", fg="White")

    batteristatus.place(relx=0.8, rely=0.45, anchor="sw")
    
    #Batteri status 12v
    batteri12v = Label(text=b, font=("Century Gothic", 80), bg="black", fg="White")

    batteri12v.place(relx=0.8, rely=0.70, anchor="sw")
    
    
    speedometer.after(MS_DELAY, update)




#####################################################
#Hastighet
    speed_digits = Label(text=str(a), font=("Century Gothic", 320), bg="black", fg="White")
    
    speed_digits.place(relx=0.5, rely=0.45, anchor="center")





######################################################
#Temperature

temperature2 = Label(text="Temperatur", font=("Century Gothic", 50), bg="black", fg="#119ED9")

temperature2.place(relx=0.7, rely=0.97, anchor="sw")


######################################################
#Battery Status

    
batterihv = Label(text="HV", font=("Century Gothic", 50), bg="black", fg="#119ED9")

batterihv.place(relx=0.8, rely=0.30, anchor="sw")

batteri12v = Label(text="12V", font=("Century Gothic", 50), bg="black", fg="#119ED9")

batteri12v.place(relx=0.8, rely=0.55, anchor="sw")
 




######################################################
#Gasspådrag 

exit_button = Button(speedometer, text="Exit", command=speedometer.destroy)
exit_button.pack(pady=20)
speedometer.after(MS_DELAY, update)



speedometer.mainloop()
while True:
    x+=1