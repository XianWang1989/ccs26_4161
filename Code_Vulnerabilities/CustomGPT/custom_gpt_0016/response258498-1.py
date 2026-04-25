
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Assuming an SQLite in-memory database for demonstration purposes
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Creating and adding a sample Recipe instance
new_recipe = Recipe(title='Pasta', instructions='Boil water; add pasta.')
session.add(new_recipe)
session.commit()

# Querying the Recipe instance
r = session.query(Recipe).first()

# Getting the nth column value
def get_nth_column(instance, n):
    # Get all column names in the order they are defined
    column_names = Recipe.__mapper__.c.keys()
    if n < 0 or n >= len(column_names):
        raise IndexError("Column index out of range.")

    # Use the column name to access the value
    column_name = column_names[n]
    return getattr(instance, column_name)

# Example usage
nth_value = get_nth_column(r, 2)  # This will fetch the 'instructions'
print(f"The 2nd column value is: {nth_value}")
