from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,roc_curve

root = tk.Tk()
root.title("Mobile Botnet Detection System")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open('imgbot1.jpg')

image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image



background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="__Mobile Botnet Detection System___", font=('times', 35,' bold '), height=1, width=60,bg="green",fg="Black")
lbl.place(x=0, y=0)



# frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=300, height=400, bd=5, font=('times', 14, ' bold '),bg="#808080")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=50, y=200)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv("new1.csv")



data = data.dropna()

le = LabelEncoder()
data['TelephonyManager.*getDeviceId'] = le.fit_transform(data['TelephonyManager.*getDeviceId'])

data['TelephonyManager.*getSubscriberId'] = le.fit_transform(data['TelephonyManager.*getSubscriberId'])
data['abortBroadcast'] = le.fit_transform(data['abortBroadcast'])
data['SEND_SMS'] = le.fit_transform(data['SEND_SMS'])
data['DELETE_PACKAGES'] = le.fit_transform(data['DELETE_PACKAGES'])
data['PHONE_STATE'] = le.fit_transform(data['PHONE_STATE'])
data['RECEIVE_SMS'] = le.fit_transform(data['RECEIVE_SMS'])
data['Ljava.net.InetSocketAddress'] = le.fit_transform(data['Ljava.net.InetSocketAddress'])
data['READ_SMS'] = le.fit_transform(data['READ_SMS'])
data['android.intent.action.BOOT_COMPLETED'] = le.fit_transform(data['android.intent.action.BOOT_COMPLETED'])
data['io.File.*delete('] = le.fit_transform(data['io.File.*delete('])
data['chown'] = le.fit_transform(data['chown'])
data['chmod'] = le.fit_transform(data['chmod'])
data['mount'] = le.fit_transform(data['mount'])
data['.apk'] = le.fit_transform(data['.apk'])
data['.zip'] = le.fit_transform(data['.zip'])
data['.dex'] = le.fit_transform(data['.dex'])
data['CAMERA'] = le.fit_transform(data['CAMERA'])
data['ACCESS_FINE_LOCATION'] = le.fit_transform(data['ACCESS_FINE_LOCATION'])
data['INSTALL_PACKAGES'] = le.fit_transform(data['INSTALL_PACKAGES'])
data['android.intent.action.BATTERY_LOW'] = le.fit_transform(data['android.intent.action.BATTERY_LOW'])
data['.so'] = le.fit_transform(data['.so'])
data['android.intent.action.ACTION_POWER_CONNECTED'] = le.fit_transform(data['android.intent.action.ACTION_POWER_CONNECTED'])
data['System.*loadLibrary'] = le.fit_transform(data['System.*loadLibrary'])
data['.exe'] = le.fit_transform(data['.exe'])    

data.head()

"""Feature Selection => Manual"""
x = data.drop(['ACCESS_NETWORK_STATE','BLUETOOTH','ACCESS_WIFI_STATE','BROADCAST_SMS','CALL_PHONE','CALL_PRIVILEGED','CLEAR_APP_CACHE','CLEAR_APP_USER_DATA','CONTROL_LOCATION_UPDATES','INTERNET','Result'], axis=1)


