
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example usage
recipe_instance = Recipe(id=1, title='Pancakes', instructions='Mix ingredients and cook.')
session.add(recipe_instance)
session.commit()

# Access the nth column value (for example, 2nd column)
n = 1  # change as needed for 0-based index
column_value = list(recipe_instance.__dict__.values())[n]
print(column_value)  # Output: 'Pancakes'
