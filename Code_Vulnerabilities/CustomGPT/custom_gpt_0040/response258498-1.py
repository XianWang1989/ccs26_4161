
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database connection and session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example: Add a sample recipe
new_recipe = Recipe(title='Pancakes', instructions='Mix ingredients and cook.')
session.add(new_recipe)
session.commit()

# Query the first recipe
r = session.query(Recipe).first()

# Get the nth column value
def get_nth_column(instance, n):
    # Get the columns in the class
    columns = [column.name for column in instance.__table__.columns]
    # Return the nth column value
    return getattr(instance, columns[n])

# Example usage
n = 1  # Example: get the 'instructions'
nth_value = get_nth_column(r, n)
print(nth_value)  # Output: Mix ingredients and cook.
