
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database (example with SQLite)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a recipe for demonstration
new_recipe = Recipe(title='Pasta', instructions='Boil water, cook pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Getting the nth column (0-indexed)
n = 2  # For example, to get the 'instructions'
column_name = r.__table__.columns.keys()[n]
nth_value = getattr(r, column_name)

print(f'The {n+1}th column value is: {nth_value}')
