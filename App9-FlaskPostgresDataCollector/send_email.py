from email.mime.text import MIMEText
import smtplib
import random
gil_1000=['pebble','arcana','wolf pelt','2000 gil','1 gil']
gil_10000=['20000 gil','5000 gil','random gambit']
gil_100000=['random technick','random magick','5000 gil','10000 gil','34000 gil']
gil_500000=['random grimoire','class specific chest','serpentarius','24000 gil','4 gil']
gil_1000000=['golden ticket','5x random loot','500000 gil','steingrat bow','zodiac spear','genji gloves','5 gil','class specific chest']

def send_email(email,gil):
    from_email='alexeipetronov@gmail.com'
    from_password='kmzway87aa'
    to_email=email
    
    if int(gil)<=1000:
        reward=random.choice(gil_1000)
    elif int(gil)<=10000:
        reward=random.choice(gil_10000)
    elif int(gil)<=100000:
        reward=random.choice(gil_100000)
    elif int(gil)<=500000:
        reward=random.choice(gil_500000)
    elif int(gil)<=1000000:
        reward=random.choice(gil_1000000)





    subject='Gacha Reward'
    message='Message sent from app 9. You gamble %s and your gacha reward is %s' % (gil,reward.title())

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
