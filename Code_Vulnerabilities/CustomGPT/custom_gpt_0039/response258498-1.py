
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database engine and session
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding a recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value (e.g., 0 for title, 1 for instructions)
def get_nth_column_value(instance, n):
    return list(instance.__dict__.values())[n]

# Get instructions (nth column)
instructions = get_nth_column_value(r, 2)  # Adjust index based on your needs
print(instructions)  # Output: "Mix ingredients and cook."
