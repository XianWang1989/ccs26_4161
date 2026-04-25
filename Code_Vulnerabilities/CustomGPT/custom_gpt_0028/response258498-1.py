
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Sample database setup (adjust URL as necessary)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example query to add and retrieve a recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water, add pasta.')
session.add(new_recipe)
session.commit()

# Retrieve the first recipe instance
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column(instance, n):
    if n < 0 or n >= len(instance.__table__.columns):
        raise IndexError("Column index out of range.")
    return getattr(instance, instance.__table__.columns.keys()[n])

# Accessing the nth column value
try:
    nth_value = get_nth_column(r, 1)  # 1 for 'title', 2 for 'instructions'
    print(nth_value)
except IndexError as e:
    print(e)
