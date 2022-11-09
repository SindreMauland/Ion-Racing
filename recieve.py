import can
import os
import keyboard
a = 0
def messages():
    can0 = can.interface.Bus(channel = "can0",bustype="socketcan")
    msg = can0.recv()

    if msg.arbitration_id == 584 or msg.arbitration_id ==248:
        m1 = msg.data.hex()[0:4]
        global a
        a = int(m1,16)/100
        print(a)
    else:
        print(msg)
    
 
        
  
    if msg is None:
        print("ingen beskjed")

os.system("sudo ifconfig can0 down")