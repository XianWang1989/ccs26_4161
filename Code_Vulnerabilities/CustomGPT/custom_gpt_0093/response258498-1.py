
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Assuming you've set up your database connection
engine = create_engine('sqlite:///:memory:')  # Example SQLite in-memory DB
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water, cook pasta.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing nth column value (0-based index)
columns = [r.id, r.title, r.instructions]
n = 2  # for example, to get the 'instructions' column
nth_value = columns[n]

print(f"The {n + 1}th column value is: {nth_value}")
