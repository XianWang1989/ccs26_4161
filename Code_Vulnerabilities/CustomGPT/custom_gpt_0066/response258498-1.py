
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Database setup (example with SQLite in-memory)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add an example recipe
recipe = Recipe(title='Pasta', instructions='Boil water and add pasta.')
session.add(recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column(instance, n):
    return list(instance.__dict__.items())[n][1]

# Accessing the nth column
nth_value = get_nth_column(r, 2)  # Index 2 for 'instructions'
print(nth_value)  # Output: Boil water and add pasta.
