
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the database engine and session
engine = create_engine('sqlite:///:memory:')  # Example with an in-memory SQLite database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add an example Recipe
new_recipe = Recipe(title='Pancakes', instructions='Mix ingredients and cook.')
session.add(new_recipe)
session.commit()

# Query the recipe
r = session.query(Recipe).first()

# Accessing the nth column (0-indexed)
n = 2  # For example, to access instructions (index 2)
column_name = r.__table__.columns.keys()[n]  # Get the nth column name
value = getattr(r, column_name)  # Get the value of the nth column

print(f"The value of the {n}th column (i.e., {column_name}): {value}")
