
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base
Base = declarative_base()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite database in memory for this example
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Set up a session
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title='Pancakes', instructions='Mix ingredients and cook.')
session.add(new_recipe)
session.commit()

# Query the recipe
recipe_instance = session.query(Recipe).first()

# Function to get nth column
def get_nth_column(instance, n):
    # Adjust n for 0-based indexing
    column_name = list(instance.__class__.__table__.columns.keys())[n]
    return getattr(instance, column_name)

# Example usage: Get the 2nd column (instructions)
nth_value = get_nth_column(recipe_instance, 2)
print(nth_value)  # Output: Mix ingredients and cook.
