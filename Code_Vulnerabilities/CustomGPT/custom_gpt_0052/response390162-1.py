
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                # Noun phrases
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}       # Verbs followed by noun phrases
  ENTITY: {<NN.*>}                          # Single nouns
"""

# Create a chunk parser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged words
chunked = chunk_parser.parse(tagged)

# Display the chunks
print(chunked)

# Drawing the parse tree (optional)
chunked.draw()
