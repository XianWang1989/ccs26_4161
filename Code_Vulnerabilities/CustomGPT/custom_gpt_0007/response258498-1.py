
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create engine and session
engine = create_engine('sqlite:///:memory:')  # Using an in-memory SQLite database for demonstration
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample entry
new_recipe = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Access the nth column value (e.g., 0: id, 1: title, 2: instructions)
n = 2  # Change this as needed
nth_column_value = list(r.__mapper__.columns)[n]
nth_value = getattr(r, nth_column_value.name)

print(f"The value of the {n}th column is: {nth_value}")
