
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class and the Recipe model
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

# Example data insertion
session.add(Recipe(title="Pasta", instructions="Boil water, add pasta."))
session.commit()

# Querying the first recipe
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # For example, to get the 'instructions'
column_value = list(r.__dict__.values())[n]  # Accessing by index
print(column_value)  # Output: 'Boil water, add pasta.'
