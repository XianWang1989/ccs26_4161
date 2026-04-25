
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example SQLAlchemy setup (replace with your own database URL)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example entry
new_recipe = Recipe(title="Pancakes", instructions="Mix and cook.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column (e.g., 0 for 'id', 1 for 'title', 2 for 'instructions')
n = 2  # For instructions
column_value = list(r.__dict__.items())[n][1]
print(column_value)  # Outputs: Mix and cook.
