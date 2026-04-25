
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base
Base = declarative_base()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example connection to the database (adjust URL accordingly)
engine = create_engine('sqlite:///recipes.db')
Session = sessionmaker(bind=engine)
session = Session()

# Perform a query to get a recipe instance
r = session.query(Recipe).first()

# Accessing the nth column (for example, instructions which is the 2nd column)
nth_value = list(r.__dict__.values())[1]  # Index 1 corresponds to the n-th column since it's 0 indexed
print(nth_value)
