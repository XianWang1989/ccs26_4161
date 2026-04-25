
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example database setup
engine = create_engine('sqlite:///:memory:')  # Use a real database URL
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example of querying a Recipe instance
recipe = Recipe(title='Pancakes', instructions='Mix and cook.')
session.add(recipe)
session.commit()

# Fetch the recipe instance
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column(instance, n):
    if n < 0 or n >= len(instance.__table__.columns):
        raise IndexError("Column index out of range.")
    column_name = instance.__table__.columns.keys()[n]
    return getattr(instance, column_name)

# Example to access the 2nd column (instructions)
nth_value = get_nth_column(r, 2)  # Column index 2 refers to 'instructions'
print(nth_value)
