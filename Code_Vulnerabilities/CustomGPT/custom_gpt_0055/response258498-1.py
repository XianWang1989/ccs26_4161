
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database (this is an example with SQLite)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a Recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(new_recipe)
session.commit()

# Querying the Recipe instance
r = session.query(Recipe).first()

# Accessing the nth column value (e.g., 1 for title, 2 for instructions)
def get_nth_column(instance, n):
    return list(instance.__dict__.values())[n]

# Get the title (0th column)
print(get_nth_column(r, 0))  # Output: Pasta

# Get instructions (1st column)
print(get_nth_column(r, 2))  # Output: Boil water and cook pasta.
