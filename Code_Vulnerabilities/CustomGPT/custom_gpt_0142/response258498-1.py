
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setup the database and Base class
Base = declarative_base()
engine = create_engine('sqlite:///:memory:')  # Using an in-memory SQLite database
Session = sessionmaker(bind=engine)
session = Session()

# Definition of the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create the table
Base.metadata.create_all(engine)

# Insert a sample Recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix flour and water.")
session.add(new_recipe)
session.commit()

# Query a Recipe instance
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # For example, to access the 2nd column (instructions)
nth_value = getattr(r, r.__table__.columns.keys()[n])
print(f"The {n}th column value is: {nth_value}")
