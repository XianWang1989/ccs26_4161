
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (adjust the connection string as necessary)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a sample recipe and add it to the session
new_recipe = Recipe(title='Pancakes', instructions='Mix ingredients and cook.')
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column(instance, n):
    return list(instance.__mapper__.iterate_properties)[n].key

# Accessing the nth column value
nth_column_index = 2  # For instructions (index starts at 0)
nth_value = getattr(r, get_nth_column(r, nth_column_index))
print(nth_value)  # Output: Mix ingredients and cook.
