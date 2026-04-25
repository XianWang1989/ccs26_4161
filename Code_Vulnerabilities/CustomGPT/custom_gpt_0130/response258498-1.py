
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Database setup (example connection string)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example usage
# Create a recipe instance
recipe = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Access the nth column value (e.g., instructions)
n = 2  # For instructions
column_value = list(r.__dict__.values())[n]
print(column_value)  # Output: Boil water, add pasta.
