
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Database setup (modify the connection string as needed)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Example usage
session = Session()

# Add a sample recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix flour and water.")
session.add(new_recipe)
session.commit()

# Query for the recipe
r = session.query(Recipe).first()

# Get the nth column value
n = 2  # For example, to get instructions which is the 2nd column (index 1)
nth_value = list(r.__dict__.values())[n]

print(nth_value)  # Output: "Mix flour and water."
