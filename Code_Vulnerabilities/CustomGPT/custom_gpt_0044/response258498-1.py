
from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite database and session for demonstration
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example data
new_recipe = Recipe(title='Pancakes', instructions='Mix and cook.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Function to get the nth column value
def get_nth_column(instance, n):
    column_names = instance.__mapper__.columns
    return getattr(instance, list(column_names)[n])

# Access the nth column (e.g., instructions, which is the second column)
nth_value = get_nth_column(r, 2)  # 0: id, 1: title, 2: instructions
print(nth_value)  # Output: 'Mix and cook.'
