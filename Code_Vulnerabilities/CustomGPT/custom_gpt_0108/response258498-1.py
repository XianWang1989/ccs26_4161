
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example Database Setup (adjust as needed)
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite for demonstration
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water and add pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
# Method 1: Using __dict__
nth_value = list(r.__dict__.values())[1]  # 1 is the index for the 2nd column (after id)

# Method 2: Using values() method
nth_value = list(r.__dict__.values())[1]  # Adjust index as needed

print(nth_value)  # Output the 2nd column value (instructions)
