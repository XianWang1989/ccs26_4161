
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Example sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by some director"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the chunk grammar with cascading rules
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                   # Media noun phrases
  RELATION: {<V.*> <DT>?<JJ>*<NN.*>+}          # Verbs followed by NP
  ENTITY: {<NN.*>}                             # Entities
  """

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunks = chunk_parser.parse(tagged)

# Print the resulting chunk tree
print(chunks)

# Draw the tree (optional, requires GUI backend)
chunks.draw()
