
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Sample setup for a SQLite in-memory database (for demonstration purposes)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding and querying a recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Query the recipe instance
r = session.query(Recipe).first()

# Function to get the nth column
def get_nth_column(instance, n):
    return getattr(instance, instance.__table__.columns.keys()[n])

# Example usage
n = 2  # Change this value to get different columns (0 for id, 1 for title, 2 for instructions)
nth_value = get_nth_column(r, n)
print(nth_value)  # Output: Mix ingredients and cook.
