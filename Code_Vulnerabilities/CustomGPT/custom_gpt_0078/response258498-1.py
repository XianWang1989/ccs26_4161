
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example of accessing the nth column
def get_nth_column_value(instance, n):
    # Retrieve values in the order of declaration
    column_values = list(instance.__dict__.values())

    # Check if the index is valid
    if n < 0 or n >= len(column_values):
        raise IndexError("Index out of range")

    return column_values[n]

# Setup database (SQLite for demonstration)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create and add a recipe instance
recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(recipe)
session.commit()

# Query to get the first recipe
r = session.query(Recipe).first()

# Access the nth column (e.g., 1 for title, 2 for instructions)
title_value = get_nth_column_value(r, 1)  # Get the second column (title)
instructions_value = get_nth_column_value(r, 2)  # Get the third column (instructions)

print(f"Title: {title_value}")
print(f"Instructions: {instructions_value}")
