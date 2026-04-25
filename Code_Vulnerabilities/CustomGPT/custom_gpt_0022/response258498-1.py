
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Sample setup for the database
engine = create_engine('sqlite:///:memory:')  # Using in-memory SQLite for demonstration
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column
def get_nth_column(instance, n):
    # Get the list of attributes and their values
    attributes = list(instance.__mapper__.c)
    return getattr(instance, attributes[n].name) if n < len(attributes) else None

# Example usage: Get the 1st column (title)
nth_value = get_nth_column(r, 1)
print(nth_value)  # Output: Pasta
