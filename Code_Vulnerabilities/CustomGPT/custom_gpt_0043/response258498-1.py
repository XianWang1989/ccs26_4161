
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (make sure to configure your database URL)
engine = create_engine('sqlite:///:memory:')  # Using in-memory SQLite for this example
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column
def get_nth_column(instance, n):
    # Get all columns from the model
    columns = list(instance.__mapper__.c.keys())
    if n < len(columns):
        return getattr(instance, columns[n])
    else:
        raise IndexError("Index out of range for recipe columns.")

# Example usage
nth_index = 2  # Example for third column (0-based index)
try:
    value = get_nth_column(r, nth_index)
    print(f"The value of the {nth_index + 1}th column is: {value}")
except IndexError as e:
    print(e)
