
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an engine and session
engine = create_engine('sqlite:///:memory:')  # Example in-memory SQLite database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Access nth column value
def get_nth_column_value(instance, n):
    return list(vars(instance).values())[n]

# Get the value of the nth column (e.g., index 2 for instructions)
nth_value = get_nth_column_value(r, 2)  # Should return the instructions
print(nth_value)
