from peewee import *
import datetime
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

DATABASE = SqliteDatabase('learning.db')


class Entry(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    title = CharField()
    timespent = CharField()
    what_learned = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)








def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()    