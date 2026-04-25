
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Assume you have your database set up
engine = create_engine('sqlite:///:memory:')  # Example engine
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding a new recipe instance for demonstration purposes
new_recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(new_recipe)
session.commit()

# Query to retrieve the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
def get_nth_column(instance, n):
    return list(instance.__dict__.values())[n]

# Example: Get the 2nd column (instructions)
nth_value = get_nth_column(r, 2)
print(nth_value)  # Output: Boil water and add pasta.
