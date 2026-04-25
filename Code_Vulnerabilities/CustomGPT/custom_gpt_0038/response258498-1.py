
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a recipe for demonstration
session.add(Recipe(title='Pancakes', instructions='Mix ingredients and fry.'))
session.commit()

# Querying the Recipe
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # For example, to get 'instructions'
nth_column_value = getattr(r, r.__table__.columns.keys()[n])
print(nth_column_value)  # Output: Mix ingredients and fry.
