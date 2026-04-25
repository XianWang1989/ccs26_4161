
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

# Example setup
engine = create_engine('sqlite:///:memory:')  # Example with an in-memory database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a recipe instance
recipe = Recipe(title='Chocolate Cake', instructions='Mix ingredients and bake.')
session.add(recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column (e.g., 2nd column which is 'instructions')
n = 2  # Index for the nth column
value = list(r.__dict__.values())[n]  # Get the nth column value

print(value)  # Output: Mix ingredients and bake.