def Data_Preprocessing():
    data = pd.read_csv("new1.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['TelephonyManager.*getDeviceId'] = le.fit_transform(data['TelephonyManager.*getDeviceId'])

    data['TelephonyManager.*getSubscriberId'] = le.fit_transform(data['TelephonyManager.*getSubscriberId'])
    data['abortBroadcast'] = le.fit_transform(data['abortBroadcast'])
    data['SEND_SMS'] = le.fit_transform(data['SEND_SMS'])
    data['DELETE_PACKAGES'] = le.fit_transform(data['DELETE_PACKAGES'])
    data['PHONE_STATE'] = le.fit_transform(data['PHONE_STATE'])
    data['RECEIVE_SMS'] = le.fit_transform(data['RECEIVE_SMS'])
    data['Ljava.net.InetSocketAddress'] = le.fit_transform(data['Ljava.net.InetSocketAddress'])
    data['READ_SMS'] = le.fit_transform(data['READ_SMS'])
    data['android.intent.action.BOOT_COMPLETED'] = le.fit_transform(data['android.intent.action.BOOT_COMPLETED'])
    data['io.File.*delete('] = le.fit_transform(data['io.File.*delete('])
    data['chown'] = le.fit_transform(data['chown'])
    data['chmod'] = le.fit_transform(data['chmod'])
    data['mount'] = le.fit_transform(data['mount'])
    data['.apk'] = le.fit_transform(data['.apk'])
    data['.zip'] = le.fit_transform(data['.zip'])
    data['.dex'] = le.fit_transform(data['.dex'])
    data['CAMERA'] = le.fit_transform(data['CAMERA'])
    data['ACCESS_FINE_LOCATION'] = le.fit_transform(data['ACCESS_FINE_LOCATION'])
    data['INSTALL_PACKAGES'] = le.fit_transform(data['INSTALL_PACKAGES'])
    data['android.intent.action.BATTERY_LOW'] = le.fit_transform(data['android.intent.action.BATTERY_LOW'])
    data['.so'] = le.fit_transform(data['.so'])
    data['android.intent.action.ACTION_POWER_CONNECTED'] = le.fit_transform(data['android.intent.action.ACTION_POWER_CONNECTED'])
    data['System.*loadLibrary'] = le.fit_transform(data['System.*loadLibrary'])
    data['.exe'] = le.fit_transform(data['.exe'])    


    # data['AHD'] = le.fit_transform(data['AHD'])
    # print(data['Ca'])
    # data['Thal'] = le.fit_transform(data['Thal'])
    # print("thal Encoding")
    # data['ChestPain'] = le.fit_transform(data['ChestPain'])

    # data['Thal'] = le.fit_transform(data['Thal'])
    # data['ChestPain'] = le.fit_transform(data['ChestPain'])

    """Feature Selection => Manual"""
    x = data.drop(['ACCESS_NETWORK_STATE','BLUETOOTH','ACCESS_WIFI_STATE','BROADCAST_SMS','CALL_PHONE','CALL_PRIVILEGED','CLEAR_APP_CACHE','CLEAR_APP_USER_DATA','CONTROL_LOCATION_UPDATES','INTERNET','Result'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Result']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="blue",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=220, y=100)


def Model_Training():
    data = pd.read_csv("new1.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['TelephonyManager.*getDeviceId'] = le.fit_transform(data['TelephonyManager.*getDeviceId'])

    data['TelephonyManager.*getSubscriberId'] = le.fit_transform(data['TelephonyManager.*getSubscriberId'])
    data['abortBroadcast'] = le.fit_transform(data['abortBroadcast'])
    data['SEND_SMS'] = le.fit_transform(data['SEND_SMS'])
    data['DELETE_PACKAGES'] = le.fit_transform(data['DELETE_PACKAGES'])
    data['PHONE_STATE'] = le.fit_transform(data['PHONE_STATE'])
    data['RECEIVE_SMS'] = le.fit_transform(data['RECEIVE_SMS'])
    data['Ljava.net.InetSocketAddress'] = le.fit_transform(data['Ljava.net.InetSocketAddress'])
    data['READ_SMS'] = le.fit_transform(data['READ_SMS'])
    data['android.intent.action.BOOT_COMPLETED'] = le.fit_transform(data['android.intent.action.BOOT_COMPLETED'])
    data['io.File.*delete('] = le.fit_transform(data['io.File.*delete('])
    data['chown'] = le.fit_transform(data['chown'])
    data['chmod'] = le.fit_transform(data['chmod'])
    data['mount'] = le.fit_transform(data['mount'])
    data['.apk'] = le.fit_transform(data['.apk'])
    data['.zip'] = le.fit_transform(data['.zip'])
    data['.dex'] = le.fit_transform(data['.dex'])
    data['CAMERA'] = le.fit_transform(data['CAMERA'])
    data['ACCESS_FINE_LOCATION'] = le.fit_transform(data['ACCESS_FINE_LOCATION'])
    data['INSTALL_PACKAGES'] = le.fit_transform(data['INSTALL_PACKAGES'])
    data['android.intent.action.BATTERY_LOW'] = le.fit_transform(data['android.intent.action.BATTERY_LOW'])
    data['.so'] = le.fit_transform(data['.so'])
    data['android.intent.action.ACTION_POWER_CONNECTED'] = le.fit_transform(data['android.intent.action.ACTION_POWER_CONNECTED'])
    data['System.*loadLibrary'] = le.fit_transform(data['System.*loadLibrary'])
    data['.exe'] = le.fit_transform(data['.exe'])    

    """Feature Selection => Manual"""
    x = data.drop(['ACCESS_NETWORK_STATE','BLUETOOTH','ACCESS_WIFI_STATE','BROADCAST_SMS','CALL_PHONE','CALL_PRIVILEGED','CLEAR_APP_CACHE','CLEAR_APP_USER_DATA','CONTROL_LOCATION_UPDATES','INTERNET','Result'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Result']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=123)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
    
    import seaborn as sns
    rf_false_positive_rate,rf_true_positive_rate,rf_threshold = roc_curve(y_test,y_pred)
    
    sns.set_style('whitegrid')
    plt.figure(figsize=(10,5))
    plt.title('Reciver Operating Characterstic Curve')
    
    plt.plot(rf_false_positive_rate,rf_true_positive_rate,label='Support Vector Machine',color='red')  
    plt.plot([0,1],ls='--',color='blue')
    plt.plot([0,0],[1,0],color='green')
    plt.plot([1,1],color='green')
    plt.ylabel('True positive rate')
    plt.xlabel('False positive rate')
    plt.legend()
    plt.show()
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=420,y=190)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as botnet_MODEL.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=420,y=419)
    from joblib import dump
    dump (svcclassifier,"botnet_MODEL.joblib")
    print("Model saved as botnet_MODEL.joblib")



def call_file():
    import Check_Bot
    Check_Bot.Train()


def window():
    root.destroy()



button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2, bd=2)
button2.place(x=100, y=240)

button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training, width=15, height=2, bd=2)
button3.place(x=300, y=240)

button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Botnet Detection", command=call_file, width=15, height=2, bd=2)
button4.place(x=500, y=240)


exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=700, y=240)

# button4 = tk.Button(root, foreground="white", background="orange", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Train the Model", command=Model_Training, width=15, height=2, bd=2)
# button4.place(x=5, y=470)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''