from app import db
import models
from telethon import TelegramClient, sync
from telethon.sessions import StringSession

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