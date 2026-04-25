
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup your database (example with SQLite in-memory)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example data
recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(recipe)
session.commit()

# Function to get the nth column value
def get_nth_column_value(instance, n):
    # Get all attributes as a list
    attributes = list(instance.__mapper__.c)
    if n < len(attributes):
        return getattr(instance, attributes[n].name)
    else:
        raise IndexError("Index out of range.")

# Usage
r = session.query(Recipe).first()
nth_value = get_nth_column_value(r, 2)  # Change 2 to access different columns
print(nth_value)  # Output: Boil water and cook pasta.
