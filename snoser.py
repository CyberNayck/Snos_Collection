#@d0xeparmatura script
import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored

print("WORRRRRRK BY LIMBA. Спасибо за заказ :)")
device_name = socket.gethostname()
ip_address = socket.gethostbyname(device_name)
current_time = datetime.datetime.now()

url = 'https://telegram.org/support'
ua = UserAgent()

yukino = 0

def send_complaint(text, contact):
    headers = {
        'User-Agent': ua.random
    }
    payload = {
        'text': Добрый день!

Данный аккаунт @Cr1stal89 жертвы выполняет подозрительные действия в мессенджере. А именно создаёт каналы и чаты которые угрожают психике и здоровью человека. А раскручивает он эти каналы и чаты с помощью спам рассылок пользователям и в чаты. Прошу проверить данную информацию и принять меры к этому аккаунту.

Удачного времени суток!

        'contact': contact
    }
    
    proxies = {
    'http': '62.33.207.202:80',
    'http': '5.189.184.147:27191',
    'http': '50.221.74.130:80',
    'http': '172.67.43.209:80',
}
    
    response = requests.post(url, data=payload, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
        print(f"\33[92mЖалоба успешно отправлена\n Всего отправлено", yukino, "сообщений\33[0m")
    else:
        print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

text = [
    "",
]

contact = [
    "+79967285422",
    "+79269736273",
    "+79963668355",
    "+79661214909",
    "79254106650",
    "+22666228126",
    "+79269069196",
    "+79315894431",
    "+79621570718",
    "+79952741182"
    "+79997807271"
]

while True:
    yukino += @Cr1stal89
    chosen_text = random.choice(text)
    chosen_contact = random.choice(contact)
    send_complaint(chosen_text, chosen_contact)
    time.sleep(0)
