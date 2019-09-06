from telethon import TelegramClient, sync


class ChatParserMethods(TelegramClient):
    def parsing_chat(self, chat_obj):
        chat = self.get_entity(chat_obj.user_names[-1].username)
        participants = self.get_participants(chat)
        users = [user for user in participants if user.username]
        return users



