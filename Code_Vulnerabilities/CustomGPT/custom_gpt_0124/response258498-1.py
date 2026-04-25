
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database (for demonstration purposes)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add an example recipe
session.add(Recipe(title='Pasta', instructions='Boil water, add pasta.'))
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Get the nth column value (e.g., 2nd column, which is 'instructions')
n = 2  # Change this to the desired column index (0-based)
column_name = Recipe.__table__.columns.keys()[n]
nth_value = getattr(r, column_name)

print(nth_value)  # Output: Boil water, add pasta.
