
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setting up the database and base class
Base = declarative_base()
engine = create_engine('sqlite:///:memory:')  # Replace with your database URL
Session = sessionmaker(bind=engine)
session = Session()

# Defining the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create the table
Base.metadata.create_all(engine)

# Example of adding a recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Querying for the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
def get_nth_column_value(instance, n):
    # n must be less than the number of columns
    if 0 <= n < len(instance.__table__.columns):
        column_name = instance.__table__.columns.keys()[n]
        return getattr(instance, column_name)
    else:
        raise IndexError("Column index out of range")

# Example usage
try:
    print(get_nth_column_value(r, 0))  # Outputs the value of 'id'
    print(get_nth_column_value(r, 1))  # Outputs the value of 'title'
    print(get_nth_column_value(r, 2))  # Outputs the value of 'instructions'
except IndexError as e:
    print(e)
