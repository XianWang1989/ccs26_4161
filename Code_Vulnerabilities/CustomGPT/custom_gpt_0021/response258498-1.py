
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example usage
engine = create_engine('sqlite:///:memory:')  # Replace with your database URL
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a recipe instance for demonstration
new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(new_recipe)
session.commit()

# Fetch the recipe instance
r = session.query(Recipe).first()

# Access the nth column value (e.g., instructions which is the 2nd column)
n = 2  # Index starts from 0
nth_value = getattr(r, r.__table__.columns.keys()[n])
print(nth_value)  # Outputs: "Boil water and cook pasta."
