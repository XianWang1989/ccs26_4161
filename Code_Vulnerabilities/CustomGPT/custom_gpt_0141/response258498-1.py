
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

    def __getitem__(self, index):
        # Get the list of column names
        column_names = list(self.__table__.columns.keys())
        if index < len(column_names):
            # Return the value of the nth column
            return getattr(self, column_names[index])
        else:
            raise IndexError("Index out of range.")

# Example setup (requires a database setup)
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite for example
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Sample data
new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
try:
    print(r[0])  # Accessing the 'id'
    print(r[1])  # Accessing the 'title'
    print(r[2])  # Accessing the 'instructions'
except IndexError as e:
    print(e)
