
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Creating a sample SQLite in-memory database for demonstration
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a recipe
session.add(Recipe(title='Pasta', instructions='Boil water and cook pasta.'))
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Access nth column (e.g., 1 for title, 2 for instructions)
n = 2  # Change this to 1 for title
column_value = list(r.__dict__.values())[n]
print(column_value)  # Output: "Boil water and cook pasta."
