
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create a session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example data insert
recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(recipe)
session.commit()

# Querying a Recipe instance
r = session.query(Recipe).first()

# Accessing the nth column value (e.g., 0 for id, 1 for title, 2 for instructions)
def get_nth_column(instance, n):
    return list(instance.__dict__.values())[n]

# Example usage
nth_value = get_nth_column(r, 2)  # Get the 'instructions' column
print(nth_value)  # Output: Boil water and cook pasta.
