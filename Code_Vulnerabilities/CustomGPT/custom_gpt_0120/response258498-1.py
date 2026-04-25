
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database and session (example with SQLite)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add an example recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water and cook pasta.')
session.add(new_recipe)
session.commit()

# Query a recipe
r = session.query(Recipe).first()

# Function to get the nth column value
def get_nth_column(instance, n):
    return getattr(instance, instance.__table__.columns.keys()[n])

# Usage
nth_value = get_nth_column(r, 2)  # Accessing the 2nd column (instructions)
print(nth_value)  # Output: Boil water and cook pasta.
