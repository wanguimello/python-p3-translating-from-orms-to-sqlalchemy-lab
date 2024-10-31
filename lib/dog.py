#python lib/dog.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Dog

engine = create_engine('sqlite:///:dogs.db:')
# use our engine to configure a 'Session' class
Session = sessionmaker(bind=engine)
# use 'Session' class to create 'session' object
session = Session()

#creates a table that takes a declarative_base and creates a SQLite database
def create_table(base, engine):
    base.metadata.create_all(engine)
    return engine

#takes a Dog instance as an argument and saves(persists) the dog to the database
def save(session, dog):
    dog = Dog(
        name='joey',
        breed='cocker spaniel'
    )
    session.add(dog)
    session.commit()
    return session

#takes a session and returns a list of Dog instances for every record in the database.
def get_all(session):
    dogs = session.query(Dog).all()
    return [dog for dog in dogs ]

#takes a session and name and returns a Dog instance corresponding to its database record retrieved by name.
def find_by_name(session, name):
    dog_name = session.query(Dog).filter_by(name = name).first()  
    return dog_name

#takes a session and id and returns a Dog instance corresponding to its database record retrieved by id.
def find_by_id(session, id):
    dog_id = session.query(Dog).filter_by(id = id).first()  
    return dog_id

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter_by(name=name, breed = breed).first()
    return dog

def update_breed(session, dog, breed):
    # Querys the dog record
    dog = session.query(Dog).first()

    #if true update the breed
    if dog:
        dog.breed = breed
        
