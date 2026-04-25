
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setting up the SQLite database for demonstration
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water and cook pasta.')
session.add(new_recipe)
session.commit()

# Querying for the recipe
r = session.query(Recipe).first()

# Accessing the nth column value (1 for title, 2 for instructions)
nth_column_value = list(r.__dict__.values())[1]  # 1 for title, 2 for instructions

print(nth_column_value)  # Output will be 'Pasta'
