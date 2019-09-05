from telethon.sessions import StringSession

from chat_parser import ChatParserMethods
from models import TelegramUser
from app import db

CHAT_USERNAME = "@biznes_uslugi"
STRING = "1AZWarzQBuzwyRqDHOA6b1eyKGwUwNZwak2d_5t9d8ZSa8-_-lJFuxXicmBg0pdvjeRl4Pd-IZ-gOxHnJsdCS" \
         "-yp5qzO3OmX5oLMGQZcaq5REBpaoKcep2k2HuUVQmqfXXZ7VfjN322vkm3n7jbq0VkKrF7ZdUf99wEEySeN-Y85vma_mQXl6N9KVwdSeFLU" \
         "-QwqETUc5S7NjYUORL0vrEJNScVrRYf_nBmKo8UZzLcumqBF-44Eq5c3tZKp6noLLA9QARREtQ" \
         "-5N3dXqkaieccxUt7iqp0pE0jepNgSe72wUX9pqfX3a8VFSs56O2kZqZ6b_HKw9RaMLSVo1pNtSPiftZkvogis="
FILE_NAME = 'chats.txt'
chat_parser = ChatParserMethods(StringSession(STRING), api_hash='5c10a75e8f9a21326fa191dc8dd4d916', api_id=933676)
telegram_users = [
    TelegramUser(user_id=user.id, phone_number=user.phone, username=user.username, last_name=user.last_name,
                 first_name=user.first_name) for user in chat_parser.parsing_chat(chat_username=CHAT_USERNAME)]

for telegram_user in telegram_users:
    db.session.add(telegram_user)
    try:
        db.session.flush()
    except:
        db.session.rollback()
db.session.commit()