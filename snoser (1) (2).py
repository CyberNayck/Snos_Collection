import random
import string
import pyfiglet
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import requests
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import ReportSpamRequest
from colorama import init, Fore, Style
from faker import Faker
from faker.providers import phone_number

init(autoreset=True)

senders = {'zlotema12@gmail.com': 'xxie yzkz wdyk ugxm',
'maybelox231@gmail.com': 'auov fern blju utwf',
'andeybirum@gmail.com': 'ouho uujv htlm rwaz',
'faverokstandof@gmail.com': 'nrsg kchi etta uuzh',
'faveroktt@gmail.com': 'dywo rgle jjwl hhbq',
'mksmksergeev@gmail.com': 'ycmw rqii rcbd isfd',
'maksimafanacefish@gmail.com': 'hdpn tbfp acwv jyro',
'bzdunovartur@gmail.com': 'zyzu fkge aqxw ufhv',
'apirsokov@gmail.com': 'aajc vpye buim ipgx'}

receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org', 'ceo@telegram.org']

class UserAgent:
    def __init__(self):
        pass

    def random(self):
        return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    print(Fore.CYAN + '████████╗███████╗██╗░░░░░███████╗██╗░░██╗██╗██╗░░░░░██╗░░░░░███████╗██████╗░')
    print(Fore.CYAN + '╚══██╔══╝██╔════╝██║░░░░░██╔════╝██║░██╔╝██║██║░░░░░██║░░░░░██╔════╝██╔══██╗')
    print(Fore.CYAN + '░░░██║░░░█████╗░░██║░░░░░█████╗░░█████═╝░██║██║░░░░░██║░░░░░█████╗░░██████╔╝')
    print(Fore.CYAN + '░░░██║░░░██╔══╝░░██║░░░░░██╔══╝░░██╔═██╗░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗')
    print(Fore.CYAN + '░░░██║░░░███████╗███████╗███████╗██║░╚██╗██║███████╗███████╗███████╗██║░░██║')
    print(Fore.CYAN + '░░░╚═╝░░░╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝')
    print(Fore.LIGHTCYAN_EX + "        • Program Fixed")
    print(Fore.LIGHTCYAN_EX + "        • By @ShredderNet")
    print(Fore.LIGHTRED_EX + "")
    print(Fore.LIGHTCYAN_EX + "   Меню")
    print(Fore.LIGHTCYAN_EX + "   1. Снос по почте " + Fore.LIGHTCYAN_EX + "[Status: " + Fore.LIGHTGREEN_EX + "Work" + Fore.LIGHTCYAN_EX + "]")
    print(Fore.LIGHTCYAN_EX + "   2. Снос через сайт " + Fore.LIGHTCYAN_EX + "[Status: " + Fore.LIGHTGREEN_EX + "Work" + Fore.LIGHTCYAN_EX + "]")
    print(Fore.LIGHTCYAN_EX + "   3. Снос через телеграм " + Fore.LIGHTCYAN_EX + "[Status: " + Fore.LIGHTRED_EX + "Unwork" + Fore.LIGHTCYAN_EX + "]")
    print(Fore.LIGHTCYAN_EX + "   4. Перезапуск програмы")

def handle_email(receivers, senders):
  subject = input(Fore.LIGHTCYAN_EX + "   Введите тему: " + Fore.RESET)
  body = input(Fore.LIGHTCYAN_EX + "   Введите текст: " + Fore.RESET)

  for receiver in receivers:
    for sender_email, sender_password in senders.items():
      success = send_email(receiver, sender_email, sender_password, subject, body)
      if success:
        print(Fore.LIGHTGREEN_EX + f"Жалоба отправлена на {receiver} от {sender_email}")
        break
      else:
        print(Fore.LIGHTRED_EX + f"Не удалось отправить email на {receiver} от {sender_email}")

def handle_web_complaint():
    url = 'https://telegram.org/support'
    user_agent = UserAgent()

    text = input(Fore.LIGHTCYAN_EX+ "   Введите текст жалобы: " + Fore.RESET)
    count = int(input(Fore.LIGHTCYAN_EX + "   Введите количество жалоб: " + Fore.RESET))

    def generate_russian_number():
        while True: 
            number = f"+79{random.randint(100000000, 999999999)}"
            if len(number) == 12:
                return number

    contact = [generate_russian_number() for _ in range(5000)]

    for _ in range(count):
        chosen_contact = random.choice(contact)
        send_web_complaint(url, text, chosen_contact, user_agent)
        time.sleep(0.01)

