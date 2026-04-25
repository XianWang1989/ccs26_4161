
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the SQLAlchemy base and engine
Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite database in memory (for demonstration)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Query to get the first recipe
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column(instance, n):
    # Get the list of columns in order
    columns = list(instance.__table__.columns)
    # Return the value of the nth column (adjusting for zero indexing)
    return getattr(instance, columns[n].name)

# Example usage: Get the 1st (instructions) value
nth_value = get_nth_column(r, 2)  # Change to 0 for id, 1 for title, 2 for instructions
print(nth_value)  # Should output: Mix ingredients and cook.
