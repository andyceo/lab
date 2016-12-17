from peewee import *


class BaseModel(Model):
    class Meta:
        database = database
