
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database and session (example with SQLite)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water, cook pasta.")
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Access the nth column (e.g., 1 for title, 2 for instructions)
def get_nth_column(instance, n):
    return getattr(instance, instance.__table__.columns.keys()[n])

# Example Usage
nth_column_value = get_nth_column(r, 2)  # Accessing the 'instructions' column
print(nth_column_value)  # Output: 'Boil water, cook pasta.'
