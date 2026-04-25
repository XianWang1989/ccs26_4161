
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Creating a new SQLite database (or connecting to an existing one)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water, cook pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
def get_nth_value(instance, n):
    return list(instance.__dict__.values())[n]

# Example: Get the value of the 'instructions' column (2nd index)
nth_value = get_nth_value(r, 2)
print(nth_value)  # Output: Boil water, cook pasta.
