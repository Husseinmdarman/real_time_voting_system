import create_tables_for_voting
import generate_data
from create_tables_for_voting import Candidate
from sqlalchemy.orm import sessionmaker



if __name__ == "__main__":

    try:
        engine = create_tables_for_voting.create_tables("postgresql+psycopg2://postgres:postgres@localhost:5432/voting")
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query all rows
        results = session.query(Candidate).all()
            
        if len(results) == 0:
            for i in range(3):
                candidate_data = generate_data.generate_candidate_data(i, 3)
                
                # reading the candidate dictionary into the previously made table class definition
                new_candidate = Candidate(
                candidate_id=candidate_data['candidate_id'],
                candidate_name=candidate_data['candidate_name'],
                party_affiliation=candidate_data['party_affiliation'],
                biography=candidate_data['biography'],
                campaign_platform=candidate_data['campaign_platform'],
                photo_url=candidate_data['photo_url']
                )

                ## add new candidate information to DB
                session.add(new_candidate)
                session.commit()
                print(new_candidate)

    except Exception as e:
        print(f"There was an error when connection to db: {e}")