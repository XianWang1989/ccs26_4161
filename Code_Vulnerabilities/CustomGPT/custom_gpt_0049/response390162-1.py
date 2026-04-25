
import nltk
from nltk import RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the phrase
tokens = nltk.word_tokenize(phrase)
tagged = nltk.pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                         # Media (Noun Phrase)
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}                # Relation (Verb followed by Noun Phrase)
  ENTITY: {<NN.*>}                                   # Entity (Noun)
"""

# Create a chunk parser with your grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged)

# Print the chunked result
print(chunked)

# To draw the chunk tree (optional)
# chunked.draw()
