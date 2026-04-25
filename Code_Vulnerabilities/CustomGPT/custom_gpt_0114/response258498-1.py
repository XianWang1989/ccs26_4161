
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (adjust the database URL as necessary)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Getting the nth column value (e.g., instructions)
n = 2  # 0-indexed, so 0 is 'id', 1 is 'title', 2 is 'instructions'
columns = list(r.__dict__.items())
nth_column_value = columns[n][1]  # Get the value of the nth column

print(nth_column_value)  # Output: Boil water and cook pasta.
