
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy base class
Base = declarative_base()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database engine and create a session
engine = create_engine('sqlite:///recipes.db')  # Example SQLite database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example of retrieving a Recipe instance (assuming you have entries in the table)
r = session.query(Recipe).first()  # Fetch the first recipe

# Get the nth column value
n = 2  # for 'instructions'
column_value = list(r.__dict__.values())[n]  # Access the n-th column value
print(column_value)
