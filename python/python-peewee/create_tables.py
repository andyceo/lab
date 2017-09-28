#!/usr/bin/python3

from peewee import *
from model.Person import Person
from model.Pet import Pet
from datetime import date

db = SqliteDatabase('people.db')

db.connect()

# db.create_tables([Person, Pet])

# uncle_bob = Person(name='Bob', birthday=date(1992, 1, 15), is_relative=True)
# uncle_bob.save()  # bob is now stored in the database

# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)

# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
# grandma.name = 'Grandma L.'
# grandma.save()  # Update grandma's name in the database.

# bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
# herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
# herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
# herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

print("Select persons:")
for person in Person.select():
    print(person.name, person.is_relative)

print()
print("Select pets with additional queries:")
query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(pet.name, pet.owner.name)

print()
print("Select pets with join:")
query = (Pet.
         select(Pet, Person).
         join(Person).
         where(Pet.animal_type == 'cat'))
for pet in query:
    print(pet.name, pet.owner.name)

print()
print('Let’s get all the pets owned by Bob:')
for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)

import json
print(json.loads('{"a":"a"}'))
