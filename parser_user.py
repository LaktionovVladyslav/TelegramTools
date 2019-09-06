from telethon.errors import UsernameInvalidError
from telethon.sessions import StringSession

from app import db
from chat_parser import ChatParserMethods
from models import TelegramUser, Chat, UserNames

chats = ['@xarplace_chat',
         '@goSilavEdnosti_chat',
         '@popanchik1',
         '@kiev_chat',
         '@nay_chat',
         '@Kiev_top',
         '@makeownbusiness',
         '@lpiua',
         '@CoffeeChatUkraine',
         '@info_odessa_ua',
         '@dpinformatorua',
         '@chatinroad',
         '@recruitua',
         '@ukraina_chat',
         '@prognozichat',
         '@stavki_chatt',
         '@chat_stavki',
         '@chatecb',
         '@Business_runners_UA_chat',
         '@Business_Drive_Chat',
         '@BUSTAN_CHAT',
         '@fb_killa_chat',
         '@kpitrade_chat',
         '@ChatWarsDigest',
         '@channelsubscribers',
         '@gamblingaff',
         '@MinerGameChat',
         '@CapitalistGameChatRU',
         '@spartagamechat',
         '@seo_burzh_chat',
         '@chatmedikov',
         '@campus_kneu',
         '@sm_nau_chat',
         '@Aurum_chat',
         '@chat_stavki',
         '@Karazin_Student_Chat',
         '@HUF_STAFF_CHAT',
         '@nails_chat',
         '@nay_chat',
         '@NaVichat',
         '@filmtreiler_chat',
         '@filter_chat',
         '@abit_filosof',
         '@abit_filology',
         '@figli_IF_chat',
         '@photostudy_me_chat',
         '@muz_chat',
         '@znakomstva_chats',
         '@xtb_rn7',
         '@chatupxx',
         '@mil_chat',
         '@xarplace_chat',
         '@xiaomitechnoblog',
         '@chat_miracle_morning',
         '@milkmulatkachat',
         '@FarmGameChatRu',
         '@topsliw_chat',
         '@progeri_chat',
         '@kamaz_centre_donetsk_chat',
         '@drop_chat',
         '@lucky_days_chat',
         '@fa_chat',
         '@hollysolli',
         '@chatiksmola',
         '@truebitchland',
         '@taskrock_chat',
         '@kinzachat',
         '@Kino_Chat',
         '@findkievchat',
         '@kharkivcinema',
         '@sos_kh',
         '@nspclubrefchat',
         '@ukr_pravda_chat',
         '@RomanceClubChat',
         '@KlymenkoTime_chat',
         '@thealphacentauri',
         '@od_chat',
         '@cichat']
STRING = '1AZWarzYBu5cqO93YuMHLQLx7sw08jetAqyYP9JIIT' \
         '-doAkRmmKQnSv3w3Ihi8z7AFlde67BIwzRPaPb59VIbIySKcNu9nbCDoeac84u8jBHc-2xa-wSjo06aFae1wb3kRO' \
         '-3vEnEmUCGKaaEYGBARf-lBvp1_2jmZliuOX__B' \
         '-hG200VgQPlStgaaAxMId4k9PCxYsEcuz2mX1p9qZVs1EpmXoKXqzGwG1ZscyHrNIafWpZxeRgYfT-HurgvI5ZPrDS7E8tjjIQjhof9Y-6M' \
         '-c2DAUJ6ntsNd7rAucmez3yGs0C9l3CyufLwIUts8DXKN5rx4TdTEUhYFRGlChDK0ddDG_iv3ho='

chat_parser = ChatParserMethods(StringSession(STRING), api_hash='5c10a75e8f9a21326fa191dc8dd4d916', api_id=933676)
chat_parser.connect()
for chat in chats:
    try:
        chat_entity = chat_parser.get_entity(chat)
    except UsernameInvalidError:
        print(chat)
        continue
    chat_obj = Chat.query.get(chat_entity.id)
    if not chat_obj:
        chat_username_obj = UserNames.query.filter_by(username=chat_entity.username).first()
        if not chat_username_obj:
            chat_username_obj = UserNames(username=chat_entity.username)
        chat_obj = Chat(id=chat_entity.id, user_names=[chat_username_obj], title=chat_entity.title)
        db.session.add(chat_obj)
        db.session.commit()


# for user in chat_parser.parsing_chat(chat_username=chat):
#     telegram_user_obj = TelegramUser.query.get(user.id)
#     if not telegram_user_obj:
#         telegram_user_obj = TelegramUser(user_id=user.id, phone_number=user.phone, username=user.username,
#                                          last_name=user.last_name,
#                                          first_name=user.first_name)
#     chat_obj.telegram_users.append(telegram_user_obj)
#     try:
#         db.session.flush()
#     except Exception as e:
#         print(e)
#         db.session.rollback()
# db.session.commit()
