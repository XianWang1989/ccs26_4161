
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example session setup (assuming you have a database setup)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water and cook pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
def get_nth_column(instance, n):
    return list(instance.__dict__.items())[n][1]

# Example usage
nth_instruction = get_nth_column(r, 2)  # Adjust the index as needed
print(nth_instruction)  # Outputs: 'Boil water and cook pasta.'
