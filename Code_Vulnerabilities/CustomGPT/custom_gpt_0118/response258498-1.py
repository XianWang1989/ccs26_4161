
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup to create an SQLite database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(new_recipe)
session.commit()

# Query to get the recipe instance
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column(instance, n):
    # Convert instance to list of its values
    values = list(instance.__dict__.values())
    # Return the nth value (excluding the SQLAlchemy internal state)
    return values[n+1]  # +1 to skip the instance state

# Get the value of the 2nd column (instructions)
nth_value = get_nth_column(r, 2)
print(nth_value)  # Output: Boil water, add pasta.
