
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database (replace with your database URL)
engine = create_engine('sqlite:///:memory:')  # In-memory database for example
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Creating an example recipe
new_recipe = Recipe(title='Pasta', instructions='Boil water and cook pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # For example, to get the 'instructions' column
columns = list(Recipe.__table__.columns)  # List of columns
nth_column_value = getattr(r, columns[n].name)

# Output the nth column value
print(nth_column_value)  # This will print 'Boil water and cook pasta.'
