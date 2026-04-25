
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create a new SQLite database (in-memory for example)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example: Add a recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Fetch the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # for example, to get 'instructions'
columns = list(Recipe.__table__.columns)

# Get the nth column's value
nth_value = getattr(r, columns[n].name)
print(nth_value)  # Outputs: Mix ingredients and cook.
