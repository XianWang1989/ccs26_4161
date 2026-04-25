
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (replace with your actual database URL)
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite for demonstration
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
session.add(Recipe(title="Pasta", instructions="Boil water and cook pasta."))
session.commit()

# Querying the Recipe instance
r = session.query(Recipe).first()

# Accessing the nth column value (0-based index)
def get_nth_column(instance, n):
    return list(instance.__dict__.values())[n]

# Example usage
nth_value = get_nth_column(r, 2)  # Access instructions column (index 2)
print(nth_value)
