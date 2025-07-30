from sqlalchemy import create_engine, Column, String, Integer, Text, TIMESTAMP, func, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

###
""""
creating classes that will be used to map attribute to tables
"""
###

Base = declarative_base()


class Candidate(Base):
    """
    This class represents the candidates that are up for election
    """
    __tablename__ = 'candidates'
    
    candidate_id = Column('candidate.id',Integer, unique=True ,primary_key=True) # unique identifier for each candidate
    candidate_name = Column(String(255))
    party_affiliation = Column(String(255))
    biography = Column(Text)
    campaign_platform = Column(Text)
    photo_url = Column(Text)


class Voter(Base):
    """
    This class represents the voters who can vote in the election
    """
    __tablename__ = 'voters'
    
    voter_id = Column('voters.id',Integer, unique=True,primary_key=True) # unique identifier for each voter
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

class Vote(Base):
    """
    This class represents the voters who have voted for a candidate
    """
    __tablename__ = 'vote'
    
    voter_id = Column(Integer, unique=True, nullable = False, ForeignKey('voters.id')) # unique identifier for each voter since they can only vote once
    candidate_id = Column(Integer, nullable = False, ForeignKey('candidates.id')) # This is not unique since a candidate can receive multiple votes
    vote_time = Column(TIMESTAMP,  server_default=func.now(), nullable=False) # time when the vote was cast

    __table_args__ = ( PrimaryKeyConstraint(voter_id, candidate_id),
      )  # Ensures that a voter can only vote for a candidate once
    

def create_tables(connection_string):
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    return engine