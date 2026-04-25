
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Creating session for demonstration
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding an example recipe
recipe = Recipe(title="Pasta", instructions="Boil water and add pasta.")
session.add(recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value (e.g., 1 for instructions)
n = 1  # 0 for id, 1 for title, 2 for instructions
nth_value = list(vars(r).values())[n]

print(nth_value)  # Output: "Pasta" (for title)
