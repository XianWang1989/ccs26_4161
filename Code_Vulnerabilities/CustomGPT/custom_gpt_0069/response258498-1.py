
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Creating a new SQLite database (just for example)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding an example recipe
new_recipe = Recipe(title="Pasta", instructions="Boil water and cook pasta.")
session.add(new_recipe)
session.commit()

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column (in this case, 2nd column which is `instructions`)
def get_nth_column(instance, n):
    # Get the keys of the instance's __dict__ as a list
    keys = list(instance.__dict__.keys())
    # Return the nth attribute value (adjusting for _sa_instance_state)
    return getattr(instance, keys[n + 1]) if n < len(keys) - 1 else None

# Example usage
nth_value = get_nth_column(r, 1)  # This will return r.instructions
print(nth_value)  # Output: Boil water and cook pasta.
