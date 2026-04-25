
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example usage
r = Recipe(id=1, title='Pasta', instructions='Boil water and cook pasta.')

# Accessing the nth column value
# Assuming n = 2 (which corresponds to instructions based on the order)
n = 2
column_name = list(r.__dict__.keys())[n]  # Get the nth column name
nth_value = r.__dict__[column_name]  # Get the value of that column

print(f"The {n}th column '{column_name}' has the value: {nth_value}")
