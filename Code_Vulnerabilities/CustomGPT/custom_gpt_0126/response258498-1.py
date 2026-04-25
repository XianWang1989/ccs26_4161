
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class and the Recipe model
Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create a database session for demonstration purposes
engine = create_engine('sqlite:///recipes.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example of querying a Recipe instance
# (Make sure to populate the table with actual data first)
recipe_instance = session.query(Recipe).first()

# Function to get nth column
def get_nth_column(instance, n):
    return list(instance.__dict__.values())[n]

# Usage: Access the 2nd column (index 2 corresponds to 'instructions')
nth_value = get_nth_column(recipe_instance, 2)
print(nth_value)
