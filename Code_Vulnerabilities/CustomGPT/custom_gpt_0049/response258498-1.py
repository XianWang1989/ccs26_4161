
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Assuming you have an instance of Recipe
r = Recipe(id=1, title="Pasta", instructions="Boil water and add pasta.")

# Getting the nth column value. For example, to get the instructions.
n = 2  # Index for the nth column (0-based index)
column_value = list(r.__table__.columns.items())[n][1].expression
nth_value = getattr(r, column_value.name)

print(f"The value of the nth column is: {nth_value}")
