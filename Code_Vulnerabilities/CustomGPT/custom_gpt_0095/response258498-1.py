
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database (example with SQLite in-memory database)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample Recipe instance
new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(new_recipe)
session.commit()

# Querying the Recipe
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # For example, 0 is id, 1 is title, 2 is instructions
column_value = list(r.__dict__.values())[n + 1]  # Skip the _sa_instance_state
print(column_value)  # Output: Boil water and cook pasta.
