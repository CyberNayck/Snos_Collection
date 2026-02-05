import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
#Parol

a=input("Введи пароль для запуска программы:")
if a!="сносер залупа":
    print("Пароль не верен! Программа завершает работу")
    print("Уточни его у создателя шуралоохэтотсносерхуйняебаннаякопипаста")
    time.sleep(5)
    exit()
else:
    print("Пароль верен! Программа начинает работу ")
#Otpraviteli jalob
senders = {
         'jdlodd@mail.ru': 'rcAxee0FtnzL0wf4qUuX',
           'mmardjela@mail.ru': '3fhUwHBWipHasch29fv0',
           'andrea.aalto@mail.ru': 'XJrFhNwPamYaz6mjJ6yT',
           'luca.velde@mail.ru': 'cEeCv1mtP8Y2fsL4F1Xf',
           'esolhov@mail.ru': 'HB3zF1mz1H7EDEfinhdi',
           'fdfsfg04@mail.ru': 'hSrWxzjRWBLDYuPAB60F',
           'amardjela@mail.ru': 'rmyndAbyj7e5gjg3queN',
           'mrashni@mail.ru': 'Gukjw4sbwCrgAgFaZzx1',
    'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
    'terbgebuoviror@mail.ru': 'gaqaKs06xg22kkXXW2LU',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
    'lovedel.anisss@mail.ru': 'cJkiz18MAWS0L85DGW8n',
           'love.efs@mail.ru': 'vzw5bwePbzeXhYhDeeA1',
           'fsadfsaf.sdfasdfas@mail.ru': 'KUN0wpJbViwpFXFPkHb4',
           'fkjvfmdsof@mail.ru': 'CxM2JUT0vx03aSyD53Ns',
           'sawage.dasha@mail.ru': 'SyfStmkgK29KUB0BQVAy',
           'opunm.sdaww@mail.ru': 'Y1BjSZCHeLTxmvaW49FH',
           'fall.gall@mail.ru': 'tFqTgMUqkidcBbw91hD7',
           'wzxcvd@mail.ru': 'vwPUnRUGW75MUKaFzhVc',
           'masha.mashala@mail.ru': 'rtM0rCSHZstDVQpxmEkh',
           'wwagege@mail.ru': 'ZZNkRLrZseLN57phVeEQ',
           'irigjfodjdkdkk@mail.ru': 'n8r0TKCygC5xqaWxStr1',
           'sdfghafdhg@mail.ru': 'Kag0fefn6mFWMzQ17PGb',
           'dasha.goat@mail.ru': '3bkf9iHyuFUfEfKzXYLm',
           'dasha.sasaas@mail.ru': 'UAVwCgpFXaD2zcQ9gVSE',
           'dasha.lovely.02@mail.ru': 'paUrCHANKWWxefzaQvQm',
           'dasha.butifull@mail.ru': '0bAbKQUfpVRDcrLtc0Ya',
           'firirotifigj@gmail.com': 'RQCgW8vb127AGRZ5Kvf1',
           'dasha.mdaaa@gmail.com': 'HXNg0M0bvyaEs1tbMjTB',
           'lfwgdg@mail.ru': 'h6hAUvp3KNPqqcmmduU3',
           'dasha.holle@mail.ru': '0g5g6kwEtkKw2hYCaSTj',
           'darya.holly@mail.ru': 'he02duEXu4iiDambB6ZG',
           'dasha.vonk@mail.ru': 'AayKrKyfEDyeubmRqKRm',
           'kloxc@mail.ru': 'FVUeii2MdbNcqEmZrq7N',
           'proto.dasha@mail.ru': 'LqJt4xXtqaAxUsd4D1HD',
           'dportq@mail.ru': 'CRUJZ7gi37VFn6a9mmYx',
           'dasha.port.06@mail.ru': 'Cnsy43cXqbAGVUswWdig',
           'portuyeye@mail.ru': 'y2jPgBkCxLuDBiHU2cAV',
           'dlegoyy@mail.ru': 'NtX9FmVJDi8fsBusv16Z',
           'portee05@mail.ru': '2eiDAier2n1MBrf1MZiX',
           'flipov.vlad@mail.ru': 'yePH6i1Sxw7XiYjR3E5K',
           'msolhov@mail.ru': 'RzQcdrRwYaJqycuxHzxM',
           'aslocv@mail.ru': 'i7n8zk8Dy0E9v7Sx2wLX',
           'kagbxz@mail.ru': 'vYkY8mrbqxGzpz8NqXe7',
           'mardjela@mail.ru': 'Cug2mXZ5d4c8aLNfnwCR',
           'egsdfdg@mail.ru': 'kCYudJg4P1KYF7iLkgcK',
           'ejofree@mail.ru': 'YKxiqwNwA87DEf8VftHF',
           'lina.fdfsfg@mail.ru': 'ts4JsHZhPf2vZ8rqxhmr',
           'abfdgs@mail.ru': 'vqdEDLtXpTU784KqLcvF',
           'pgkksdg@mail.ru': 'qfs6Nrg2zG2Zfudt8idz',
           'vadgadg@mail.ru': 'VkM3a1GpPaABr84PCztb',
           'jake.nod@mail.ru': '39uS26JTgKrBWJFdC16h',
           'noah.soli@mail.ru': 'xXvHn9usximafHmt4Rup',
           'jdlodd@mail.ru': 'rcAxee0FtnzL0wf4qUuX',
           'mmardjela@mail.ru': '3fhUwHBWipHasch29fv0',
           'andrea.aalto@mail.ru': 'XJrFhNwPamYaz6mjJ6yT',
           'luca.velde@mail.ru': 'cEeCv1mtP8Y2fsL4F1Xf',
           'esolhov@mail.ru': 'HB3zF1mz1H7EDEfinhdi',
           'fdfsfg04@mail.ru': 'hSrWxzjRWBLDYuPAB60F',
           'amardjela@mail.ru': 'rmyndAbyj7e5gjg3queN',
           'mrashni@mail.ru': 'Gukjw4sbwCrgAgFaZzx1',
    'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
    'terbgebuoviror@mail.ru': 'gaqaKs06xg22kkXXW2LU',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'nicrey4@comcast.net': 'Dabears54',
'mordechai@mail.com': 'Mordechai',
'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
'tarabedford@comcast.net': 'Money4me',
'mycockneedsit@mail.com': 'benjamin3',
'saralaine@mail.com': 'sarlaine12!1',
'jonb2006@verizon.net': '1969Camaro',
'rjhssa1@verizon.net': 'Donna613*',
'cameron.doug@charter.net': 'Jake2122$',
'bridget.shappell@comcast.net': 'Brennan1',
'rugs8@comcast.net': 'baseball46',
'averyjacobs3@mail.com': '1960682644!',
'lstefanick@hotmail.com': 'Luv2dance2',
'bchavez123@mail.com': 'aadrianachavez',
'lukejamesjones@mail.com': 'tinkerbell1',
'emahoney123@comcast.net': 'Shieknmme3#',
'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
'jet747@cox.net': 'Sadie@1234',
'landsgascareservices@mail.com': 'Alisha25@',
'samantha224@mail.com': 'Madden098!@',
'kbhamil@wowway.com': 'Carol1940',
'email@bjasper.com': 'Lhsnh4us123!',
'biggsbrian@cox.net': 'Trains@2247Trains@2247',
'dzzeblnd@aol.com': 'Geosgal@1',
'jtrego@indy.rr.com': 'Jackwill14!',
'chrisphonte.rj@comcast.net': 'Junior@3311',
'tvwifiguy@comcast.net': 'Bill#0101',
'defenestrador@mail.com': 'm0rb1d8ss',
'glangley@gmx.com': 'ironhide',
'charlotte2850@hotmail.com': 'kelalu2850',}
#Poluchateli
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def logo():
#Ya eto logo zaebalsya delat
    print("")
    print("\033[92m                                                Version 3.0")



