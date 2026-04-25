
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite engine and session
engine = create_engine('sqlite:///:memory:')  # Replace with your database URL
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Assuming you've added a recipe instance to the session
new_recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(new_recipe)
session.commit()

# Querying the instance
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # For the instructions (0-indexed), this is the 2nd column
nth_value = getattr(r, r.__table__.columns.keys()[n])

print(nth_value)  # Output: "Boil water and add pasta."
