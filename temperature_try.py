from tkinter import *
from tkinter import ttk

MS_DELAY = 1




temperatures = Tk(className="Temperatures")
temperatures.attributes('-fullscreen', True)
temperatures.configure(background='black')


tempMotor=IntVar()
tempAir=IntVar()
tempColant= IntVar()
tempECU=IntVar()
tempMCU=IntVar()
tempBattery=IntVar()

#########################################
#Making the Labels
#########################################

#Temperatur Motor 
temp_Motor = Label(textvariable=tempMotor, font=("Century Gothic", 135), bg="black", fg="White")
temp_Motor.place(relx=0.01, rely=0.45, anchor="sw")
temp_Motor_label = Label(text="Temp Motor", font=("Century Gothic", 50), bg="black", fg="#119ED9")
temp_Motor_label.place(relx=0.01, rely=0.15, anchor="sw")

#Temperatur Batteri
temp_Battery = Label(textvariable=tempBattery, font=("Century Gothic", 135), bg="black", fg="White")
temp_Battery.place(relx=0.01, rely=0.95, anchor="sw")
temp_Battery_label = Label(text="Temp Battery", font=("Century Gothic", 50), bg="black", fg="#119ED9")
temp_Battery_label.place(relx=0.01, rely=0.65, anchor="sw")

#Temperatur ECU
temp_ECU = Label(textvariable=tempECU, font=("Century Gothic", 135), bg="black", fg="White")
temp_ECU.place(relx=0.36, rely=0.45, anchor="sw")
temp_ECU_label = Label(text="Temp ECU", font=("Century Gothic", 50), bg="black", fg="#119ED9")
temp_ECU_label.place(relx=0.38, rely=0.15, anchor="sw")

temp_Air = Label(textvariable=tempAir, font=("Century Gothic", 135), bg="black", fg="White")
temp_Air.place(relx=0.36, rely=0.95, anchor="sw")
temp_Air_label = Label(text="Temp Air", font=("Century Gothic", 50), bg="black", fg="#119ED9")
temp_Air_label.place(relx=0.38, rely=0.65, anchor="sw")

temp_Coolant = Label(textvariable=tempColant, font=("Century Gothic", 135), bg="black", fg="White")
temp_Coolant.place(relx=0.72, rely=0.45, anchor="sw")
temp_Coolant_label = Label(text="Temp Coolant", font=("Century Gothic", 50), bg="black", fg="#119ED9")
temp_Coolant_label.place(relx=0.65, rely=0.15, anchor="sw")

temp_MCU = Label(textvariable=tempMCU, font=("Century Gothic", 135), bg="black", fg="White")
temp_MCU.place(relx=0.72, rely=0.95, anchor="sw")
temp_MCU_label = Label(text="Temp MCU", font=("Century Gothic", 50), bg="black", fg="#119ED9")
temp_MCU_label.place(relx=0.70, rely=0.65, anchor="sw")

def temp_progress():
    tempMotor.set(10.5)
    tempAir.set(10.5)
    tempColant.set(20.5)
    tempECU.set(30.5)
    tempMCU.set(40.5)
    tempBattery.set(15.5)

    temperatures.update()
    temperatures.after(MS_DELAY, temp_progress)




temperatures.after(MS_DELAY, temp_progress)


temperatures.mainloop()