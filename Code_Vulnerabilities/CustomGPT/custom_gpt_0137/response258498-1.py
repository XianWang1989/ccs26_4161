
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example usage
if __name__ == "__main__":
    # Set up the database connection (replace with your database URI)
    engine = create_engine('sqlite:///recipes.db')
    Base.metadata.create_all(engine)  # Create tables

    Session = sessionmaker(bind=engine)
    session = Session()

    # Assuming you have an instance of Recipe from a query
    r = session.query(Recipe).first()  # Fetch the first recipe instance

    # Access the nth column value
    # For example, accessing instructions (which is the 2nd column, index 1 if we start from 0)
    n = 2  # Change this to access different columns
    nth_column_value = getattr(r, r.__table__.columns.keys()[n-1])  # n-1 to adjust for index

    print(nth_column_value)
