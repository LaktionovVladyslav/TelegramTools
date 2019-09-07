from telethon import TelegramClient, sync
from telethon.errors import ChatAdminRequiredError


class ChatParserMethods(TelegramClient):
    def parsing_chat(self, chat_obj):
        chat = self.get_entity(chat_obj.user_names[-1].username)
        if chat.megagroup:
            try:
                participants = self.get_participants(chat)
            except ChatAdminRequiredError:
                return []
            users = [user for user in participants if user.username]
            return users
        else:
            return []



