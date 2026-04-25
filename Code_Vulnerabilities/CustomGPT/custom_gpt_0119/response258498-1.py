
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Creating a SQLAlchemy engine and session
engine = create_engine('sqlite:///:memory:')  # example for SQLite in-memory database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample entry
new_recipe = Recipe(title='Pasta', instructions='Boil water, add pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # Example: change this to access different columns
column_value = list(r.__dict__.values())[n]
print(column_value)  # Output will be the value of the nth column (e.g. 'Boil water, add pasta.')
