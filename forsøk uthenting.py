
#Henter ut og oversetter data fra bilen
import can
import os


def messages():
    can0 = can.interface.Bus(channel = "can0",bustype="socketcan")
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
        global mcu_data
        mcu_data = int(msg.data.hex()[0:2],16)
        global torque_mcu
        torque_mcu = (int(msg.data.hex()[2:6],16)+32766)/655.34
        print(mcu_data, ' Torquekomand MCU',torque_mcu)

    elif msg.arbitration_id == 584 or msg.arbitration_id ==248: #APPS/BSE gass og bremsepedal
        m1 = msg.data.hex()[0:4]
        global pedal_gass
        pedal_gass = int(m1,16)/100
        m2 = msg.data.hex()[8:12]
        global pedal_brems
        pedal_brems = int(m2,16)/100
        print('Gass:',pedal_gass, 'Brems: ', pedal_brems)

    elif msg.arbitration_id == 594 or msg.arbitration_id == 252:
            global tempMotor
            tempMotor = int(msg.data.hex()[4:8], 16)/10
            global tempAir 
            tempAir = int(msg.data.hex()[12:],16)/10
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
      
  

os.system("sudo ifconfig can0 down")