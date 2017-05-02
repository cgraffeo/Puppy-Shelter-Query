# Import stuff from sqlalchemy and bind engine, accessed through DBSessions
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Shelter, Puppy
import datetime


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


def query_One():
    puppies = session.query(Puppy.name).order_by(Puppy.name.asc()).all()
    for puppy in puppies:
        print puppy[0]


def query_Two():
    today = datetime.date.today()
    six_months = today - datetime.timedelta(days=182)
    young_pups = session.query(Puppy.name, Puppy.dateOfBirth)\
                        .filter(Puppy.dateOfBirth >= six_months)\
                        .order_by(Puppy.dateOfBirth.desc())
    for item in young_pups:
        name = item[0]
        dob = str(item[1])
        print "Name:" + name + "\nDOB: " + dob + "\n"


def query_Three():
    pup_weight = session.query(Puppy.name, Puppy.weight)\
                        .order_by(Puppy.weight.asc()).all()
    for item in pup_weight:
        name = item[0]
        weight = str(int(item[1]))
        print "name: " + name + "\nWeight: " + weight + " lbs" + "\n"


def query_four():
    pup_by_shelter = session.query(Shelter, func.count(Puppy.id)).join(Puppy)\
                            .group_by(Shelter.id).all()
    for item in pup_by_shelter:
        id = str(item[0].id)
        shelter = item[0].name
        count = str(item[1])
        print "Shelter ID: " + id + "\nShelter Name: " + shelter\
            + "\nPuppy Count: " + count + "\n"




query_One()
query_Two()
query_Three()
query_four()
