
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Assuming you have a recipe instance
r = Recipe(id=1, title="Pancakes", instructions="Mix ingredients and cook.")

# Convert to dictionary and get the nth column value
recipe_dict = r.__dict__
nth_column_value = list(recipe_dict.values())[2]  # Assuming n=2

print(nth_column_value)  # Outputs: Mix ingredients and cook.
