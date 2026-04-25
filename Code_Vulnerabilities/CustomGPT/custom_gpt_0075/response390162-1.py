
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenization and Part-of-Speech tagging
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the chunking grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media chunk
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}              # Relation chunk
    ENTITY: {<NN.*>}                                # Entity chunk
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Display the chunked sentence
print(chunked)

# Draw the chunk tree (optional)
chunked.draw()
