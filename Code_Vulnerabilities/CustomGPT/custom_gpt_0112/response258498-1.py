
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example engine and session setup
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite for example
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water and cook pasta.')
session.add(new_recipe)
session.commit()

# Querying a recipe
r = session.query(Recipe).first()

# Accessing the nth column (e.g., 1 for title, 2 for instructions)
n = 1  # Change this for different columns
value = list(r.__dict__.values())[n]
print(value)
