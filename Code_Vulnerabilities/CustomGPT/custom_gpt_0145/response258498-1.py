
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup for SQLAlchemy
engine = create_engine('sqlite:///:memory:')  # using in-memory SQLite for demonstration
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water, cook pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Function to get the nth column value
def get_nth_column_value(instance, n):
    column_name = instance.__table__.columns.keys()[n]
    return getattr(instance, column_name)

# Example usage
nth_value = get_nth_column_value(r, 2)  # Gets the value of 'instructions'
print(nth_value)  # Output: Boil water, cook pasta.
