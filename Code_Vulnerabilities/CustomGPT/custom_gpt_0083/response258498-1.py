
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (replace with your database URI)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding sample data
new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(new_recipe)
session.commit()

# Querying the Recipe instance
r = session.query(Recipe).first()

# Accessing nth column value using __dict__
def get_nth_column_value(instance, n):
    return list(instance.__dict__.values())[n]

# Example usage: Get the 2nd column value (0-indexed)
nth_value = get_nth_column_value(r, 2)  # This will get "Boil water and cook pasta."
print(nth_value)
