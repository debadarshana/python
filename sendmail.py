# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 09:51:46 2017

@author: deb
"""

import smtplib
#open an smtp object
def send_mail():
    server = smtplib.SMTP_SSL('smtp.googlemail.com', 465) #create an SMTP object
    #server.starttls()
    server.login('papa90papa@gmail.com','papadipa@9093')
    sender='papa90papa@gmail.com'
    recver='papa90papa@gmail.com'
    msg ='Have a good day Deba'
    server.sendmail(sender,recver,msg)
    server.quit()

send_mail()
    
    
    