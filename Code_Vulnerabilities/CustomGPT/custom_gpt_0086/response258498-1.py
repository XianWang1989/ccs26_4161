
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database (using SQLite for this example)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example usage
recipe = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Getting the nth column value (e.g., 0 for 'id', 1 for 'title', 2 for 'instructions')
n = 2
nth_value = getattr(r, r.__table__.columns[n].name)

print(nth_value)  # Output: Boil water, add pasta.
