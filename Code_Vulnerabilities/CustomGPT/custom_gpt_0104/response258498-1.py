
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup for creating the database and session
engine = create_engine('sqlite:///:memory:') # In-memory SQLite database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding an example recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing nth column value (for example, index 1 for title)
n = 1  # Change this value to get a different column (0 for id, 1 for title, 2 for instructions)
column_names = ['id', 'title', 'instructions']
if n < len(column_names):
    nth_value = r.__dict__[column_names[n]]
    print(f"The value of the column at index {n} is: {nth_value}")
else:
    print("Column index out of range.")
