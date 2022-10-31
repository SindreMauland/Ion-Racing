import os
import can
from can import Message



os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')

can0= can.interface.Bus(channel= 'can0', bustype = 'socketcan')

while True:
    
    msg= can0.recv(1.0)
    print(msg.data())

    try:
        i=msg.ID
        print(i)
    except AttributeError:
        pass
    print(type(msg))
    if msg is None:
        
        print ('Ingen beskjed')
        
os.system('sudo ifconfig can0 down')
