
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (make sure to change the connection string)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(new_recipe)
session.commit()

# Fetching the recipe instance
r = session.query(Recipe).first()

# Getting the nth column value
def get_nth_column(instance, n):
    return list(instance.__dict__.values())[n]

# Accessing the 2nd column (0-based indexing)
nth_value = get_nth_column(r, 2)
print(nth_value)  # Output: "Boil water and add pasta."
