
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example of getting the nth column value
def get_nth_column_value(instance, n):
    values = list(instance.__dict__.items())
    if n < 0 or n >= len(values):
        raise IndexError("Index out of range")
    return values[n][1]

# Example usage
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a new Recipe instance
recipe = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(recipe)
session.commit()

# Fetch the recipe
r = session.query(Recipe).first()

# Get the nth column value, e.g., 2nd column (instructions)
nth_value = get_nth_column_value(r, 2)

print(nth_value)  # Output: Boil water, add pasta.
