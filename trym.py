from tkinter import *
from tkinter import ttk
import os
import can

MS_DELAY = 10
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
    
    


    #Gaspådrag
    pb['value']= torque_mcu

    ####################################################
    msg = can0.recv()

    if msg.arbitration_id == 256 or msg.arbitration_id ==100: #Errorcode battery
        print ('fault battety')

    elif msg.arbitration_id == 273 or msg.arbitration_id ==111: #Suspension POS
        print ()
    
    elif msg.arbitration_id == 274 or msg.arbitration_id ==112: #steering Wheel position
        print()

    elif msg.arbitration_id == 275 or msg.arbitration_id ==113: #RPM Wheel sensor
        global speed
        speed = int(msg.data.hex()[0:16],16)

    elif msg.arbitration_id == 512 or msg.arbitration_id ==200: #Data for battery
        print()

    elif msg.arbitration_id == 528 or msg.arbitration_id ==210: #MCU transmitt request
       
        mcu_data = int(msg.data.hex()[0:2],16)
        torque_mcu = (int(msg.data.hex()[2:6],16)+32766)/655.34
        print(mcu_data, ' Torquekomand MCU',torque_mcu)

    elif msg.arbitration_id == 584 or msg.arbitration_id ==248: #APPS/BSE gass og bremsepedal
        global speed1
        speed1.set(int(msg.data.hex()[0:4],16)/100)
        m2 = msg.data.hex()[8:12]
        global pedal_brems
        pedal_brems = int(m2,16)/100
        print('Gass:',pedal_gass, 'Brems: ', pedal_brems)
        pedal_gass= int(msg.data.hex()[0:4],16)/100
        
        if pedal_gass>=50:
            Tsal = Label(bg="red", width=200, height=5)
            Tsal.place(relx=0.5,rely=0.07, anchor="n")
        else:
            Tsal = Label(bg="green", width=200, height=5)
            Tsal.place(relx=0.5,rely=0.07, anchor="n")

    elif msg.arbitration_id == 594 or msg.arbitration_id == 252:
            m1= msg.data.hex()[0:4]
            global tempMotor
            tempMotor = int(m1, 16)/10
            m2 = msg.data.hex()[12:]
            global tempAir 
            tempAir = int(m2,16)/10
            print ('Temp motor: ',tempMotor, ' Temp lufta', tempAir)
            
    elif  msg.arbitration_id == 595 or msg.arbitration_id == 253:
        m1= msg.data.hex()[4:8]
        global tempEcu
        tempEcu = int(m1, 16)

    elif  msg.arbitration_id == 596 or msg.arbitration_id == 254: #Fault GND
        print() 

        
    elif msg is None:
        print("ingen beskjed")

    else:
        print(msg)
###############################################################
    #endrer veriene 
    '''
    global tempMotor1
    tempMotor1.set(int(tempMotor))
    global hv_verdi1
    hv_verdi1.set(int(hv_verdi))
    global verdi_12v1
    verdi_12v1.set(int(verdi_12v))

'''
    #Oppdaterer verdiene
    speedometer.update()
    speedometer.after(MS_DELAY, progress)



#Exit knapp for test
exit_button = Button(speedometer, text="Exit", command=speedometer.destroy)
exit_button.pack(pady=20)
speedometer.after(MS_DELAY, progress)



speedometer.mainloop()