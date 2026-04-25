
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                         # Media noun phrases
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}                 # Relations based on verbs and NPs
  ENTITY: {<NN.*>}                                   # Entities
"""

# Create a RegexpParser
chunker = RegexpParser(grammar)

# Perform chunking
chunked = chunker.parse(tagged_tokens)

# Display the chunked structure
print(chunked)

# Visualize the chunked structure (optional)
chunked.draw()
