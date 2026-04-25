
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database and session
engine = create_engine('sqlite:///:memory:')  # Example in-memory SQLite database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example data
new_recipe = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column
def get_nth_column(instance, n):
    return list(instance.__dict__.values())[n - 1]  # n is 1-indexed

# Example usage
print(get_nth_column(r, 2))  # Outputs: "Pasta"
print(get_nth_column(r, 3))  # Outputs: "Boil water, add pasta."
