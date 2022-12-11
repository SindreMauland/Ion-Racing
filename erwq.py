from tkinter import *
from tkinter import ttk
import os
import can

MS_DELAY = 1
os.system("sudo ip link set can0 type can bitrate 500000")
os.system("sudo ifconfig can0 up")
can0 = can.interface.Bus(channel = "can0",bustype="socketcan")


    
#####################################################
#Speedometer vindu
speedometer = Tk(className="Speedometer")
speedometer.attributes('-fullscreen', True)
speedometer.configure(background='black')
#####################################################

speed= IntVar()
tempMotor=IntVar()
hv_verdi= IntVar()
verdi_12v=IntVar()

#Tsal status
s= ttk.Style()
s.configure( "green.Vertical.TProgressbar",troughcolor= 'blue', background= 'green',thickness= 200)
pb= ttk.Progressbar( speedometer,variable =speed, orient="vertical",mode="determinate",length=700, style= "green.Vertical.TProgressbar")

pb.place(relx=0.05,rely=0.25)

#TemperaturMotor 
temperature1 = Label(textvariable=tempMotor, font=("Century Gothic", 80), bg="black", fg="White")
temperature1.place(relx=0.7, rely=0.9, anchor="sw")


#Batteri Status HV
batteristatus = Label(textvariable=speed, font=("Century Gothic", 80), bg="black", fg="White")
batteristatus.place(relx=0.8, rely=0.45, anchor="sw")
  
#Batteri status 12v
batteri12v = Label(textvariable=speed, font=("Century Gothic", 80), bg="black", fg="White")
batteri12v.place(relx=0.8, rely=0.70, anchor="sw")
    
#Hastighet
speed_digits = Label(textvariable=speed, font=("Century Gothic", 320), bg="black", fg="White")
speed_digits.place(relx=0.4, rely=0.45, anchor="center")

    



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

def progress():
    
    


    #Gaspådrag


    ####################################################
    msg = can0.recv()

    if msg.arbitration_id == 256 or msg.arbitration_id ==100: #Errorcode battery
        print ('fault battety')




    elif msg.arbitration_id == 275 or msg.arbitration_id ==113: #RPM Wheel sensor
        speed1 =  int(msg.data.hex()[0:16],16)

    elif msg.arbitration_id == 512 or msg.arbitration_id ==200: #Data for battery
        print()



    elif msg.arbitration_id == 584 or msg.arbitration_id ==248: #APPS/BSE gass og bremsepedal
        speed.set(int(int(msg.data.hex()[0:4],16)/100))
        m2 = msg.data.hex()[8:12]
        
        pedal_brems = int(m2,16)/100

        pedal_gass= int(msg.data.hex()[0:4],16)/100
        
        if pedal_gass>=50:
            Tsal = Label(bg="red", width=200, height=5)
            Tsal.place(relx=0.5,rely=0.07, anchor="n")
        else:
            Tsal = Label(bg="green", width=200, height=5)
            Tsal.place(relx=0.5,rely=0.07, anchor="n")

    elif msg.arbitration_id == 594 or msg.arbitration_id == 252:
        
        tempMotor.set(int(int(msg.data.hex()[0:4],16)/10)) 
        
       
            
    elif  msg.arbitration_id == 595 or msg.arbitration_id == 253:
        m1= msg.data.hex()[4:8]
        tempEcu = int(m1, 16)

    elif msg.arbitration_id == 596 or msg.arbitration_id == 254: #Fault GND
        print()

    pb["value"]==speed



###############################################################
    #endrer veriene 

    '''
    global hv_verdi1
    hv_verdi1.set(int(hv_verdi))
    global verdi_12v1
    verdi_12v1.set(int(verdi_12v))
'''
    #Oppdaterer verdiene
    speedometer.update()
    speedometer.after(MS_DELAY, progress)




speedometer.after(MS_DELAY, progress)



speedometer.mainloop()