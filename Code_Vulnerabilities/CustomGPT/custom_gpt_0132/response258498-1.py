
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Creating a new SQLite database (change as needed)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title='Pancakes', instructions='Mix ingredients and cook.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column
def get_nth_column(instance, n):
    column_keys = list(instance.__class__.__dict__.keys())[1:]  # Skip 'metadata'
    if n < len(column_keys):
        return getattr(instance, column_keys[n])
    else:
        return None

# Example: Get the first and then second column
first_column_value = get_nth_column(r, 0)  # r.title
second_column_value = get_nth_column(r, 1)  # r.instructions

print(first_column_value)  # Output: Pancakes
print(second_column_value)  # Output: Mix ingredients and cook.
