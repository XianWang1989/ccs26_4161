
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database connection and session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water and add pasta.')
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Convert the instance to a dictionary
recipe_dict = {column.name: getattr(r, column.name) for column in Recipe.__table__.columns}

# Get the nth column value (e.g., 2nd column)
n = 1  # Change this to get different columns (0-based index)
nth_value = list(recipe_dict.values())[n]

print(nth_value)  # Output will be 'Boil water and add pasta.'
