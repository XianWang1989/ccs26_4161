
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Assuming your engine and session are set up
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create and add a sample Recipe instance to the session
new_recipe = Recipe(title="Pasta", instructions="Boil water, add pasta.")
session.add(new_recipe)
session.commit()

# Retrieve the instance
r = session.query(Recipe).first()

# To access the nth column value, you can use:
n = 2  # Specify which column you want to access (0 for 'id', 1 for 'title', 2 for 'instructions')
column_name = list(r.__table__.columns.keys())[n]
column_value = getattr(r, column_name)

print(f"The {n}th column value is: {column_value}")
