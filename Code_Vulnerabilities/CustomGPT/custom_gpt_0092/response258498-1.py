
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create a database engine and session (for demonstration purposes)
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Access the nth column (e.g., instructions as the 2nd column)
n = 2
nth_column_value = getattr(r, r.__table__.columns.keys()[n])
print(nth_column_value)  # Outputs: "Boil water and add pasta."