def handle_session_complaint():
    API_ID = '22622166'
    API_HASH = 'e4de2de0112314c46f74e98f4d050407'

    def send_telegram_complaint(channel_username, text):
        with TelegramClient('session', API_ID, API_HASH) as client:
            client.send_message(channel_username, text)
            client(ReportSpamRequest(channel_username))

    channel_username = input(Fore.LIGHTCYAN_EX + "   Введите username канала: " + Fore.RESET)
    text = input(Fore.LIGHTCYAN_EX + "   Введите текст жалобы: " + Fore.RESET)

    send_telegram_complaint(channel_username, text)
    print(Fore.LIGHTCYAN_EX + "Жалоба успешно отправлена!")

def send_email(receiver, sender_email, sender_password, subject, body):
  try:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver, msg.as_string())
    server.quit()
    return True
  except Exception as e:
    print(f"Ошибка при отправке с {sender_email}: {e}")
    return False

def send_web_complaint(url, text, contact, user_agent):
    headers = {
        'User-Agent': user_agent.random()
    }

    phone = "+79" + str(random.randint(100000000, 999999999))

    email = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)) + "@gmail.com"

    payload = {
        'message': text,
        'email': email,
        'phone': phone,
        'setln': 'en'
    }

    proxies = {
    'http': '103.111.22.26:58563',
    'http': '200.108.190.110:9800',
    'http': '88.255.64.83:1080',
    'http': '94.198.221.222:1080',
    'http': '91.192.81.137:58032',
    'http': '103.165.155.163:1111',
    'http': '162.214.90.49:59997',
    'http': '154.65.39.8:80',
    'http': '94.228.252.69:4153',
    'http': '114.231.8.117:8089',
    'http': '64.137.90.18:5638',
    'http': '72.10.164.178:14215',
    'http': '103.131.18.183:8080',
    'http': '103.131.19.43:8080',
    'http': '165.225.72.156:10089',
    'http': '162.214.90.49:34409',
    'http': '177.87.15.141:8081',
    'http': '212.31.100.138:4153',
    'http': '136.0.220.18:5398',
    'http': '136.226.232.125:11066',
    'http': '107.180.101.226:47757',
    'http': '95.111.227.164:20170',
    'http': '116.236.68.169:8800',
    'http': '50.63.13.3:50887',
    'http': '45.117.179.179:29647',
    'http': '109.95.207.24:33333',
    'http': '168.205.217.37:4145',
    'http': '80.191.46.59:1080',
    'http': '103.95.97.42:4153',
    'http': '181.13.198.90:4153',
    'http': '83.97.73.39:11817',
    'http': '178.79.165.164:35142',
    'http': '74.62.23.242:39593',
    'http': '103.51.21.250:83',
    'http': '131.161.238.14:51327',
    'http': '162.241.45.22:52048',
    'http': '190.109.72.17:33633',
    'http': '176.236.37.132:1080',
    'http': '103.209.176.76:32650',
    'http': '143.137.116.72:1080',
    'http': '103.154.112.34:35010',
    'http': '83.143.24.66:80',
    'http': '184.178.172.17:4145',
    'http': '51.79.87.144:41230',
    'http': '148.72.215.230:5483',
    'http': '123.154.24.179:8085',
    'http': '173.214.176.87:6058',
    'http': '87.116.144.229:4153',
    'http': '36.66.171.215:8080',
    'http': '13.232.82.215:8888',
    'http': '89.187.173.19:80',
    'http': '212.126.5.246:42344',
    'http': '51.158.76.35:16379',
    'http': '122.3.168.75:8080',
    'http': '181.48.155.78:8003',
    'http': '103.163.244.49:83',
    'http': '124.29.249.56:5678',
    'http': '104.129.192.167:8800',
    'http': '91.134.140.160:48949',
    'http': '69.49.246.155:59227',
    'http': '198.98.61.25:30907',
    'http': '51.83.155.89:3128',
    'http': '117.250.3.58:8080',
    'http': '116.99.239.57:24026',
    'http': '144.126.135.250:50040',
    'http': '38.9.113.164:8080',
    'http': '184.181.217.201:4145',
    'http': '174.64.199.82:4145',
    'http': '14.241.241.185:4145',
    'http': '170.78.92.98:5678',
    'http': '178.46.163.102:3128',
    'http': '67.213.212.51:55621',
    'http': '51.89.173.40:35077',
    'http': '64.202.186.2:31411',
    'http': '103.10.99.110:5678',
    'http': '36.64.214.50:1080',
    'http': '107.180.101.226:49590',
    'http': '45.188.164.47:999',
    'http': '154.65.39.7:80',
    'http': '189.79.62.116:8080',
    'http': '142.11.227.126:3128',
    'http': '103.153.134.20:8080',
    'http': '129.205.127.30:8080',
    'http': '193.34.237.241:1080',
    'http': '176.113.115.84:47237',
    'http': '147.124.212.31:24230',
    'http': '213.238.168.198:80',
    'http': '38.242.240.167:49923',
    'http': '124.158.182.34:7654',
    'http': '186.219.96.47:49923',
    'http': '103.204.55.221:1080',
    'http': '103.102.141.40:4145',
    'http': '98.162.25.7:31653',
    'http': '125.26.4.197:4145',
    'http': '98.188.47.132:4145',
    'http': '89.116.250.0:80',
    'http': '67.43.228.253:3721',
    'http': '199.102.104.70:4145',
    'http': '94.232.11.178:58028',
    'http': '176.236.163.36:59311',
    'http': '190.4.205.226:4153',
    'http': '212.220.13.98:4153',
    'http': '187.252.154.90:4153',
    'http': '198.204.241.50:17097',
    'http': '198.98.49.113:30228',
    'http': '190.94.212.222:999',
    'http': '166.0.235.142:5459',
    'http': '181.209.82.202:999',
    'http': '192.169.205.131:56355',
    'http': '184.178.172.5:15303',
    'http': '117.54.114.32:80',
    'http': '199.102.105.242:4145',
    'http': '176.98.248.2:4153',
    'http': '154.12.253.232:12263',
    'http': '192.163.202.88:53651',
    'http': '172.233.120.89:8000',
    'http': '177.184.67.33:4145',
    'http': '91.189.177.186:3128',
    'http': '89.145.162.81:3128',
    'http': '192.252.220.89:4145',
    'http': '185.217.198.121:4444',
    'http': '91.189.177.189:3128',
    'http': '185.105.91.62:4444',
    'http': '116.203.28.43:80',
    'http': '185.217.199.176:4444',
    'http': '51.89.14.70:80',
    'http': '60.188.102.225:18080',
    'http': '162.223.94.166:80',
    'http': '162.223.94.164:80',
    'http': '189.240.60.164:9090',
    'http': '67.43.227.228:1233',
    'http': '51.145.176.250:8080',
    'http': '182.61.38.114:82',
    'http': '72.10.164.178:25541',
    'http': '8.219.97.248:80',
    'http': '49.13.252.196:80',
    'http': '70.166.167.38:57728',
    'http': '36.111.186.194:3129',
    'http': '133.18.234.13:80',
    'http': '125.77.25.178:8080',
    'http': '185.105.90.88:4444',
    'http': '65.109.189.49:80',
    'http': '103.86.109.38:80',
    'http': '5.104.75.41:3128',
    'http': '167.102.133.106:80',
    'http': '67.43.227.227:23217',
    'http': '93.171.220.229:8888',
    'http': '65.108.126.45:3128',
    'http': '51.89.73.162:80',
    'http': '189.240.60.168:9090',
    'http': '84.252.74.190:4444',
    'http': '47.238.210.31:3128',
    'http': '110.80.140.213:443',
    'http': '116.114.20.148:3128',
    'http': '111.89.130.107:3128',
    'http': '217.26.67.57:3180',
    'http': '115.223.11.212:8103',
    'http': '154.203.132.49:8080',
    'http': '221.140.235.237:5002',
    'http': '47.91.65.23:3128',
    'http': '80.241.251.54:8080',
    'http': '58.246.58.150:9002',
    'http': '43.255.113.232:8083',
    'http': '123.30.154.171:7777',
    'http': '125.77.25.177:8080',
    'http': '103.101.205.143:8000',
    'http': '67.43.227.227:17579',
    'http': '116.63.129.202:6000',
    'http': '178.48.68.61:18080',
    'http': '152.26.229.88:9443',
    'http': '114.156.77.107:8080',
    'http': '8.213.151.128:3128',
    'http': '194.61.24.198:8080',
    'http': '103.215.207.65:83',
    'http': '170.239.205.113:999',
    'http': '185.232.169.108:4444',
    'http': '67.43.228.252:7551',
    'http': '91.189.177.188:3128',
    'http': '192.252.208.70:14282',
    'http': '164.163.42.5:10000',
    'http': '154.203.132.49:8090',
    'http': '111.1.61.62:3128',
    'http': '45.117.29.153:58080',
    'http': '103.17.90.6:5678',
    'http': '111.89.130.116:3128',
    'http': '72.10.160.170:31281',
    'http': '161.35.70.249:8080',
    'http': '34.92.250.88:11111',
    'http': '181.41.194.186:80',
    'http': '185.105.91.53:4444',
    'http': '34.92.250.88:10000',
    'http': '199.58.184.97:4145',
    'http': '67.43.227.229:32227',
    'http': '67.227.240.157:3128',
    'http': '190.103.177.131:80',
    'http': '51.210.19.141:80',
    'http': '35.185.196.38:3128',
    'http': '47.56.110.204:8989',
    'http': '190.95.202.210:999',
    'http': '120.194.4.157:5443',
    'http': '95.0.168.62:1981',
    'http': '199.167.236.12:3128',
    'http': '197.98.201.96:10672',
    'http': '124.105.24.80:8082',
    'http': '221.140.235.236:5002',
    'http': '47.251.70.179:80',
    'http': '120.194.4.157:82',
    'http': '183.215.23.242:9091',
    'http': '202.93.245.46:8080',
    'http': '38.54.71.67:80',
    'http': '67.43.227.227:30611',
    'http': '72.10.160.92:28423',
    'http': '201.77.108.21:999',
    'http': '72.10.164.178:18953',
    'http': '189.240.60.171:9090',
    'http': '200.24.131.125:999',
    'http': '114.143.0.177:80',
    'http': '67.43.236.20:32239',
    'http': '58.210.227.210:8088',
    'http': '62.162.90.212:80',
    'http': '189.240.60.163:9090',
    'http': '103.53.170.199:3128',
    'http': '178.217.168.164:55443',
    'http': '119.28.60.64:8090',
    'http': '188.132.209.245:80',
    'http': '47.89.184.18:3128',
    'http': '47.243.92.199:3128',
    'http': '84.252.73.132:4444',
    'http': '98.162.25.23:4145',
    'http': '125.99.106.250:3128',
    'http': '61.158.175.38:9002',
    'http': '173.21.8.226:3128',
    'http': '213.217.30.69:3128',
    'http': '114.129.2.82:8081',
    'http': '182.34.18.191:38801',
    'http': '213.252.245.221:6118',
    'http': '72.10.160.90:9307',
    'http': '103.191.155.70:8080',
    'http': '41.59.210.2:8080',
    'http': '31.43.63.70:4145',
    'http': '106.14.222.35:54245',
    'http': '107.180.92.72:24005',
    'http': '94.40.90.49:5678',
    'http': '192.162.232.15:1080',
    'http': '36.94.110.49:5678',
    'http': '93.190.138.24:20629',
    'http': '154.73.28.89:8080',
    'http': '110.232.67.44:55443',
    'http': '104.207.46.8:3128', #отсюда фаст проксе
    'http': '104.207.53.84:3128',
    'http': '104.207.39.99:3128',
    'http': '104.207.33.41:3128',
    'http': '104.207.54.180:3128',
    'http': '104.207.60.87:3128',
    'http': '104.207.52.3:3128',
    'http': '104.207.38.54:3128',
    'http': '104.207.49.185:3128',
    'http': '104.207.47.109:3128',
    'http': '104.207.58.55:3128',
    'http': '104.207.63.90:3128',
    'http': '104.207.57.125:3128',
    'http': '104.207.33.91:3128',
    'http': '104.167.29.118:3128',
    'http': '104.207.33.180:3128',
    'http': '104.167.28.242:3128',
    'http': '104.207.32.87:3128',
    'http': '104.207.53.34:3128',
    'http': '104.207.35.170:3128',
    'http': '104.207.43.211:3128',
    'http': '104.167.25.248:3128',
    'http': '104.207.39.34:3128',
    'http': '104.207.37.32:3128',
    'http': '104.167.31.248:3128',
    'http': '104.207.42.115:3128',
    'http': '104.207.54.78:3128',
    'http': '104.207.32.180:3128',
    'http': '104.207.49.145:3128',
    'http': '104.207.46.188:3128',
    'http': '104.207.56.140:3128',
    'http': '104.207.63.252:3128',
    'http': '104.207.47.215:3128',
    'http': '104.207.59.26:3128',
    'http': '104.207.46.37:3128',
    'http': '104.207.34.17:3128',
    'http': '104.207.61.46:3128',
    'http': '104.207.61.8:3128',
    'http': '104.167.24.61:3128',
    'http': '104.207.47.1:3128',
    'http': '104.207.58.98:3128',
    'http': '104.167.26.237:3128',
    'http': '104.207.41.56:3128',
    'http': '104.207.42.3:3128',
    'http': '104.207.61.148:3128',
    'http': '104.207.37.106:3128',
    'http': '104.167.31.56:3128',
    'http': '104.207.35.147:3128',
    'http': '104.207.39.160:3128',
    'http': '104.207.40.82:3128',
    'http': '104.207.47.155:3128',
    'http': '104.207.37.42:3128',
    'http': '104.207.50.29:3128',
    'http': '104.207.46.173:3128',
    'http': '104.207.51.144:3128',
    'http': '104.207.48.189:3128',
    'http': '104.167.28.213:3128',
    'http': '104.207.43.198:3128',
    'http': '104.207.51.109:3128',
    'http': '104.167.26.41:3128',
    'http': '104.167.24.19:3128',
    'http': '104.207.63.253:3128',
    'http': '104.167.25.222:3128',
    'http': '104.207.52.146:3128',
    'http': '104.167.29.113:3128',
    'http': '104.207.41.134:3128',
    'http': '104.207.49.50:3128',
    'http': '104.207.57.253:3128',
    'http': '104.207.35.215:3128',
    'http': '104.207.46.120:3128',
    'http': '104.207.53.49:3128',
    'http': '104.207.62.34:3128',
    'http': '104.207.60.228:3128',
    'http': '104.207.56.50:3128',
    'http': '104.207.56.51:3128',
    'http': '104.207.63.91:3128',
    'http': '104.207.32.71:3128',
    'http': '104.207.32.0:3128',
    'http': '104.207.63.195:3128',
    'http': '104.207.32.225:3128',
    'http': '104.167.31.138:3128',
    'http': '104.207.63.157:3128',
    'http': '104.167.25.79:3128',
    'http': '104.167.28.68:3128',
    'http': '104.167.29.227:3128',
    'http': '104.207.34.92:3128',
    'http': '104.207.41.153:3128',
    'http': '104.207.54.242:3128',
    'http': '104.207.42.117:3128',
    'http': '104.207.35.247:3128',
    'http': '104.207.35.129:3128',
    'http': '104.207.35.119:3128',
    'http': '104.207.45.194:3128',
    'http': '104.167.30.163:3128',
    'http': '104.207.42.96:3128',
    'http': '104.207.50.24:3128',
    'http': '104.167.31.189:3128',
    'http': '104.207.59.109:3128',
    'http': '104.207.41.54:3128',
    'http': '104.207.51.15:3128', #и до сюдо
    }

    try:
        response = requests.post(url, data=payload, headers=headers, proxies=proxies)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + f"<Updated TK> Жалоба успешно отправлена! Контакт: {contact}, Email: [{email}]")
        else:
            print(Fore.LIGHTRED_EX + "Произошла ошибка при отправке жалобы")
    except Exception as e:
        print(Fore.YELLOW + f"Что-то пошло не так: {e}")

def check_access_code():
    banner = pyfiglet.figlet_format("  TeleKiller - Auth")
    color_banner = Fore.LIGHTCYAN_EX + banner + Style.RESET_ALL
    print(color_banner)
    
    user_input = input(Fore.YELLOW + "Введите код доступа: " + Fore.RESET)
    access_codes = '111'
    if user_input in access_codes:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.LIGHTGREEN_EX + "Код доступа верный. Программа запущена.")
        return True
    else:
        print(Fore.LIGHTRED_EX + "Неверный код доступа. Программа завершает работу.")
        return False

def main():
    if check_access_code():
        while True:
            print_menu()
            choice = input(Fore.LIGHTCYAN_EX + "   Введите ваш выбор: " + Fore.RESET)

            if choice == "1":
                handle_email(receivers, senders)
            elif choice == "2":
                handle_web_complaint()
            elif choice == "3":
                handle_session_complaint()
            elif choice == "4":
                pass
            else:
                print(Fore.LIGHTRED_EX + "Неверный выбор. Пожалуйста, введите правильную опцию.")
            input(Fore.LIGHTCYAN_EX + "Нажмите Enter для продолжения...")
            print("\033c", end="")

if __name__ == "__main__":
    main()