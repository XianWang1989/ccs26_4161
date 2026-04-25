
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                          # Media entities
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}                # Relationships
  ENTITY: {<NN.*>}                                    # Entities
  PP: {<IN><MEDIA>}                                  # Preposition Phrase with MEDIA
  CLAUSE: {<ENTITY><RELATION>}                       # Clause structure with ENTITY and RELATION
"""

# Create a chunker
chunker = RegexpParser(grammar)

# Parse the sentence
chunked = chunker.parse(tagged)

# Display the chunked result
print(chunked)

# Optionally, visualize the tree structure
chunked.pretty_print()
