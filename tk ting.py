from tkinter import *

MS_DELAY = 50



root = Tk()

master = Toplevel()
root.geometry("200x200") 
master.geometry("200x200") 

a=0
string = "km/t"
mylabel = IntVar()
def update():
    global a
    a+=1
    x = str(a)+string
    mylabel.set(x)
    root.after(MS_DELAY, update)
def update1():
    global a
    a+=1
    x=str(a)+string
    mylabel.set(x)
    master.after(MS_DELAY, update)
 

def remove_master():
    master.withdraw()
    root.deiconify()
    root.after(MS_DELAY, update)
def remove_root():
    root.withdraw()
    master.deiconify()
    master.after(MS_DELAY, update1)



btn1 = Button(master,
             text ="Click to open a new window",
             command = remove_master)
btn = Button(root,
             text ="Click to open a new window",
             command = remove_root)
btn1.pack(pady = 10)
btn.pack(pady = 10)



    

lbl = Label(root, textvariable=mylabel)
lbl.pack(pady=10)
lbl = Label(master, textvariable=mylabel)
lbl.pack(pady=10)
remove_master()
root.after(MS_DELAY, update)
mainloop()