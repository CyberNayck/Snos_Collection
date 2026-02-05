import requests
import time
import random
from fake_useragent import UserAgent

url = 'https://telegram.org/support'
ua = UserAgent()

yukino = 0

def send_complaint(text, contact):
    headers = {
        'User-Agent': ua.random
    }
    payload = {
        'text': text,
        'contact': contact
    }
    response = requests.post(url, data=payload, headers=headers)
    
    if response.status_code == 200:
        print("\33[92mЖалоба успешно отправлена\n Всего отправлено", yukino, "сообщений\33[0m")
    else:
        print("Произошла ошибка при отправке жалобы")

text = [
    "Hello, there is a complaint about the user @ClEDCTBEHIE_KOMITET, he uses the virtual number +79012561439, on his channel (https://t.me/PRICEKOMlTET) he violates the telegram rules, it is on this channel that services are sold: murder, de-anonymization, false impersonation of a victim , demolition of accounts, childish perversions! Please take action! it's outrageous! or I will be forced to contact the police.",
    "Hello, I want to complain about the user (ClEDCTBEHIE_KOMITET, id6813631931), he uses a virtual number: 79012561439, threatens with deanonymization and false feminization, there are also violations in his channel https://t.me/PRICEKOMlTET"
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
]

while True:
    yukino += 1
    chosen_text = random.choice(text)
    chosen_contact = random.choice(contact)
    send_complaint(chosen_text, chosen_contact)
    time.sleep(0)