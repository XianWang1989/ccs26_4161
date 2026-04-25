
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

    def __getitem__(self, index):
        # Create a list of column attributes
        columns = [self.id, self.title, self.instructions]
        return columns[index]

# Set up the database (example with SQLite)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example data
recipe = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
print(r[0])  # Output: 1 (id)
print(r[1])  # Output: 'Pasta' (title)
print(r[2])  # Output: 'Boil water, add pasta.' (instructions)
