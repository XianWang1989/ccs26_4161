
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Step 1: Define your sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Step 2: Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Media definition
  RELATION: {<VB.*>}{<DT>?<JJ>*<NN.*>+}          # Relation verbs followed by media
  ENTITY: {<NN.*>}                               # Entities
"""

# Step 3: Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Step 4: Parse the sentence
tree = chunk_parser.parse(tagged)

# Step 5: Print the resulting chunks
print(tree)

# Optional: Draw the tree if you have a graphical backend
# tree.draw()
