
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite database (for example)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example usage
# Adding a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water and add pasta.')
session.add(new_recipe)
session.commit()

# Querying the first recipe
r = session.query(Recipe).first()

# Accessing the nth column (e.g., 1st column corresponds to title)
n = 1  # for example
nth_column_value = getattr(r, r.__table__.columns.keys()[n])
print(nth_column_value)  # Outputs: 'Pasta'
