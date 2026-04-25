
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
engine = create_engine('sqlite:///:memory:')  # Using an in-memory SQLite database for this example
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding a recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(new_recipe)
session.commit()

# Querying the instance
r = session.query(Recipe).first()

# Accessing the nth column value
def get_nth_column(instance, n):
    columns = list(instance.__table__.columns)  # Get the column objects
    if n < len(columns):
        return getattr(instance, columns[n].name)  # Use getattr to access the value
    else:
        raise IndexError("Column index out of range")

# For example, to get instructions which is the 2nd column (index 1)
instructions_value = get_nth_column(r, 1)
print(instructions_value)  # Output: Boil water and add pasta.
