
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Set up the database connection (replace with your DB URL)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(new_recipe)
session.commit()

# Querying the first recipe
r = session.query(Recipe).first()

# Accessing the nth column value
n = 1  # Change this to get the nth column (0 for 'id', 1 for 'title', 2 for 'instructions')
nth_column_value = getattr(r, r.__table__.columns.values()[n].name)

print(f"The value of the {n}th column is: {nth_column_value}")
