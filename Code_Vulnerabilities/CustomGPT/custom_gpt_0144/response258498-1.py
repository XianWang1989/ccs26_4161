from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Example setup
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample recipe
session.add(Recipe(title='Pancakes', instructions='Mix and fry.'))
session.commit()

# Fetch an instance
r = session.query(Recipe).first()

# Get the nth column value, e.g., n=2 for 'instructions'
n = 2
columns = list(Recipe.__table__.columns)
column_name = columns[n].name
value = getattr(r, column_name)

print(f"The {n}th column ({column_name}) has value: {value}")
