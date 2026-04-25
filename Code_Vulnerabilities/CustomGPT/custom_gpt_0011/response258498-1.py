
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database engine and session
engine = create_engine('sqlite:///:memory:')  # Using in-memory SQLite for demonstration
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding a recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing nth column value
# Convert the object to a list of its values
column_values = [r.id, r.title, r.instructions]

# Accessing the 2nd column (index 1)
nth_value = column_values[1]  # This will give you 'Pasta'
print(nth_value)  # Output: Pasta
