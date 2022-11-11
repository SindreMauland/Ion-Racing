# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:54:50 2022

@author: trymr
"""

from tkinter import *
from tkinter import ttk
import os
import can
from recieve import messages

MS_DELAY = 150
os.system("sudo ip link set can0 type can bitrate 500000")
os.system("sudo ifconfig can0 up")
can0 = can.interface.Bus(channel = "can0",bustype="socketcan")


    
#####################################################
#Speedometer vindu
speedometer = Tk(className="Speedometer")
speedometer.attributes('-fullscreen', True)
speedometer.configure(background='black')
#####################################################

speed1= IntVar()
tempMotor1=IntVar()
hv_verdi1= IntVar()
verdi_12v1=IntVar()

#Tsal status

pb= ttk.Progressbar( speedometer,orient="vertical",mode="determinate",length=400)
pb.place(relx=0.05,rely=0.5)

#TemperaturMotor 
temperature1 = Label(textvariable=tempMotor1, font=("Century Gothic", 80), bg="black", fg="White")
temperature1.place(relx=0.7, rely=0.9, anchor="sw")


#Batteri Status HV
batteristatus = Label(textvariable=hv_verdi1, font=("Century Gothic", 80), bg="black", fg="White")
batteristatus.place(relx=0.8, rely=0.45, anchor="sw")
  
#Batteri status 12v
batteri12v = Label(textvariable=verdi_12v1, font=("Century Gothic", 80), bg="black", fg="White")
batteri12v.place(relx=0.8, rely=0.70, anchor="sw")
    
#Hastighet
speed_digits = Label(textvariable=speed1, font=("Century Gothic", 320), bg="black", fg="White")
speed_digits.place(relx=0.5, rely=0.45, anchor="center")

    



#Labler til verdiene 
######################################################
#TemperatureMotor
temperature2 = Label(text="Temperatur", font=("Century Gothic", 50), bg="black", fg="#119ED9")
temperature2.place(relx=0.7, rely=0.97, anchor="sw")

#Battery Status HV
batterihv = Label(text="HV", font=("Century Gothic", 50), bg="black", fg="#119ED9")
batterihv.place(relx=0.8, rely=0.30, anchor="sw")

#Battery Status 12V
batteri12v = Label(text="12V", font=("Century Gothic", 50), bg="black", fg="#119ED9")
batteri12v.place(relx=0.8, rely=0.55, anchor="sw")
 
#Gasspådrag
pb= ttk.Progressbar( speedometer,orient="vertical",mode="determinate",length=400)
pb.place(relx=0.05,rely=0.5)
def progress():
    messages()
    from recieve import tsal, torque_mcu, tempMotor, speed, hv_verdi, verdi_12v
    
    if tsal==1:
        Tsal = Label(bg="red", width=200, height=5)
        Tsal.place(relx=0.5,rely=0.07, anchor="n")
    else:
        Tsal = Label(bg="green", width=200, height=5)
        Tsal.place(relx=0.5,rely=0.07, anchor="n")

    #Gaspådrag
    pb['value']= torque_mcu

    #endrer veriene 
    global speed1
    speed1.set(int(speed))
    global tempMotor1
    tempMotor1.set(int(tempMotor))
    global hv_verdi1
    hv_verdi1.set(int(hv_verdi))
    global verdi_12v1
    verdi_12v1.set(int(verdi_12v))


    #Oppdaterer verdiene
    speedometer.update()
    speedometer.after(MS_DELAY, progress)



#Exit knapp for test
exit_button = Button(speedometer, text="Exit", command=speedometer.destroy)
exit_button.pack(pady=20)
speedometer.after(MS_DELAY, progress)



speedometer.mainloop()