
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database engine and session
engine = create_engine('sqlite:///:memory:')  # Example using an in-memory SQLite database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example instance creation
new_recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(new_recipe)
session.commit()

# Querying the instance
r = session.query(Recipe).first()

# Accessing the nth column (0-indexed)
n = 2  # for example, to get the 'instructions'
columns = [r.id, r.title, r.instructions]  # List of column values
nth_value = columns[n]  # Get the nth value

print(f"The {n+1}th column value is: {nth_value}")
