
import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the words
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define the grammar for the cascading chunker
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}            # Media phrases
  RELATION: {<VB.*>{<DT>?<JJ>*<NN.*>+}} # Relations with entities
  ENTITY: {<NN.*>}                       # Entities
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged text
parsed = chunk_parser.parse(tagged)

# Print the result
print(parsed)

# Draw the parse tree (optional)
parsed.draw()
