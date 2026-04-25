
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example usage
engine = create_engine('sqlite:///:memory:')  # in-memory SQLite database
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
recipe = Recipe(title='Pasta', instructions='Boil water, add pasta.')
session.add(recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Get the nth column value (for example, n=1 for the second column, instructions)
n = 2  # 1-based index for nth column
column_value = getattr(r, r.__table__.columns.keys()[n-1])

print(column_value)  # Output: Boil water, add pasta.
