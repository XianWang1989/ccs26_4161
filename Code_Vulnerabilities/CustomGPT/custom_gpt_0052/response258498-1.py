
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database connection
engine = create_engine('sqlite:///:memory:')  # Use your database URL
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding a recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water and cook pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column(instance, n):
    return getattr(instance, instance.__table__.columns.keys()[n])

# Example usage: Get instructions (which is the 2nd column, index 1)
nth_value = get_nth_column(r, 2)
print(nth_value)  # Output: Boil water and cook pasta.
