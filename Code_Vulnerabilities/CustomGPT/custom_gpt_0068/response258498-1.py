
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setup SQLAlchemy and create a Recipe model
Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite database in memory (for example purposes)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a recipe for querying
new_recipe = Recipe(title='Spaghetti', instructions='Boil water, cook pasta.')
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Function to get nth column value
def get_nth_column(instance, n):
    return list(instance.__table__.columns)[n].name, getattr(instance, list(instance.__table__.columns)[n].name)

# Access nth column, for example the 2nd column (instructions)
column_index = 2
column_name, column_value = get_nth_column(r, column_index)
print(f"{column_name}: {column_value}")
