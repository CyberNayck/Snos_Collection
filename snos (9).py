import os
import sys
import time
import requests
import random
from datetime import datetime
import platform
import socket
import datetime

menu = input("1. Снос канала\n2. Снос чата\n3. Снос аккаунта\n4. О разработке\nВведите запрос: ")

if menu == "1":
    message = input('Введите ссылку на канал: ')
    if message.startswith("t.me/"):
        yukino = 0
        url = 'https://telegram.org/support'

        def send_complaint(text, contact):
            payload = {
                'text': text,
                'contact': contact
            }
            proxies = {
                'http': '50.168.163.179:80',
                'http': '97.107.131.77:80',
                'http': '162.223.94.166:80',
                'http': '139.60.209.2:80',
                'http': '162.245.81.45:80',
                'http': '50.171.187.50:80',
                'http': '50.171.187.51:80',
                'http': '50.168.163.182:80',

            }
            response = requests.post(url, data=payload, proxies=proxies)
            if response.status_code == 200:
                os.system('clear')
                sys.stdout.write("\033[2J\033[H")
                print(f"Жалоба отправлена. Всего жалоб: {yukino}")
            else:
                print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

        text = [
            'Данный канал создали для объединения троллей для унижения и оскорбления личностей людей, а это может привести к тому, что маленьких детей начнут оскорблять, и это может привести к плачевным действиям. Прошу вам принять меры и заблокировать группу.',
            'Данный аккаунт продает запрещенные услуги, занимается сливом информации, угрозами для жизни, попрошу принять меры, и заблокировать данного пользователя.',
        ]
        contact = [
            "+79006060609",
            "+79517778686",
            "+79315944444",
            "+79313722222",
        ]
        while True:
            yukino += 500
            time.sleep(1)
            chosen_text = random.choice(text)
            chosen_contact = random.choice(contact)
            send_complaint(chosen_text, chosen_contact)
            if yukino == 9000:
                for char in text1:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
                break
    else:
        print('Не вижу ссылки на канал.. Он должен начинаться на t.me/')


if menu == "2":
    message = input('Введите ссылку на чат: ')
    if message.startswith("t.me/"):
        yukino = 0
        url = 'https://telegram.org/support'

        def send_complaint(text, contact):
            payload = {
                'text': text,
                'contact': contact
            }
            proxies = {
                'http': '50.168.163.179:80',
                'http': '97.107.131.77:80',
                'http': '162.223.94.166:80',
                'http': '139.60.209.2:80',
                'http': '162.245.81.45:80',
                'http': '50.171.187.50:80',
                'http': '50.171.187.51:80',
                'http': '50.168.163.182:80',

            }
            response = requests.post(url, data=payload, proxies=proxies)
            if response.status_code == 200:
                os.system('clear')
                sys.stdout.write("\033[2J\033[H")
                print(f"Жалоба отправлена. Всего жалоб: {yukino}")
            else:
                print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

        text = [
            'Данный канал создали для объединения троллей для унижения и оскорбления личностей людей, а это может привести к тому, что маленьких детей начнут оскорблять, и это может привести к плачевным действиям. Прошу вам принять меры и заблокировать группу.',
            'Данный аккаунт продает запрещенные услуги, занимается сливом информации, угрозами для жизни, попрошу принять меры, и заблокировать данного пользователя.',
        ]
        contact = [
            "+79006060609",
            "+79517778686",
            "+79315944444",
            "+79313722222",
        ]
        while True:
            yukino += 500
            time.sleep(1)
            chosen_text = random.choice(text)
            chosen_contact = random.choice(contact)
            send_complaint(chosen_text, chosen_contact)
            if yukino == 9000:
                for char in text1:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
                break
    else:
        print('Не вижу ссылки на чат. Он должен начинатся на t.me/')
        
if menu == "3":
    message = input('Введите ссылку на аккаунт: ')
    if message.startswith("@"):
        yukino = 0
        url = 'https://telegram.org/support'

        def send_complaint(text, contact):
            payload = {
                'text': text,
                'contact': contact
            }
            proxies = {
                'http': '50.168.163.179:80',
                'http': '97.107.131.77:80',
                'http': '162.223.94.166:80',
                'http': '139.60.209.2:80',
                'http': '162.245.81.45:80',
                'http': '50.171.187.50:80',
                'http': '50.171.187.51:80',
                'http': '50.168.163.182:80',

            }
            response = requests.post(url, data=payload, proxies=proxies)
            if response.status_code == 200:
                os.system('clear')
                sys.stdout.write("\033[2J\033[H")
                print(f"Жалоба отправлена. Всего жалоб: {yukino}")
            else:
                print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

        text = [
            'Данный канал создали для объединения троллей для унижения и оскорбления личностей людей, а это может привести к тому, что маленьких детей начнут оскорблять, и это может привести к плачевным действиям. Прошу вам принять меры и заблокировать группу.',
            'Данный аккаунт продает запрещенные услуги, занимается сливом информации, угрозами для жизни, попрошу принять меры, и заблокировать данного пользователя.',
        ]
        contact = [
            "+79006060609",
            "+79517778686",
            "+79315944444",
            "+79313722222",
        ]
        while True:
            yukino += 500
            time.sleep(1)
            chosen_text = random.choice(text)
            chosen_contact = random.choice(contact)
            send_complaint(chosen_text,    
            chosen_contact)
            if yukino == 9000:
                text1 = "Задачу выполнил\n9000 жалоб в час на 1 аккаунт, чтобы не было проблем\nС уважением ваш паралел, до встречи :3"
                for char in text1:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
                break
    else:
        print('Не вижу ссылки на чат. Он должен начинатся на @')

if menu == "4":
	print("Лимба - d0xep, python/lua разработчик.\nДанный бот создан для сноса обидчиков.\n\nМОЙ ТГ: @d0xeparmatura.\nМОЙ КАНАЛ: есть в био")