
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create a mock engine and session for demonstration purposes
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example data
new_recipe = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(new_recipe)
session.commit()

# Query the first recipe
r = session.query(Recipe).first()

# Accessing the nth column (e.g., instructions as the second column)
column_names = ['id', 'title', 'instructions']  # List of column names in order
n = 2  # Example for the second column (instructions)

# Retrieve the nth column value
nth_value = r.__dict__[column_names[n]]
print(nth_value)  # Output: Boil water, add pasta.
