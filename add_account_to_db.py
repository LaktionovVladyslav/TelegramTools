from app import db
import models
from telethon import TelegramClient, sync
from telethon.sessions import StringSession


def login_and_add():
    api_id = int(input('Api id: '))
    api_hash = input('Api hash: ')
    phone = input('Номер телефона')
    client = TelegramClient(StringSession(), api_id=api_id, api_hash=api_hash)

    client.start(phone=lambda: phone)
    user = client.get_me()
    session_string = client.session.save()
    user_obj = models.TelegramUser.query.get(user.id)
    if not user_obj:
        user_obj = models.TelegramUser(user_id=user.id, phone_number=user.phone, username=user.username,
                                       last_name=user.last_name, first_name=user.first_name)
    account = models.Account(session=session_string, telegram_user=user_obj)
    db.session.add(account)
    db.session.commit()


def reg_and_add():
    api_id = int(input('Api id: '))
    api_hash = input('Api hash: ')
    phone = input('Номер телефона')
    client = TelegramClient(StringSession(), api_id=api_id, api_hash=api_hash)
    client.connect()
    client.send_code_request(phone=phone, force_sms=True)
    code = int(input('Code: '))
    client.sign_up(phone=phone, code=code, first_name='Борис', last_name='Власенко')
    user = client.get_me()
    session_string = client.session.save()
    user_obj = models.TelegramUser.query.get(user.id)
    if not user_obj:
        user_obj = models.TelegramUser(user_id=user.id, phone_number=user.phone, username=user.username,
                                       last_name=user.last_name, first_name=user.first_name)
    account = models.Account(session=session_string, telegram_user=user_obj)
    db.session.add(account)
    db.session.commit()


mode = input('Добавить сушествующий аккаунт (1), новий (2)')

if mode == "1":
    login_and_add()
else:
    reg_and_add()
