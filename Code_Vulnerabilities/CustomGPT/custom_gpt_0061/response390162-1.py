
import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}              # Media noun phrases
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}    # Relations with media
  ENTITY: {<NN.*>}                        # Entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunked = chunk_parser.parse(tagged)

# Display the result
print(chunked)

# Optionally, for a more visual output
chunked.draw()
