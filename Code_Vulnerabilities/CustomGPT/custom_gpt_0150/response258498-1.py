
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setting up the database and session
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite for example
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding example data
session.add(Recipe(title='Pasta', instructions='Boil water and add pasta.'))
session.commit()

# Querying a Recipe instance
r = session.query(Recipe).first()

# Accessing the nth column (e.g., 2nd column which is instructions)
n = 2  # For example, to get the second column
column_value = list(r.__dict__.values())[n]

print(column_value)  # Output: 'Boil water and add pasta.'
