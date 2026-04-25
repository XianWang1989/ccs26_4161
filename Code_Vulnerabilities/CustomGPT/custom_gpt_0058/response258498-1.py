
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (you might already have this)
engine = create_engine('sqlite:///:memory:')  # Using an in-memory SQLite database
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add an example recipe
example_recipe = Recipe(title="Pasta", instructions="Boil pasta and add sauce.")
session.add(example_recipe)
session.commit()

# Query to get the recipe
r = session.query(Recipe).first()

# Accessing the nth column (for example, 2nd column: instructions)
n = 2  # Change this to the column index you want (0-indexed)
column_value = list(r.__table__.columns.keys())[n]  # Get the column name
nth_value = getattr(r, column_value)  # Get the value of the nth column

print(f"The value of the {n}th column (which is '{column_value}') is: {nth_value}")
