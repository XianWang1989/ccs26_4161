
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database connection and session
engine = create_engine('sqlite:///:memory:')  # Example using an in-memory SQLite database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water, add pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Getting the nth column value
n = 1  # For example, to get the title
column_value = list(r.__dict__.values())[n + 1]  # +1 to account for the SQLAlchemy internal state

print(column_value)  # Output: 'Pasta'
