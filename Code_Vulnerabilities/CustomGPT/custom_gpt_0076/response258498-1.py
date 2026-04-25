
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example: Set up the database (replace with your database URL)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Insert a sample recipe
recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Access the nth column value
n = 2  # For example, get the 2nd column (instructions)
nth_column_value = getattr(r, r.__mapper__.columns.keys()[n])
print(nth_column_value)
