import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import datetime
from tqdm import tqdm
from time import sleep
import random
import socks
import socket
from fake_useragent import UserAgent
import random
from termcolor import colored



checkserver = input("Введите почтовый сервер (mail_ru, rambler, google, yahoo): ")

count = 0

ua = UserAgent()

def my_function():
    global count
    count += 1

def sendemail(senderemail, senderpassword, recipientemail, subject, messagetext):
    try:
        headers = {'User-Agent': ua.random}
        if checkserver == 'rambler':
        	
        	server = smtplib.SMTP('smtp.rambler.ru', 587)
        if checkserver =='google':
        	server = smtplib.SMTP('smtp.gmail.com', 587)
        if checkserver =='mail_ru':
        	server = smtplib.SMTP('smtp.mail.ru', 587)
        if checkserver =='yahoo':
        	server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server.starttls()

        server.login(senderemail, senderpassword)

        message = MIMEMultipart()
        message['From'] = senderemail
        message['To'] = recipientemail
        message['Subject'] = subject

        body = messagetext
        message.attach(MIMEText(body, 'plain'))

        server.send_message(message)
        now = datetime.datetime.now()
        print(now.strftime("%H:%M:%S"))
        my_function()
        print(f"\33[92mПисьмо от {senderemail} успешно отправлено на {recipientemail}\n Всего Отправлено", count, "сообщений\33[0m")

        server.quit()
    except Exception as e:
        print(colored(f"Ошибка при отправке письма: {str(e)}", "red"))

if checkserver =='rambler':
	senders = [ 
("edikabakumovskih96@rambler.ru", "KsrI4b6WlU"),
("romanmekesh95@rambler.ru", "vkRr15mM"),
("baklakovarsenii93@rambler.ru", "JgsXE1QD"),
("garikpyatyjkin88@rambler.ru", "DvIn72F4y"),
("anatoliisavkin1994@rambler.ru", "JxL39BgBvRd"),
("barilkinasara@rambler.ru", "WDy2j4kRK"),
("dmitriifidelskii@rambler.ru", "cBBCMK06Q"),
("boryasigalin1998@rambler.ru", "4a5dVodAQ"),
("muravyhsvetlana@rambler.ru", "5WLEF0jltlJ"),
("ekaterinastruchkova1994@rambler.ru" "2zLvDlmHejS"),
("tarusovgleb1991@rambler.ru", "98vJ7a8Q"),
("kseniyateregulova@rambler.ru", "F1EWeAJDz"),
("jidenkovanina@rambler.ru", "hD8a9oRIGuK"),
("chichernikovaevgeniya@rambler.ru", "c2STlnHL"),
("dulimovkirill97@rambler.ru", "1NXtYjIXLS"),
("halilulinbogdan99@rambler.ru", "rPCLdMxTu9f"),
("aleksandramelichkina1993@rambler.ru", "Sj60kFtS"),
("lyubomirzyurnyaev1989@rambler.ru", "04nLMoKv5j"),
("arturfilchkov93@rambler.ru", "ZEa7UpylAOH"),
]

if checkserver =='google':
	senders = [ 
("gmail@gmail.com", "password"),
]

if checkserver =='mail_ru':
	senders = [ 
("elirerdelm@mail.ru", "V0wMtM4uR"),
]

if checkserver =='yahoo':
	senders = [ 
("lauren.sanders27@yahoo.com", "lupoolovesyou"),
("nsbabyblues17@yahoo.com", "nikkiz17"),
("brendapondvt@yahoo.com", "harold"),
("shanerogersadi@yahoo.com", "shanerogers"),
]

recipients = [
"support@telegram.org", 
"dmca@telegram.org", 
"security@telegram.org", 
"sms@telegram.org", 
"info@telegram.org", 
"marta@telegram.org", 
"spam@telegram.org", 
"alex@telegram.org", 
"abuse@telegram.org", 
"pavel@telegram.org", 
"durov@telegram.org", 
"elies@telegram.org", 
"ceo@telegram.org", 
"mr@telegram.org", 
"levlam@telegram.org", 
"perekopsky@telegram.org", 
"recover@telegram.org", 
"germany@telegram.org", 
"hyman@telegram.org", 
"qa@telegram.org", 
"Stickers@telegram.org", 
"ir@telegram.org", 
"vadim@telegram.org", 
"shyam@telegram.org", 
"stopca@telegram.org", 
"u003esupport@telegram.org", 
"ask@telegram.org", 
"125support@telegram.org", 
"me@telegram.org", 
"enquiries@telegram.org", 
"api_support@telegram.org", 
"marketing@telegram.org", 
"ca@telegram.org", 
"recovery@telegram.org", 
"http@telegram.org", 
"corp@telegram.org", 
"corona@telegram.org", 
"ton@telegram.org", 
"sticker@telegram.org",
]

messages = [ # можешь написать и больше сообщений по аналогии
    "Hello, I want to complain about the user (@HEBIDIMblU, id6531158642), he uses a virtual number, threatens with deanonymization and false feminization, his channel with terrorist services: https://t.me/phobiadoxchat, as well as his channel with violations: @phob1axgod, where he posts child abuse, false mining, selling weapons and so on! please take action!"
    "hello, I want to complain about a user who clearly violates the telegram rules, his account @HEBIDIMblU - this user uses a virtual number, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action! Please! He also has his channel in his bio where he posts it all (violations), and he use virtual numberthere are also violations his channel with terrorist services: https://t.me/phobiadoxchat, as well as his channel with violations: https://t.me/phob1axgod, where he posts child abuse, false mining, selling weapons and so on! please take action",
    "hello, I want to complain about a user who clearly violates the telegram rules, his account @HEBIDIMblU, id6531158642 - this user uses a virtual number, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action! Please! He also has his channel in his bio where he posts it all (violations), and he use virtual number, there are also violations in his channel https://t.me/phob1axgod",
        "hello, @HEBIDIMblU - this user uses a virtual number, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action! Please! his channel with terrorist services: https://t.me/phobiadoxchat, as well as his channel with violations: https://t.me/phob1axgod, where he posts child abuse, false mining, selling weapons and so on! please take action",
            "hello,help me, I want to complain about a user who clearly violates the telegram rules, his account @HEBIDIMblU this user uses a virtual number, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action!",
]

subjects = [ # можешь написать и больше тем по аналогии
    "Report for User",
    "Reporting",
    "Help Please!",
    "Report User",
    "Report",
]

for senderemail, senderpassword in senders:
    for recipientemail in recipients:
        subject = random.choice(subjects)
        messagetext = random.choice(messages)
        sendemail(senderemail, senderpassword, recipientemail, subject, messagetext)
        time.sleep(0.
        ) # время задержки между сообщ в секундах