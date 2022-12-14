from tkinter import *
from tkinter import ttk
import os
import can
MS_DELAY = 1


#####################################################
#Åpner CAN systemet 
os.system("sudo ip link set can0 type can bitrate 500000")
os.system("sudo ifconfig can0 up")
can0 = can.interface.Bus(channel = "can0",bustype="socketcan")
#####################################################

    
#####################################################
#Speedometer vindu
speedometer = Tk(className="Speedometer")
speedometer.attributes('-fullscreen', True)
speedometer.configure(background='black')
#####################################################

#####################################################
#temp vindu
temperatures = Tk(className="Temperatures")
temperatures.attributes('-fullscreen', True)
temperatures.configure(background='black')
#####################################################

 
#####################################################
#Variables
speed = IntVar()
hv_verdi = IntVar()
verdi_12v =IntVar()
torqueCommand = IntVar()
pedalGass = IntVar()
pedalBrems = IntVar()
#Temp variables 
tempMotor =IntVar()
tempAir = IntVar()
tempECU = IntVar()
tempMCU = IntVar()
tempCoolant = IntVar()
tempBattery = IntVar()
#####################################################





#Gasspådrag 
s= ttk.Style()
s.configure( "green.Vertical.TProgressbar",troughcolor= 'blue', background= 'green',thickness= 200)
pb= ttk.Progressbar( speedometer,variable =torqueCommand, orient="vertical",mode="determinate",length=700, style= "green.Vertical.TProgressbar")
pb.place(relx=0.05,rely=0.25)

#TemperaturMotor 
temperature1 = Label(textvariable=tempMotor, font=("Century Gothic", 80), bg="black", fg="White")
temperature1.place(relx=0.7, rely=0.9, anchor="sw")
temperature2 = Label(text="Temperatur", font=("Century Gothic", 50), bg="black", fg="#119ED9")
temperature2.place(relx=0.7, rely=0.97, anchor="sw")

#Batteri Status HV
batteristatus = Label(textvariable=speed, font=("Century Gothic", 80), bg="black", fg="White")
batteristatus.place(relx=0.8, rely=0.45, anchor="sw")
batterihv = Label(text="HV", font=("Century Gothic", 50), bg="black", fg="#119ED9")
batterihv.place(relx=0.8, rely=0.30, anchor="sw")  

#Batteri status 12v
batteri12v = Label(textvariable=speed, font=("Century Gothic", 80), bg="black", fg="White")
batteri12v.place(relx=0.8, rely=0.70, anchor="sw")
batteri12v = Label(text="12V", font=("Century Gothic", 50), bg="black", fg="#119ED9")
batteri12v.place(relx=0.8, rely=0.55, anchor="sw") 

#Hastighet
speed_digits = Label(textvariable=speed, font=("Century Gothic", 320), bg="black", fg="White")
speed_digits.place(relx=0.4, rely=0.45, anchor="center")

exit_button = Button(speedometer, text="Exit", command=speedometer.destroy)
exit_button.pack(pady=20)

#Leser fra Can og oppdaterer variablene 
def speedometer_progress():
    msg = can0.recv()

    if msg.arbitration_id == 256 or msg.arbitration_id ==100: #Errorcode battery
        print ('fault battety')


    elif msg.arbitration_id == 275 or msg.arbitration_id ==113: #RPM Wheel sensor
        speed1 =  int(msg.data.hex()[0:16],16)

    elif msg.arbitration_id == 512 or msg.arbitration_id ==200: #Data from battery
        print()

    elif msg.arbitration_id == 528 or msg.arbitration_id ==210: #MCU transmitt request
        if int(msg.data.hex()[0:2],16) == 144: #Kode for torque comand to MCU            
            if (msg.data.hex()[2:6],16)==0: 
                Tsal = Label(bg="green", width=200, height=5)#Setter TSAl som grønn
                Tsal.place(relx=0.5,rely=0.07, anchor="n")
            else:
                torqueCommand.set(int(abs(msg.data.hex()[2:6],16)-32766)/655.34)#sets the turque command, sendt to the ECU
                Tsal = Label(bg="red", width=200, height=5) #setter TSAL som rød 
                Tsal.place(relx=0.5,rely=0.07, anchor="n")
        
    elif msg.arbitration_id == 584 or msg.arbitration_id ==248: #APPS/BSE gass og bremsepedal
        pedalBrems.set(int(msg.data.hex()[8:12],16)/100)
        pedalGass.set(int(msg.data.hex()[0:4],16)/100)
        
    elif msg.arbitration_id == 594 or msg.arbitration_id == 252: 
        tempMotor.set(int(msg.data.hex()[0:4],16)/10) #sets the Motror temp
        tempAir.set(int(msg.data.hex()[12:],16)/10) #sets the Air temp 
            
    elif  msg.arbitration_id == 595 or msg.arbitration_id == 253: #ECU temp
        tempECU.set(int(msg.data.hex()[4:8], 16))#sets the ECU temp

    elif msg.arbitration_id == 596 or msg.arbitration_id == 254: #Fault GND
        print()
    try:
        pb["value"]==torqueCommand #setter pådrag verdien 
    except:
        pass



    #Oppdaterer verdiene
    speedometer.update()
    speedometer.after(MS_DELAY, speedometer_progress)

speedometer.after(MS_DELAY, speedometer_progress)
speedometer.mainloop()



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

temp_Coolant = Label(textvariable=tempCoolant, font=("Century Gothic", 135), bg="black", fg="White")
temp_Coolant.place(relx=0.72, rely=0.45, anchor="sw")
temp_Coolant_label = Label(text="Temp Coolant", font=("Century Gothic", 50), bg="black", fg="#119ED9")
temp_Coolant_label.place(relx=0.65, rely=0.15, anchor="sw")

temp_MCU = Label(textvariable=tempMCU, font=("Century Gothic", 135), bg="black", fg="White")
temp_MCU.place(relx=0.72, rely=0.95, anchor="sw")
temp_MCU_label = Label(text="Temp MCU", font=("Century Gothic", 50), bg="black", fg="#119ED9")
temp_MCU_label.place(relx=0.70, rely=0.65, anchor="sw")

def temp_progress():
    msg = can0.recv()

    if msg.arbitration_id == 256 or msg.arbitration_id ==100: #Errorcode battery
        print ('fault battety')

    elif msg.arbitration_id == 512 or msg.arbitration_id ==200: #Data from battery
        print()
                
    elif msg.arbitration_id == 594 or msg.arbitration_id == 252: 
        tempMotor.set(int(msg.data.hex()[0:4],16)/10) #sets the Motor temp
        tempAir.set(int(msg.data.hex()[12:],16)/10) #sets the Air temp 
            
    elif  msg.arbitration_id == 595 or msg.arbitration_id == 253: #ECU temp
        tempECU.set(int(msg.data.hex()[4:8], 16))#sets the ECU temp

    elif msg.arbitration_id == 596 or msg.arbitration_id == 254: #Fault GND
        print()

    temperatures.update()
    temperatures.after(MS_DELAY, temp_progress)




temperatures.after(MS_DELAY, temp_progress)


temperatures.mainloop()