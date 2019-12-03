class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:123@localhost/mydb_wl'
    SECRET_KEY = 'something very secret'
