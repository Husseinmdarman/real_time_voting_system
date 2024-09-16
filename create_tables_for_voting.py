from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

###
""""
creating classes that will be used to map attribute to tables
"""
###

Base = declarative_base()

class Candidate(Base):
    __tablename__ = 'candidates'
    
    candidate_id = Column(String(255), primary_key=True)
    candidate_name = Column(String(255))
    party_affiliation = Column(String(255))
    biography = Column(Text)
    campaign_platform = Column(Text)
    photo_url = Column(Text)


class Voter(Base):
    __tablename__ = 'voters'
    
    voter_id = Column(String(255), primary_key=True)
    voter_name = Column(String(255))
    date_of_birth = Column(String(255))
    gender = Column(String(255))
    nationality = Column(String(255))
    registration_number = Column(String(255))
    address_street = Column(String(255))
    address_city = Column(String(255))
    address_state = Column(String(255))
    address_country = Column(String(255))
    address_postcode = Column(String(255))
    email = Column(String(255))
    phone_number = Column(String(255))
    cell_number = Column(String(255))
    picture = Column(Text)
    registered_age = Column(Integer)


def create_tables(connection_string):
    engine = create_engine('postgresql://username:password@localhost/mydatabase')
    Base.metadata.create_all(engine)
    return engine