def menu():
    print(" ╔════════════════╗")
    print(" ║[1] Автор       ║")
    print(" ╚════════════════╝")
    print(" ╔════════════════╗")
    print(" ║[2]Сн0с аккаунта║")
    print(" ╚════════════════╝")
    print(" ╔════════════════╗")
    print(" ║[3]Сн0с канала  ║")
    print(" ╚════════════════╝")
    print(" ╔════════════════╗")
    print(" ║[4]Сн0с бота    ║")
    print(" ╚════════════════╝")
    print(" ╔════════════════╗")
    print(" ║[5]Выход        ║")
    print(" ╚════════════════╝")

    choice = input("ввод: ")
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    logo()
    choice = menu()
    if choice == '2':
        print("1. СПАМ,ДОКСUHG,TРOLLINГ")
        print("2. СНОС СЕССИЙ.")
        print("3. С премкой,виртуальным номером")

        comp_choice = input("выбирай: ")
        if comp_choice in ["1", "2", "3"]:

            username = input("юзер жертвы: ")
            id = input("айди жертвы: ")
            chat_link = input("ссылка на чат: ")
            violation_link = input("ссылка на нарушение: ")
            print("Ожидайте...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice == "2":
            username = input("юзернейм: ")
            id = input("айди: ")
            print("Ожидайте...")
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["3"]:

            username = input("юзернейм: ")
            id = input("айди: ")
            comp_texts = {
                "5": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 9999
                    time.sleep(5)


    elif choice == "3":
        
        print("1. с личными данными,с живодерством и тд")

        ch_choice = input("Ввод: ")

        if ch_choice in ["1"]:
            channel_link = input("ссылка на канал жертвы: ")
            channel_violation = input("ссылка на нарушение: ")
            print("Ожидайте...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 100000
                    time.sleep(5)

    elif choice == "1":
        print("сносер хуйня паста ебаннаЯ")
        time.sleep(7)

    elif choice == "4":
        print("1. Пробив бот на подобии гб и тд")
        bot_ch = input("ввод: ")

        if bot_ch == "1":
            bot_user = input("юз бота: ")
            print("Ожидайте")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, '\033[92mЖалоба на бота телеграм\033[0m', comp_body)
                    print(f"\033[92mОтправлено на {receiver} от {sender_email}!\033[0m")
                    sent_emails += 1
                    time.sleep(5)

                if choice == '5':
                    print("удачи")
                    time.sleep(2)



  
if __name__ == "__main__":
    main()
