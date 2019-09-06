from telethon import TelegramClient, sync


class ChatParserMethods(TelegramClient):
    def parsing_chat(self, chat_id):
        print(chat_id)
        chat = self.get_entity(chat_id)
        try:
            participants = self.get_participants(chat)
            users = [user for user in participants if user.username]
            return users
        except:
            return []



