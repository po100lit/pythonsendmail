import logging
import os
# lib for send text email
import smtplib
# lib for send attach file
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email
import email.mime.application


def send_text_mail() -> None:
    logging.info('Start logging...')
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()
    smtp_obj.login('pytonsendmail@gmail.com', password=os.environ['gmail_pass'])
    '''
    Как создать и использовать пароли приложений
    Важно! Чтобы создать пароль приложения, необходимо включить двухэтапную аутентификацию в аккаунте Google.
    Если она включена и при входе появляется сообщение "Неверный пароль", попробуйте использовать пароль приложения.
        Откройте страницу Аккаунт Google.
        Нажмите Безопасность.
        В разделе "Вход в аккаунт Google" выберите пункт Двухэтапная аутентификация.
        Внизу страницы нажмите Пароли приложений.
        Укажите название, которое поможет вам запомнить, где будет использоваться пароль приложения.
        Выберите Создать.
        Введите пароль приложения, следуя инструкциям на экране. Пароль приложения – это 16-значный код, 
            который генерируется на вашем устройстве.
        Нажмите Готово.
    '''
    smtp_obj.sendmail("pytonsendmail@gmail.com", "po100lit@mail.ru", "go to bed!")
    smtp_obj.quit()


def send_attach_mail() -> None:
    logging.info('Start logging...')

    # Create a text/plain message
    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = 'Greetings'
    msg['From'] = 'pytonsendmail@gmail.com'
    msg['To'] = 'po100lit@mail.ru'
    logging.info('message headers was created')

    # The main body — just another attachment
    body = email.mime.text.MIMEText("Hello, how r you? I am fine.")
    msg.attach(body)
    logging.info('message body/text was created')

    # File attachment
    filename = 'sample.pdf'
    with open(filename, 'rb') as file:
        att = email.mime.application.MIMEApplication(file.read())
    att.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(att)
    logging.info('attach file was prepared')

    # send via Gmail server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('pytonsendmail@gmail.com', password=os.environ['gmail_pass'])
    s.sendmail("pytonsendmail@gmail.com", "po100lit@mail.ru", msg.as_string())
    s.quit()
    logging.info('message with attach sent successfully')


if __name__ == '__main__':
    logging.basicConfig(filename='log_file.log', encoding='utf-8', level=logging.INFO, filemode='a',
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    # send_text_mail()
    send_attach_mail()
