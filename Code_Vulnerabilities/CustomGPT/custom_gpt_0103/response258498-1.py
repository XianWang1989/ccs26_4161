
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite database (or connect to your database)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a Recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water, cook pasta.")
session.add(new_recipe)
session.commit()

# Querying the Recipe instance
r = session.query(Recipe).first()

# Accessing the nth column value (0-based index)
n = 2  # For example, to get the instructions column
column_value = list(vars(r).values())[n]  # Get the nth value

print(f"The value of the {n}th column (instructions) is: {column_value}")
