
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database engine and session
engine = create_engine('sqlite:///:memory:')  # Replace with your database URL
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example usage
# Adding a sample recipe
recipe = Recipe(title='Pasta', instructions='Boil water and add pasta.')
session.add(recipe)
session.commit()

# Fetching the recipe instance
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_value(instance, n):
    # Get the column names
    column_names = list(instance.__mapper__.c.keys())
    # Return the nth value
    return getattr(instance, column_names[n])

# Example: Accessing the 1st (title) and 2nd (instructions) columns
title_value = get_nth_value(r, 0)  # 1st column
instructions_value = get_nth_value(r, 1)  # 2nd column

print(f'Title: {title_value}')
print(f'Instructions: {instructions_value}')
