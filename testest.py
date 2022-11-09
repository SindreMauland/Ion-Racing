import sys
import can
import os
import keyboard


while True:
    can0 = can.interface.Bus(channel = "can0",bustype="socketcan")
    msg = can0.recv()

    if msg.arbitration_id == 584 or msg.arbitration_id ==248:
        m1 = msg.data.hex()[0:4]
        sys.stdout.flush()
        a = int(m1,16)/100
        print(a)
    
        #print(msg)
    
 
        
  
    if msg is None:
        print("ingen beskjed")


os.system("sudo ifconfig can0 down")
    
    

