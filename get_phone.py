from requests import Session
import models
from app import db
from tqdm import tqdm

s = Session()


def get_info(user):
    s.get('https://peopleua.site/')
    data = {
        'deanon': user.id
    }
    response = s.post('https://peopleua.site/file.php', data=data)
    if response.json().get('status') == 666:
        data = response.json().get('data')
        phone_obj = models.PhoneNumber.query.filter_by(phone_number=data).filter()
        if not phone_obj:
            phone_obj = models.PhoneNumber(phone_number=data)
        phone_obj.telegram_user = user
        db.session.commit()


def split_list(lst, n):
    splitted = []
    for i in reversed(range(1, n + 1)):
        split_point = len(lst) // i
        splitted.append(lst[:split_point])
        lst = lst[split_point:]
    return splitted


tg_users = models.TelegramUser.query.all()

for tg_user in tqdm(tg_users):
    get_info(tg_user)
