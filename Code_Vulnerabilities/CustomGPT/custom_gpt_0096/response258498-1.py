
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite engine and a session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example: adding a recipe
session.add(Recipe(title="Pasta", instructions="Boil water, add pasta."))
session.commit()

# Querying the recipe instance
r = session.query(Recipe).first()

# Getting the nth column (e.g., instructions)
def get_nth_column(instance, n):
    return getattr(instance, instance.__table__.columns.keys()[n])

# Usage
nth_column_value = get_nth_column(r, 2)  # 2 corresponds to `instructions`
print(nth_column_value)  # Output: Boil water, add pasta.
