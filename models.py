from peewee import *
import datetime

DATABASE = SqliteDatabase('Tracker.sqlite')


class Stock(Model):
    ticker = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Stock], safe=True)
    print("TABLES Created")
    DATABASE.close()







