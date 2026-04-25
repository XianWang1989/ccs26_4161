
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup, replace 'sqlite:///:memory:' with your database URL
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water, add pasta")
session.add(new_recipe)
session.commit()

# Query an instance
r = session.query(Recipe).first()

# Access the nth column value
n = 2  # For example, we want the 2nd column (instructions)
column_value = getattr(r, Recipe.__table__.columns.items()[n][0])

print(f"The {n}th column value is: {column_value}")
