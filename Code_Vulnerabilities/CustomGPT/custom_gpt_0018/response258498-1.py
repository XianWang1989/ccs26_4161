
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Assuming you have a recipe instance:
r = Recipe(title="Chocolate Cake", instructions="Mix ingredients and bake")

# Getting the nth column value (0-based index)
def get_nth_column_value(instance, n):
    return list(instance.__dict__.values())[n]

# Example usage:
nth_value = get_nth_column_value(r, 1)  # This will get r.title
print(nth_value)  # Output: Chocolate Cake
