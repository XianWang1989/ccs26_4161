
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (use your actual database URL)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(new_recipe)
session.commit()

# Fetching the recipe instance
r = session.query(Recipe).first()

# Access the nth column value (0-based index)
n = 1  # For the 'instructions' column
nth_column_value = list(r.__dict__.values())[n + 1]  # +1 to skip the SQLAlchemy internal state

print(nth_column_value)  # Output: Boil water and cook pasta.
