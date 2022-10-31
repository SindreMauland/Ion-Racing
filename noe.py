
import os
import can
def start():
    f = open("log.txt","a+")
    g = open("log_0249.txt", "a+")
    os.system('sudo ip link set can0 type can bitrate 500000')
    os.system('sudo ifconfig can0 up')

    can0= can.interface.Bus(channel= 'can0', bustype = 'socketcan')


def recieve():
        f = open("log.txt","a+")
        g = open("log_0249.txt", "a+")
        can0= can.interface.Bus(channel= 'can0', bustype = 'socketcan')
        msg= can0.recv(1.0)
        if msg.arbitration_id == 0x0249:
        
            g.write(f"{msg},\n")

        print(msg)

        f.write(f"{msg},\n")
            

        if msg is None:
            
            print ('Ingen beskjed')
        f.close()
        g.close()
    
            
os.system('sudo ifconfig can0 down')