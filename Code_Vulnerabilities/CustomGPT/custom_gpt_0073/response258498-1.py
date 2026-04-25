
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example code to query a recipe
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

# Assuming `r` is a Recipe instance obtained from a query
# Here’s how you can get the nth column value
r = session.query(Recipe).first()  # Fetch the first recipe (for example)
n = 2  # For example, 0 = id, 1 = title, 2 = instructions

# Access nth column (adjusting for zero-based index)
nth_column_value = list(r.__dict__.values())[n + 1]  # +1 to skip _sa_instance_state
print(nth_column_value)
