
import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenization and POS tagging
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}            # Noun phrases potentially starting with a determiner and adjectives
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}    # Verbs followed by noun phrases
  ENTITY: {<NN.*>}                      # Generic entity chunk
"""

# Create a chunk parser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Apply the chunk parser
chunked = chunk_parser.parse(tagged)

# Print the chunked output
print(chunked)

# Visualize the chunking
chunked.draw()
