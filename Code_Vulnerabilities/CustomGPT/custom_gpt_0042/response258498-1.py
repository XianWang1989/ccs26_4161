
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the Recipe class
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database (replace with your database URL)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe to the database
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Function to get the n-th column value
def get_nth_column(instance, n):
    return list(instance.__table__.columns.items())[n][1].name, getattr(instance, list(instance.__table__.columns.keys())[n]) 

# Get the 2nd column (0-based index)
column_index = 2  # For 'instructions'
column_name, column_value = get_nth_column(r, column_index)

print(f"{column_name}: {column_value}")
