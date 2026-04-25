
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup database and session
engine = create_engine('sqlite:///:memory:')  # Using in-memory SQLite for demonstration
Base.metadata.create_all(engine)  # Create the table
Session = sessionmaker(bind=engine)
session = Session()

# Insert a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water, cook pasta.')
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column(instance, n):
    columns = list(instance.__table__.columns)  # Get all columns in order
    return getattr(instance, columns[n].name)  # Use the column name to access the value

# Example usage
nth_value = get_nth_column(r, 2)  # This will retrieve the value of the 'instructions' column
print(nth_value)  # Output: 'Boil water, cook pasta.'
