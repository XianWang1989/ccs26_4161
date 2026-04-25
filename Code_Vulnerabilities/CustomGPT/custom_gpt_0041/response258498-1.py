
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup database (replace with your database URI)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Fetch the recipe instance
r = session.query(Recipe).first()

# Function to get the nth column value
def get_nth_column(instance, n):
    columns = inspect(instance).mapper.column_attrs
    return getattr(instance, columns[n].key) if n < len(columns) else None

# Example usage
nth_value = get_nth_column(r, 2)  # Access the 3rd column (index 2)
print(nth_value)  # Output: "Mix ingredients and cook."
