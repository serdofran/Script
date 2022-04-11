#Give the memory use
#free the memory stop non used process

from __future__ import print_function
import psutil


import os


print('memory_manager starting')
#os.system('free -g')
msg=""
"""print(psutil.cpu_percent())
print(psutil.virtual_memory())  # physical memory usage"""
print('memory % used:', psutil.virtual_memory()[2])
def popupmsg(msg, title):
    root = tk.Tk()
    root.title(title)
    label = ttk.Label(root, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(root, text="Okay", command = root.destroy)
    B1.pack()
    popup.mainloop() 

def wait_minute():
    import time
   # os.system('pkill -f Memorymanager.py')
    time.sleep(60);
    #Attendre 10 minute pour reprendre
    os.system('python Memorymanager.py')
def memory_warning():
    if(psutil.virtual_memory()[2]>=75):

        try:
            from tkinter import messagebox
            messagebox.showinfo(title="Memory_manager", message="memory low")
            exit
            


            
        except:
            print("An installation of python-tk occurred") 
            os.system('sudo apt-get install python-tk')

    else :
        import time
        time.sleep(10)
        os.system('python Memorymanager.py')


        


        
       


""" pid = os.getpid()
python_process = psutil.Process(pid)
memoryUse = python_process.memory_info()[0]/2.**30  # memory use in GB...I think
print('memory use:', memoryUse) """
memory_warning()
wait_minute()



#popupmsg(msg, title)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
#en background


