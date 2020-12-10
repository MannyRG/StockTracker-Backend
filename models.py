from peewee import *
import datetime
from flask_login import UserMixin
import os
from playhouse.db_url import connect


DATABASE = SqliteDatabase('Tracker.sqlite')

class Stocks(Model):
    name = TextField()
    ticker = CharField()
    weburl = CharField()
    logo = TextField()
    Industry = TextField()
    country = CharField()
    exchange = TextField()
    ipo = CharField()
    marketCapitalization = CharField()

    class Meta:
        database = DATABASE


class Tracker(Model):
    title = TextField(default="New Track")
    track1 = ForeignKeyField(Stocks, backref="tracked", null = True)
    track2 = ForeignKeyField(Stocks, backref="tracked", null = True)
    track3 = ForeignKeyField(Stocks, backref="tracked", null = True)
    track4 = ForeignKeyField(Stocks, backref="tracked", null = True)
    notes = TextField(default="")
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE




def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Tracker, Stocks], safe=True)
    print("TABLES Created")
    DATABASE.close()







