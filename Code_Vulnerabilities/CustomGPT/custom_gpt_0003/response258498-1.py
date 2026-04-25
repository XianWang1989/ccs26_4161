
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create engine and session (replace with your database connection)
engine = create_engine('sqlite:///:memory:')  # Example in-memory SQLite database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample entry to the database
new_recipe = Recipe(title="Pancakes", instructions="Mix the ingredients and cook.")
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Access the nth column value (for example, instructions which is the second column)
n = 2  # For 0-based index, where 0 is id, 1 is title, and 2 is instructions
column_value = list(vars(r).values())[n]

print(f"The {n}th column value is: {column_value}")
