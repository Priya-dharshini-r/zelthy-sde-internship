import os
import smtplib

# setting up from email address and app-password
EMAIL_ADDRESS = "elenadamonstefan739@gmail.com"
EMAIL_PASSWORD = "nkjdogeksxshyahf"

# By using SMTP Class, call smtp gmail server and set port number set variable name as smtp 
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    
    # establishing secure connection with the server
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    subject = str(input("Subject? "))
    body = str(input("Body? "))
    to_email = str(input("Recipient? "))
    
    msg = f'Subject:{subject}\n\n {body}'
    
    smtp.sendmail('EMAIL_ADDRESS', to_email, msg)

print("Email Sent!")
