
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an engine and a session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column(instance, n):
    return list(instance.__dict__.values())[n]

# Example usage
nth_value = get_nth_column(r, 2)  # Get the value of 'instructions'
print(nth_value)  # Output: Mix ingredients and cook.
