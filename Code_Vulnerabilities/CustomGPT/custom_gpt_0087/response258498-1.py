
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example for getting nth column value
def get_nth_column(instance, n):
    # Convert to a list of column attributes
    columns = list(instance.__dict__.keys())
    # Check if n is within the valid range
    if 0 <= n < len(columns):
        return getattr(instance, columns[n])
    else:
        raise IndexError("Column index out of range")

# Example usage
# Assume you have a SQLAlchemy session established
# session = sessionmaker(bind=create_engine('your_database_url'))()
# r = session.query(Recipe).first()  # Get the first recipe
# nth_value = get_nth_column(r, 2)  # Get the value of the 3rd column (index 2)
# print(nth_value)

