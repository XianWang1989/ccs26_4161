
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database (example)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example data
new_recipe = Recipe(title='Pancakes', instructions='Mix and fry.')
session.add(new_recipe)
session.commit()

# Querying the instance
r = session.query(Recipe).first()

# Accessing the nth column (e.g., 1 for title, 2 for instructions)
n = 2  # assuming 1-based index for user understanding
column_value = list(r.__dict__.values())[n]
print(column_value)  # Output: 'Mix and fry.'
