
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setting up the database (example SQLite in memory)
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

# Accessing the nth column value
# Method 1: Using __dict__
n = 2  # For instructions (index starts at 0)
nth_value = list(r.__dict__.values())[n]
print(f"Nth value using __dict__: {nth_value}")

# Method 2: Using keys() method
nth_column_name = list(Recipe.__table__.columns)[n].name
nth_value_by_key = getattr(r, nth_column_name)
print(f"Nth value using keys(): {nth_value_by_key}")
