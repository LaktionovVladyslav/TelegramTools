from telethon import TelegramClient, sync
from telethon.sessions import StringSession


class ChatParserMethods(TelegramClient):
    def parsing_chat(self, chat_username):
        self.connect()
        participants = self.get_participants(chat_username)
        users = [user for user in participants if user.username]
        return users



