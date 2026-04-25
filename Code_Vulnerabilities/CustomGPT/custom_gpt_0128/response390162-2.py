
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                 # Chunk for media entities
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}        # Chunk for relationships 
  ENTITY: {<NN.*>}                            # Chunk for entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Apply chunking
parsed_tree = chunk_parser.parse(tagged)

# Print the result
print(parsed_tree)

# Optionally, visualize the tree
# parsed_tree.draw()
