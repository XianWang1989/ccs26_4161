
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database engine and session
engine = create_engine('sqlite:///:memory:')  # Example with an in-memory SQLite database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example to add a recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Access nth column value
n = 2  # For instance, we want the instructions (which is the 3rd column)
column_value = list(r.__table__.columns)[n].name  # Get column name by index
value = getattr(r, column_value)  # Access the value dynamically

print(f"Column name: {column_value}, Value: {value}")
