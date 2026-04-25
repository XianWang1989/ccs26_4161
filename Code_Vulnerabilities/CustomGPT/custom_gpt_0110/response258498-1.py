
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Database setup (use your actual database URL)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example data insertion
recipe = Recipe(title='Pasta', instructions='Boil water and add pasta.')
session.add(recipe)
session.commit()

# Querying a recipe
r = session.query(Recipe).first()

# Accessing the nth column (0-based indexing)
n = 2  # for 'instructions'
nth_value = getattr(r, r.__table__.columns.keys()[n])
print(nth_value)  # Output: Boil water and add pasta.
