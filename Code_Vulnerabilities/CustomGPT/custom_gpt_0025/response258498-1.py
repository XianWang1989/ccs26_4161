
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Database setup (replace with your database connection string)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water and cook pasta.')
session.add(new_recipe)
session.commit()

# Query to get the first recipe
r = session.query(Recipe).first()

# Function to get the nth column value
def get_nth_column(instance, n):
    return list(instance.__dict__.values())[n]

# Example usage
nth_value = get_nth_column(r, 2)  # Adjust the index based on your columns
print(nth_value)  # Prints: Boil water and cook pasta.
