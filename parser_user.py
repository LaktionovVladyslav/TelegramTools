import random
import time

from tqdm import tqdm
from telethon.errors import UsernameInvalidError, FloodWaitError
from telethon.sessions import StringSession

from app import db
from chat_parser import ChatParserMethods
from models import TelegramUser, Chat, UserNames, Account


def add_list_chats(chats):
    for chat in chats:
        account = random.choice(Account.query.filter_by(valid=True).all())
        chat_parser = ChatParserMethods(StringSession(account.session), api_hash='5c10a75e8f9a21326fa191dc8dd4d916',
                                        api_id=933676)
        chat_parser.connect()
        usernames_obj = [chat.username for chat in db.session.query(UserNames.chat).filter_by(username=chat).all()]
        if chat in usernames_obj:
            continue
        try:
            chat_entity = chat_parser.get_entity(chat)
        except UsernameInvalidError:
            print(f"UsernameInvalidError: {chat}")
            continue
        except FloodWaitError:
            print(f"FloodWaitError: {chat_parser.get_my().id}")
            chat_parser.valid = False
            db.session.commit()
        except Exception as e:
            print(f"Exception: {e}")
            continue

        chat_obj = Chat.query.get(chat_entity.id)
        if not chat_obj:
            chat_username_obj = UserNames.query.filter_by(username=chat_entity.username).first()
            if not chat_username_obj:
                chat_username_obj = UserNames(username=chat_entity.username)
            chat_obj = Chat(id=chat_entity.id, user_names=[chat_username_obj], title=chat_entity.title)
            db.session.add(chat_obj)
            db.session.commit()


def add_chats_users(chats):
    for chat_obj in chats:
        account = random.choice(Account.query.filter_by(valid=True).all())
        chat_parser = ChatParserMethods(StringSession(account.session), api_hash='5c10a75e8f9a21326fa191dc8dd4d916',
                                        api_id=933676)
        chat_parser.connect()
        users = chat_parser.parsing_chat(chat_obj=chat_obj)
        for user in tqdm(users):
            telegram_user_obj = TelegramUser.query.get(user.id)
            if not telegram_user_obj:
                telegram_user_obj = TelegramUser(user_id=user.id, phone_number=user.phone, username=user.username,
                                                 last_name=user.last_name,
                                                 first_name=user.first_name)
            chat_obj.telegram_users.append(telegram_user_obj)
            try:
                db.session.flush()
            except Exception as e:
                print(e)
                db.session.rollback()
        db.session.commit()


add_chats_users(chats=Chat.query.all())
