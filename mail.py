# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 01:37:29 2023

@author: admin
"""

import smtplib
from email.message import EmailMessage
import imghdr

Sender_Email = "pragati.code@gmail.com"
Reciever_Email = "pragati.sctcode@gmail.com"
Password ='grqheqzoutabdfzd'
newMessage = EmailMessage()    #creating an object of EmailMessage class
newMessage['Subject'] = "Test Email from Registration" #Defining email subject
newMessage['From'] = Sender_Email  #Defining sender email
newMessage['To'] = Reciever_Email  #Defining reciever email


import requests 
api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
        
import json
location_req_url='http://api.ipstack.com/103.51.95.183?access_key=a7003977af457525708100fca423928d'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)
        
lat = location_obj['latitude']
lon = location_obj['longitude']
latitude = lat
longitude = lon
print(str(latitude))
print(str(longitude))


newMessage.set_content('Registration are Successfully !') #Defining email body

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)
