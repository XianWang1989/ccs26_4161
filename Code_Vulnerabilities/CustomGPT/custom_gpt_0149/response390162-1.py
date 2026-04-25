
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Input phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and part-of-speech tagging
tokens = word_tokenize(phrase)
tagged_tokens = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA:       {<DT>?<JJ>*<NN.*>+}                      # Media noun phrase
  RELATION:    {<V.*>{<DT>?<JJ>*<NN.*>+}}               # Relation structure
  ENTITY:      {<NN.*>}                                  # Entity
"""

# Create a parser with the defined grammar
chunker = RegexpParser(grammar)

# Perform chunking
chunked = chunker.parse(tagged_tokens)

# Display the chunked structure
print(chunked)

# Optional: draw the tree structure
chunked.draw()
