
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setup the base and engine
Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)  # Using an in-memory SQLite database
Session = sessionmaker(bind=engine)
session = Session()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create the table
Base.metadata.create_all(engine)

# Add a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water, add pasta, cook for 10 minutes.')
session.add(new_recipe)
session.commit()

# Perform the query
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # example index (0-based), 0: id, 1: title, 2: instructions
nth_value = getattr(r, r.__table__.columns.keys()[n])

# Print the nth column value
print(f'The {n}th column value is: {nth_value}')
