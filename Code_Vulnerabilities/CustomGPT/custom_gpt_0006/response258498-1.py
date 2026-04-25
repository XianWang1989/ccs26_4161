
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup the database (adjust the URL as needed)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example data insertion
session.add(Recipe(title="Pancakes", instructions="Mix ingredients and cook."))
session.commit()

# Querying the instance
r = session.query(Recipe).first()

# Accessing the nth column value (0-indexed)
n = 2
nth_column_value = list(r.__dict__.values())[n]
print(nth_column_value)  # Output will be the 'instructions'
