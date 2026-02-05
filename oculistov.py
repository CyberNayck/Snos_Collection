import colorama 
import pystyle
import time
from colorama import Fore, Back, Style
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print(Fore.GREEN + '''
MMm                    mMM      EEEEEEEEEEEEEEEEEEEEEEEE     TTTTTTTTTTTTTTTTTTTTTTTTTTT      EEEEEEEEEEEEEEEEEEEEEEEE       l
Mm m                  m mM      e                                       tttt                  e                              l 
Mm  m               m   mM      e                                       tttt                  e                              l
Mm   m            m     mM      e                                       tttt                  e                              l
Mm     m         m      mM      e                                       tttt                  e                              l
Mm       m     m        mM      e                                       tttt                  e                              l
Mm        m  m          mM      EEEEEEEEEEEEEEEEEEEEEEE                 tttt                  EEEEEEEEEEEEEEEEEEEEEEE        l
Mm          m           mM      EEEEEEEEEEEEEEEEEEEEEEE                 tttt                  EEEEEEEEEEEEEEEEEEEEEEE        l
Mm                      mM      e                                       tttt                  e                              l
Mm                      mM      e                                       tttt                  e                              l
Mm                      mM      e                                       tttt                  e                              l
Mm                      mM      e                                       tttt                  e                              l
Mm                      mM      e                                       tttt                  e                              l
Mm                      mM      EEEEEEEEEEEEEEEEEEEEEE                  tttt                  EEEEEEEEEEEEEEEEEEEEEEE        LLLLLLLLLLLLLLLLLL

https://t.me/metelmemory
 
      1. TG SNOS
''')

def rambler(subject, text, times):
    gmail_user = 'metelmemory602@gmail.com'
    gmail_password = 'blizzardDark.13'

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['Subject'] = subject
    body = text
    msg.attach(MIMEText(body, 'plain'))
    recipient_emails = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org','sticker@telegram.org','stopCA@telegram.org','recover@telegram.org','support@telegram.org','security@telegram.org',
'abuse@telegram.org' ,
'DMCA@telegram.org' ,
'qa@telegram.org',
'stopCA@telegram.org '
     ]
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 535)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        msg['To'] = ', '.join(recipient_emails)
        while times > 0:
            times = times - 1
            server.sendmail(gmail_user, recipient_emails, msg.as_string())
            print(f"Письмо успешно отправлено с почтового ящика gmail")
            time.sleep(60)
        
        server.close()
    except Exception as e:
        print('Что-то пошло не так при отправке писем:', e)


menu_pick = input(Fore.WHITE + "\nEnter number -> ")
if menu_pick == '1':
    subject = input('Email subject: ')
    print('Email text: ')
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    times = int(input('Times: '))
    rambler(subject, text, times)