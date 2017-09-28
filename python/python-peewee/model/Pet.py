from peewee import *
from model.Person import Person

db = SqliteDatabase('people.db')


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database
