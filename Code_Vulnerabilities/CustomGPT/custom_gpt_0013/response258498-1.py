
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example for creating a session (adapt the connection string as necessary)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe
new_recipe = Recipe(title='Spaghetti', instructions='Boil water, cook pasta.')
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column value
def get_nth_column(instance, n):
    return getattr(instance, instance.__mapper__.columns.keys()[n])

# Example usage
nth_value = get_nth_column(r, 2)  # n=2 for r.instructions
print(nth_value)  # Output: Boil water, cook pasta.
