
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database (replace with your database URI)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example to add a recipe and retrieve it
recipe = Recipe(title='Pasta', instructions='Boil water and cook pasta.')
session.add(recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value (e.g., instructions)
n = 2  # For the 'instructions' column
column_value = getattr(r, r.__table__.columns.items()[n][0])
print(column_value)  # Outputs: Boil water and cook pasta.
