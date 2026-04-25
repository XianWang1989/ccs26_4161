
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Create an SQLite database in memory for demonstration purposes
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding a sample recipe to the database
new_recipe = Recipe(title="Pasta", instructions="Boil the water.")
session.add(new_recipe)
session.commit()

# Function to get the nth column value
def get_nth_column(instance, n):
    # Get the mapping information for the instance's class
    mapped_class = mapper(instance.__class__)
    column_names = [prop.key for prop in mapped_class.iterate_properties if isinstance(prop, Column)]

    # Check if n is valid
    if n < len(column_names):
        return getattr(instance, column_names[n])
    else:
        return None

# Example usage
r = session.query(Recipe).first()  # Assuming there's at least one record
nth_value = get_nth_column(r, 1)   # Get the value of the 'title' column (index 1)
print(f"The nth column value is: {nth_value}")  # Output: The nth column value is: Pasta
