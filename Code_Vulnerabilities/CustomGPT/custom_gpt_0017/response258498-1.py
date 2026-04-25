
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

# Create an in-memory SQLite database for demonstration
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(recipe)
session.commit()

# Query the recipe instance
r = session.query(Recipe).first()

# Function to get the nth column value
def get_nth_column(instance, n):
    # Get the column names in order
    columns = list(instance.__table__.columns)
    # Access the nth column value (0-based)
    return getattr(instance, columns[n].name)

# Get the 2nd column value (0-based index: 1)
nth_value = get_nth_column(r, 1)
print(nth_value)  # Output: "Pasta"
