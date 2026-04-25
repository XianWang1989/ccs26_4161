
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database (in-memory for this example)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe to the database
new_recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(new_recipe)
session.commit()

# Query the recipe instance
r = session.query(Recipe).first()

# Function to get nth column
def get_nth_column(instance, n):
    return getattr(instance, instance.__table__.columns[n].name)

# Example usage
nth_index = 1  # For the second column (index 1)
value = get_nth_column(r, nth_index)
print(value)  # Output: Pasta
