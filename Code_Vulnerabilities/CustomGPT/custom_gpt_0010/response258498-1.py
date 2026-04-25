
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database (for example purposes, using SQLite)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding example data
session.add(Recipe(title="Pasta", instructions="Boil and sauté."))
session.commit()

# Query an instance of Recipe
r = session.query(Recipe).first()

# Accessing nth column value (0-indexed)
n = 2  # For example, to get 'instructions'
column_value = list(r._sa_instance_state.dict.keys())[n]  # Gets the column name

# Print the value of the nth column
print(getattr(r, column_value))
