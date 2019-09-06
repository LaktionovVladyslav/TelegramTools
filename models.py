from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app import db

chats__telegram_users = db.Table('chats__telegram_users',
                                 db.Column('telegram_users_id', db.Integer,
                                           db.ForeignKey('telegram_users.id')),
                                 db.Column('chats_id', db.Integer, db.ForeignKey('chats.id')),
                                 db.UniqueConstraint('telegram_users_id', 'chats_id')
                                 )


class TelegramUser(db.Model):
    __tablename__ = 'telegram_users'
    id = Column(Integer, primary_key=True, unique=True)
    bot = Column(Boolean)
    last_names = relationship("LastNames", back_populates="telegram_user")
    first_names = relationship("FirstNames", back_populates="telegram_user")
    phone_numbers = relationship("PhoneNumber", back_populates="telegram_user")
    user_names = relationship("UserNames", back_populates="telegram_user")
    accounts = relationship("Account", back_populates="telegram_user")
    chats = relationship(
        "Chat",
        secondary=chats__telegram_users,
        back_populates="telegram_users")

    def __init__(self, user_id, phone_number=None, username=None, last_name=None, first_name=None):
        self.id = user_id
        if phone_number:
            phone_number_obj = PhoneNumber.query.filter_by(phone_number=phone_number).first()
            if not phone_number_obj:
                phone_number_obj = PhoneNumber(phone_number=phone_number)
            self.phone_numbers.append(phone_number_obj)
        if username:
            user_name_obj = UserNames.query.filter_by(username=username).first()
            if not user_name_obj:
                user_name_obj = UserNames(username=username)
            self.user_names.append(user_name_obj)
        if last_name:
            last_name_obj = LastNames.query.filter_by(last_name=last_name).first()
            if not last_name_obj:
                last_name_obj = LastNames(last_name=last_name)
            self.last_names.append(last_name_obj)
        if first_name:
            first_name_obj = FirstNames.query.filter_by(first_name=first_name).first()
            if not first_name_obj:
                first_name_obj = FirstNames(first_name=first_name)
            self.first_names.append(first_name_obj)


class PhoneNumber(db.Model):
    __tablename__ = 'phone_numbers'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String, unique=True, nullable=False)
    telegram_user_id = Column(Integer, ForeignKey('telegram_users.id'))
    telegram_user = relationship("TelegramUser", back_populates="phone_numbers")


class UserNames(db.Model):
    __tablename__ = 'user_names'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    telegram_user_id = Column(Integer, ForeignKey('telegram_users.id'))
    telegram_user = relationship("TelegramUser", back_populates="user_names")
    chat_id = Column(Integer, ForeignKey('chats.id'))
    chat = relationship("Chat", back_populates="user_names")


class LastNames(db.Model):
    __tablename__ = 'last_names'
    id = Column(Integer, primary_key=True)
    last_name = Column(String, unique=True, nullable=False)
    telegram_user_id = Column(Integer, ForeignKey('telegram_users.id'))
    telegram_user = relationship("TelegramUser", back_populates="last_names")


class FirstNames(db.Model):
    __tablename__ = 'first_names'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, unique=True, nullable=False)
    telegram_user_id = Column(Integer, ForeignKey('telegram_users.id'))
    telegram_user = relationship("TelegramUser", back_populates="first_names")


class Chat(db.Model):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String, nullable=False)
    user_names = relationship("UserNames", back_populates="chat")
    telegram_users = relationship(
        "TelegramUser",
        secondary=chats__telegram_users,
        back_populates="chats")


class Account(db.Model):
    __tablename__ = 'accounts'
    session = Column(String, primary_key=True)
    telegram_user_id = Column(Integer, ForeignKey('telegram_users.id'))
    telegram_user = relationship("TelegramUser", back_populates="accounts")
    valid = Column(Boolean, default=True)
