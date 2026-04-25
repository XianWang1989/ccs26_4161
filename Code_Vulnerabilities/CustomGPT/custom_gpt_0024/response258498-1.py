
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setting up the database
engine = create_engine('sqlite:///:memory:')  # Example using in-memory SQLite
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and add spaghetti.")
session.add(new_recipe)
session.commit()

# Querying the first recipe
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # e.g., to get 'instructions'
column_value = list(r.__dict__.values())[n]  # Get nth item from values

print(f'The value of the {n}th column is: {column_value}')
