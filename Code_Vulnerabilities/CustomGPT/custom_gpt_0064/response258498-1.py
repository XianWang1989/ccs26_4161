
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database connection
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a recipe for demonstration
new_recipe = Recipe(title='Pasta', instructions='Boil water, cook pasta.')
session.add(new_recipe)
session.commit()

# Query to get the first recipe
r = session.query(Recipe).first()

# Accessing the nth column (e.g., 2nd column)
n = 2
nth_value = list(r.__dict__.values())[n]  # Adjust the index as needed

print(f'The {n}th column value is: {nth_value}')
