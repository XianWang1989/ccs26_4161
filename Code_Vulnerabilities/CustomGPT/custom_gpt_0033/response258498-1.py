
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database engine and session
engine = create_engine('sqlite:///:memory:')  # Example using in-memory SQLite
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
new_recipe = Recipe(title='Pancakes', instructions='Mix ingredients and cook.')
session.add(new_recipe)
session.commit()

# Query to fetch the instance
r = session.query(Recipe).first()

# Accessing the nth column value (index starts from 0)
n = 2  # For example, accessing instructions (2nd column)
nth_value = list(r.__mapper__.columns)[n].accessor.get(r)

print(f'The {n}th column value is: {nth_value}')
