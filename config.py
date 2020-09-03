import os


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = 'postgres://postgres:123@localhost/mydb_wl'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////mydb.db'
    SECRET_KEY = 'some_shit'

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
