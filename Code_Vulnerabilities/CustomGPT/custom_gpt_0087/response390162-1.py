
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag parts of speech
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar for the cascading chunker
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                          # Media phrase
    RELATION: {<V.*> <DT>?<JJ>*<NN.*>+}                # Relation phrase
    ENTITY: {<NN.*>}                                   # Entity
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the chunked tree
print(chunked)

# Optionally, visualize the chunk tree
chunked.draw()
