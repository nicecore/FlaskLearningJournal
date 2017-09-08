from peewee import *
import datetime
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

DATABASE = SqliteDatabase('learning.db')


class Entry(Model):
    title = CharField()
    date = DateTimeField()
    timespent = CharField()
    what_learned = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-date',)








def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()    