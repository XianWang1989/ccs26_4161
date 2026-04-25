
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup
engine = create_engine('sqlite:///:memory:')  # Replace with your database URI
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example query to get a Recipe instance
recipe_instance = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(recipe_instance)
session.commit()

# Accessing the nth column value
n = 2  # Example: index for instructions (0 = id, 1 = title, 2 = instructions)
nth_column_value = list(recipe_instance.__mapper__.columns)[n].value(recipe_instance)

print(f"The {n}th column value is: {nth_column_value}")
