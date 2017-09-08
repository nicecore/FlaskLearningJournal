from peewee import *
import datetime

DATABASE = SqliteDatabase('learning.db')


class Entry(Model):
    title = CharField()
    date = DateField()
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