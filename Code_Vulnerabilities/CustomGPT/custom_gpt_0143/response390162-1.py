
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by sam mendes"

# Tokenize and POS tag the text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Defining the grammar for the chunker
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                              # Media NPs
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}                     # Relation verbs leading to NPs
  ENTITY: {<NN.*>}                                        # Entity NPs
  DIRECTED: {<VBN><IN><ENTITY>}                           # "Directed by" structure
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged words
chunked = chunk_parser.parse(tagged)

# Display the result
print(chunked)

# Optional: Draw the chunk tree
chunked.draw()
