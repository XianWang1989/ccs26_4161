
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    instructions = Column(Text)

# Assuming you have a Recipe instance `r`
r = Recipe(id=1, title='Pasta', instructions='Boil water and add pasta.')

# To access the nth column value (e.g., instructions is the second column)
n = 2  # 0-based index
column_value = list(r.__dict__.values())[n]

print(column_value)  # This will print 'Boil water and add pasta.'
