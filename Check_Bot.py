from tkinter import *
from PIL import Image, ImageTk

def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Check Mobile Botnet")
    root.configure(background="purple")
    
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    
    tele_device = tk.IntVar()
    tele_subscriber = tk.IntVar()
    abort = tk.IntVar()
    sendsms = tk.IntVar()
    delete_pack = tk.IntVar()
    sms_received = tk.IntVar()
    ljava = tk.IntVar()
    phone_s= tk.IntVar()
    readsms = tk.IntVar()
    boot_comp = tk.IntVar()
    io_delete = tk.DoubleVar()
    chown = tk.IntVar()
    chmod = tk.IntVar()
    mount = tk.IntVar()
    apk = tk.IntVar()
    zip_file = tk.DoubleVar()
    dex_file= tk.IntVar()
    camera = tk.IntVar()
    access = tk.IntVar()
    package = tk.IntVar()
    battery_low = tk.IntVar()
    so_file = tk.DoubleVar()
    power_connec = tk.IntVar()
    load_lib = tk.IntVar()
    exe_file = tk.IntVar()
    
    #===================================================================================================================
    def Detect():
        
        root = tk.Tk()
        root.geometry("800x850+250+5")
        root.title("Check Mobile Botnet")
        root.configure(background="gray")
        
        e1=tele_device.get()
        print(e1)
        e2=tele_subscriber.get()
        print(e2)
        e3=abort.get()
        print(e3)
        e4=sendsms.get()
        print(e4)
        e5=delete_pack.get()
        print(e5)
        e25=phone_s.get()
        print(e5)
        e6=sms_received.get()
        print(e6)
        e7=ljava.get()
        print(e7)
        e8=readsms.get()
        print(e8)
        e9=boot_comp.get()
        print(e9)
        e10=io_delete.get()
        print(e10)
        e11=chown.get()
        print(e11)
        e12=chmod.get()
        print(e12)
        e13=mount.get()
        print(e13)
        e14=apk.get()
        print(e14)
        e15=zip_file.get()
        print(e15)
        e16=dex_file.get()
        print(e16)    
        e17=camera.get()
        print(e17)
        e18=access.get()
        print(e18)
        e19=package.get()
        print(e19)
        e20=battery_low.get()
        print(e20)    
        e21=so_file.get()
        print(e21)
        e22=power_connec.get()
        print(e22)
        e23=load_lib.get()
        print(e23)
        e24=exe_file.get()
        print(e24)

        
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('botnet_MODEL.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5,e25, e6, e7, e8, e9,e10, e11, e12, e13,e14, e15, e16, e17, e18, e19, e20, e21, e22,e23, e24]])
        print(v)
        
        if v[0]==1:
            print("Yes")
            yes = tk.Label(root,text="Mobile Botnet Detected ",background="orange",foreground="black",font=('times', 20, ' bold '),width=18)
            yes.place(x=200,y=200)
            
            yes = tk.Label(root,text=" Project Accurecy is 95% . \n Botnets can also affect mobile phones \n and the bot which attacks a mobile.\n on the basis of dataset parameters detect the Mobile bot.",background="purple",foreground="black",font=('times', 20, ' bold '),width=40)
            yes.place(x=200,y=400)
                     
        else:
            print("No")
            no = tk.Label(root, text="No Mobile Botnet Detected", background="green", foreground="black",font=('times', 20, ' bold '),width=21)
            no.place(x=200, y=200)
            
            yes = tk.Label(root,text=" Project Accurecy is 95%.",background="green",foreground="black",font=('times', 20, ' bold '),width=21)
            yes.place(x=200,y=400)
            


    l1=tk.Label(root,text="Telephony Get Device ID",background="purple",font=('times', 20, ' bold '),width=20)
    l1.place(x=5,y=1)
    tele_device=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=tele_device)
    tele_device.place(x=400,y=1)

    l2=tk.Label(root,text="Telephony Get Subscriber ID",background="purple",font=('times', 20, ' bold '),width=22)
    l2.place(x=5,y=50)
    tele_subscriber=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=tele_subscriber)
    tele_subscriber.place(x=400,y=50)

    l3=tk.Label(root,text="Abort Broadcast",background="purple",font=('times', 20, ' bold '),width=20)
    l3.place(x=5,y=100)
    abort=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=abort)
    abort.place(x=400,y=100)
    
    l4=tk.Label(root,text="Send SMS",background="purple",font=('times', 20, ' bold '),width=20)
    l4.place(x=5,y=150)
    sendsms=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sendsms)
    sendsms.place(x=400,y=150)

    l5=tk.Label(root,text="Delete Packages",background="purple",font=('times', 20, ' bold '),width=20)
    l5.place(x=5,y=200)
    delete_pack=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=delete_pack)
    delete_pack.place(x=400,y=200)

    l6=tk.Label(root,text="Phone_State",background="purple",font=('times', 20, ' bold '),width=20)
    l6.place(x=5,y=250)
    phone_s=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=phone_s)
    phone_s.place(x=400,y=250)

    l7=tk.Label(root,text="SMS_Received",background="purple",font=('times', 20, ' bold '),width=20)
    l7.place(x=5,y=300)
    sms_received=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sms_received)
    sms_received.place(x=400,y=300)

    l8=tk.Label(root,text="Ljava.net.InetSocket Address",background="purple",font=('times', 20, ' bold '),width=25)
    l8.place(x=1,y=350)
    ljava=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=ljava)
    ljava.place(x=400,y=350)

    l9=tk.Label(root,text="Read_SMS",background="purple",font=('times', 20, ' bold '),width=20)
    l9.place(x=5,y=400)
    readsms=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=readsms)
    readsms.place(x=400,y=400)

    l10=tk.Label(root,text="Android.intent.action_Boot_completed",background="purple",font=('times', 20, ' bold '),width=28)
    l10.place(x=2,y=450)
    boot_comp=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=boot_comp)
    boot_comp.place(x=465,y=450)

    l11=tk.Label(root,text="IO.File.*delete",background="purple",font=('times', 20, ' bold '),width=20)
    l11.place(x=5,y=500)
    io_delete=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=io_delete)
    io_delete.place(x=400,y=500)

    l12=tk.Label(root,text="Chown",background="purple",font=('times', 20, ' bold '),width=20)
    l12.place(x=5,y=550)
    chown=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=chown)
    chown.place(x=400,y=550)

    l13=tk.Label(root,text="Chmod",background="purple",font=('times', 20, ' bold '),width=20)
    l13.place(x=5,y=600)
    chmod=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=chmod)
    chmod.place(x=400,y=600)


    l14=tk.Label(root,text="Mount",background="purple",font=('times', 20, ' bold '),width=20)
    l14.place(x=5,y=650)
    mount=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=mount)
    mount.place(x=400,y=650)

    l15=tk.Label(root,text=".APK",background="purple",font=('times', 20, ' bold '),width=20)
    l15.place(x=630,y=1)
    apk=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=apk)
    apk.place(x=950,y=1)

    l16=tk.Label(root,text=".ZIP",background="purple",font=('times', 20, ' bold '),width=20)
    l16.place(x=630,y=50)
    zip_file=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=zip_file)
    zip_file.place(x=950,y=50)

    l17=tk.Label(root,text=".DEX",background="purple",font=('times', 20, ' bold '),width=20)
    l17.place(x=630,y=100)
    dex_file=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=dex_file)
    dex_file.place(x=950,y=100)

    l18=tk.Label(root,text="Camera",background="purple",font=('times', 20, ' bold '),width=20)
    l18.place(x=630,y=150)
    camera=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=camera)
    camera.place(x=950,y=150)
    
    l19=tk.Label(root,text="Access_fine_location",background="purple",font=('times', 20, ' bold '),width=20)
    l19.place(x=630,y=200)
    access=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=access)
    access.place(x=950,y=200)

    l20=tk.Label(root,text="install_packages",background="purple",font=('times', 20, ' bold '),width=20)
    l20.place(x=630,y=250)
    package=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=package)
    package.place(x=950,y=250)

    l21=tk.Label(root,text="Android.intent.action.Battery_low",background="purple",font=('times', 20, ' bold '),width=25)
    l21.place(x=585,y=300)
    battery_low=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=battery_low)
    battery_low.place(x=1055,y=300)

    l22=tk.Label(root,text=".SO",background="purple",font=('times', 20, ' bold '),width=20)
    l22.place(x=630,y=350)
    so_file=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=so_file)
    so_file.place(x=950,y=350)

    l23=tk.Label(root,text="Android.intent.action.power_connected",background="purple",font=('times', 20, ' bold '),width=29)
    l23.place(x=580,y=400)
    power_connec=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=power_connec)
    power_connec.place(x=1055,y=400)
    
    l24=tk.Label(root,text="System.* Load Library",background="purple",font=('times', 20, ' bold '),width=20)
    l24.place(x=630,y=450)
    load_lib=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=load_lib)
    load_lib.place(x=950,y=450)

    l25=tk.Label(root,text=".EXE",background="purple",font=('times', 20, ' bold '),width=20)
    l25.place(x=630,y=500)
    exe_file=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=exe_file)
    exe_file.place(x=950,y=500)
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 19, ' bold '),width=8, bg="green", fg="white")
    button1.place(x=730,y=562)

    def window():
       root.destroy()
    
    exit = tk.Button(root, text="Exit", command=window, width=8, font=('times', 19, ' bold '),bg="red",fg="white")
    exit.place(x=880, y=562)
    
    root.mainloop()

Train()