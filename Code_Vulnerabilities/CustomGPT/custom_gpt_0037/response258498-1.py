
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database and session (modify connection string as needed)
engine = create_engine('sqlite:///:memory:')  # Example using in-memory SQLite
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding a recipe instance
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Querying the recipe instance
r = session.query(Recipe).first()

# Accessing the nth column using __dict__
n = 2  # For the 2nd column, which is 'instructions'
nth_value = list(r.__dict__.values())[n]

print(nth_value)  # Output: "Mix ingredients and cook."
