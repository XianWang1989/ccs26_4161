
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup - creating a database in memory and adding a recipe
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a recipe to the database
new_recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(new_recipe)
session.commit()

# Querying the recipe instance
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column_value(instance, n):
    # Get a list of column names in the order they were defined
    column_names = [column.name for column in Recipe.__table__.columns]
    # Get attribute value based on the nth index
    try:
        return instance.__dict__[column_names[n]]
    except IndexError:
        return None  # Return None if n is out of index

# Example usage
nth_value = get_nth_column_value(r, 2)  # Get the value of the 2nd column (instructions)
print(nth_value)  # Output: Boil water and add pasta.
