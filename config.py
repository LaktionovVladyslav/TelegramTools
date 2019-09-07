import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig:
    DEBUG = True

    TOKEN = "839502302:AAFrzUcoluTsUGLIHKE6-S5jTzGWwSelFDU"
    LINK_TO_BOT = 'https://t.me/devrobbot?start=%s'


class ProductionConfig:
    DEBUG = False

    TOKEN = "935251633:AAHvMBBfVTSRaK3ow3sbFT-Xav8mbOtR4fQ"

    LINK_TO_BOT = 'https://t.me/my_der_register_bot'


class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:bossK@@192.168.88.235/telegram"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
