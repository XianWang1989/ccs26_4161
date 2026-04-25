
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite database in memory for demonstration
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add an example recipe
new_recipe = Recipe(title='Pancakes', instructions='Mix ingredients and cook.')
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Accessing the nth column (e.g., instructions)
def get_nth_column(instance, n):
    return list(instance.__dict__.values())[n]

# Get the nth column value (0 for id, 1 for title, 2 for instructions)
nth_value = get_nth_column(r, 2)
print(nth_value)  # Outputs: Mix ingredients and cook.
