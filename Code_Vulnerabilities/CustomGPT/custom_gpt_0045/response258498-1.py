
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database (for example purpose, not running)
engine = create_engine('sqlite:///:memory:')  # Use an in-memory SQLite database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water, add pasta")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
def get_nth_column(instance, n):
    columns = list(instance.__dict__.keys())[1:]  # Skip the first key which is '_sa_instance_state'
    return getattr(instance, columns[n]) if n < len(columns) else None

# Example usage
nth_column_value = get_nth_column(r, 2)  # Get the 2nd column (instructions)
print(nth_column_value)  # Output: Boil water, add pasta
