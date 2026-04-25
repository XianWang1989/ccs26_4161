
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

# Example function to get nth column value
def get_nth_column_value(recipe_instance, n):
    # Access nth column value using the columns attribute
    columns = list(recipe_instance.__table__.columns)
    if n < 0 or n >= len(columns):
        raise IndexError("Column index out of range")
    return getattr(recipe_instance, columns[n].name)

# Database setup (example)
# engine = create_engine('sqlite:///:memory:')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# Example usage
# r = session.query(Recipe).first()  # Assuming you fetched a recipe instance
# nth_value = get_nth_column_value(r, 1)  # Get the 2nd column value (instructions)
# print(nth_value)
