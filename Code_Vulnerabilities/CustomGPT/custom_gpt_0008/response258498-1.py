
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup (replace with your actual database URI)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Insert example data
session.add(Recipe(title="Pasta", instructions="Boil water and cook pasta."))
session.commit()

# Query an instance
r = session.query(Recipe).first()

# Accessing the nth column value
n = 2  # For example, to access the 'instructions' column
nth_value = getattr(r, r.__table__.columns.keys()[n])  # 0-based index

print(nth_value)  # Output: Boil water and cook pasta.
