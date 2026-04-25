
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database (this is just an example, replace with your database URL)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Access the nth column
def get_nth_column(instance, n):
    # Using 'inspect' to get the column names
    mapper = inspect(instance.__class__)
    column_names = [column.name for column in mapper.columns]
    return getattr(instance, column_names[n])

# Example usage to get the 1st column's value (0-based index)
nth_value = get_nth_column(r, 1)  # This will get 'Pasta', which is r.title
print(nth_value)
