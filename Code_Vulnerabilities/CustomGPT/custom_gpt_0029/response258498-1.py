
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (create an SQLite memory database for demonstration)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add example data
new_recipe = Recipe(title="Pancakes", instructions="Mix ingredients and cook.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column (for instructions)
n = 2  # For example, getting the 'instructions'
nth_column_value = getattr(r, r.__mapper__.columns[n].name)

print(nth_column_value)  # Output: Mix ingredients and cook.
