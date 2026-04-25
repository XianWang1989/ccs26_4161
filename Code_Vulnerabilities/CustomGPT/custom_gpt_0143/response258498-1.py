
from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Setup SQLite in-memory database for demonstration
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water, cook pasta.')
session.add(new_recipe)
session.commit()

# Query a recipe instance
r = session.query(Recipe).first()

# Accessing the nth column value (for example, the second column)
n = 2  # Column index (0-based), where 1 corresponds to 'title' and 2 to 'instructions'
column_value = list(r.__dict__.values())[n]

print(column_value)  # Output: Boil water, cook pasta.
