
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example usage
if __name__ == "__main__":
    # Set up the database (replace with your own database URI)
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a sample recipe
    new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
    session.add(new_recipe)
    session.commit()

    # Query the recipe
    r = session.query(Recipe).first()

    # Access the nth column (e.g., 2nd column: instructions)
    n = 2  # Change this to access different columns
    nth_value = list(r.__dict__.values())[n]

    print(nth_value)  # Output: Boil water and cook pasta.
