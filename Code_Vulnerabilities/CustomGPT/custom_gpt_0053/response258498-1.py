
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (replace with your database URL)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Access nth column (e.g., 2nd column)
nth_value = list(r.__dict__.values())[1]  # Index 1 for the 2nd column 'title'
print(nth_value)  # Output: Pancakes
