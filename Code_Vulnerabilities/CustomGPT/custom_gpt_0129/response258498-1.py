
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup for SQLAlchemy (assuming SQLite in-memory database for demonstration)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Adding a recipe instance for demonstration
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Querying the Recipe instance
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column_value(instance, n):
    # Ensure n is within bounds
    if n < 0 or n >= len(instance.__table__.columns):
        raise IndexError("Index out of range for the number of columns.")
    # Get the nth column's corresponding column object
    column_name = list(instance.__table__.columns.keys())[n]
    return getattr(instance, column_name)

# Example usage: Getting the value of the 2nd column (index 1)
nth_value = get_nth_column_value(r, 1)
print(nth_value)  # This will print "Pancakes", which is the title of the recipe
