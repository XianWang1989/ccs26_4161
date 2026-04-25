
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Assuming you have a database and the table is created
engine = create_engine('sqlite:///:memory:')  # Example engine
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a recipe instance
new_recipe = Recipe(title='Pancakes', instructions='Mix ingredients and fry.')
session.add(new_recipe)
session.commit()

# Querying the recipe instance
r = session.query(Recipe).first()

# Fetching the nth column value (e.g., instructions)
# Get the column names
column_names = Recipe.__table__.columns.keys()

# Get the nth column value by index
n = 2  # For example, to get the 'instructions' which is the third column (index 2)
nth_column_value = r.__dict__[column_names[n]]

print(f"The {n}th column value is: {nth_column_value}")
