
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite database in memory (for illustration)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
session.add(Recipe(title="Pasta", instructions="Boil water, add pasta."))
session.commit()

# Query the first recipe
r = session.query(Recipe).first()

# Access the nth column dynamically
def get_nth_column(instance, n):
    return getattr(instance, instance.__table__.columns.keys()[n])

# Example: Get the 2nd column (instructions)
nth_value = get_nth_column(r, 2)
print(nth_value)  # Output: Boil water, add pasta.
