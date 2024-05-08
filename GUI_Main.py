import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Mobile Botnet Detection System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
####For background Image
img=ImageTk.PhotoImage(Image.open("slide.jpg"))

img2=ImageTk.PhotoImage(Image.open("slide3.jpg"))

img3=ImageTk.PhotoImage(Image.open("s1.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()


# img1 = Image.open('slide.jpg')
# img1 = img1.resize((w,h), Image.ANTIALIAS)
# logo_image1 = ImageTk.PhotoImage(img1)

# logo_label1 = tk.Label(root, image=logo_image1)
# logo_label1.image = logo_image1
# logo_label1.place(x=0, y=0)


label_l1 = tk.Label(root, text="___Mobile Botnet Detection System___",font=("Times New Roman", 30, 'bold'),
                    background="brown", fg="white", width=70, height=2)
label_l1.place(x=0, y=0)

# img = Image.open('clogo.jpg')
# img = img.resize((100,70), Image.ANTIALIAS)
# logo_image = ImageTk.PhotoImage(img)

# logo_label = tk.Label(root, image=logo_image)
# logo_label.image = logo_image
# logo_label.place(x=40, y=10)

# frame_alpr = tk.LabelFrame(root, text=" --Details-- ", width=200, height=200, bd=5, font=('times', 14, ' bold '),bg="grey")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=728, y=100)

# label_l2 = tk.Label(frame_alpr, text="___Mobile Botnet Detection System___ \n \n \n Android is now the most widespread mobile operating system \n \n \n worldwide.   Over the years the volume of malware targeting Android has continued to grow. \n \n This is because it is easier and more profitable for malware authors to target \n an operating system that is open-source, more prevalent, and does not restrict the installation of apps from any possible source.\n As a matter of fact, numerous families of malware apps that are  capable of infecting Android devices and \n turning them into malicious bots have been discovered in the wild.\n These Android bots may become part of a larger botnet that can be used to perform various types of attacks such as Distributed Denial of Service (DDoS) attacks, generation and distribution of Spam, Phishing attacks, click fraud, stealing login credentials or credit card details, etc.",font=("Times New Roman",15, 'bold'),width=50,
#                     background="grey", fg="white")
# label_l2.place(x=30, y=15) 





# def log():
#     from subprocess import call
#     call(["python","GUI_main.py"])
#     root.destroy()
    
def window():
  root.destroy()
  
  
def log():
    from subprocess import call
    call(["python","login.py"])
    root.destroy()

def register():
    from subprocess import call
    call(["python","register.py"])
    root.destroy()
    
    
button1 = tk.Button(root, text="LOGIN", command=log, width=12, height=1 ,  font=('times 15 bold underline'),bd=4, bg="white", fg="black")
button1.place(x=400, y=120)

button2 = tk.Button(root, text="REGISTER",command=register,width=12, height=1,font=('times 15 bold underline'), bd=4,bg="white", fg="black")
button2.place(x=600, y=120)

button4 = tk.Button(root, text="EXIT", command=window, width=12, height=1,font=('times 15 bold underline'),bd=4, bg="white", fg="black")
button4.place(x=800, y=120)


# button1 = tk.Button(frame_alpr, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="Black", fg="white")
# button1.place(x=150, y=110)

# button2 = tk.Button(frame_alpr, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
# button2.place(x=150, y=200)

# button3 = tk.Button(frame_alpr, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
# button3.place(x=150, y=300)


label_l1 = tk.Label(root, text="** Mobile Botnet Detection System @2023 By ___ **",font=("Times New Roman", 10, 'bold'),
                    background="black", fg="white", width=250, height=2)
label_l1.place(x=0, y=800)


root.mainloop()