
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example of creating a session and querying the database
engine = create_engine('sqlite:///:memory:')  # Use an in-memory SQLite database for demonstration
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding an example recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water, add pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column
n = 2  # For example, to access 'instructions' which is the 2nd column (index 1)
nth_column_value = list(r.__dict__.values())[n]
print(nth_column_value)  # Outputs: 'Boil water, add pasta.'
