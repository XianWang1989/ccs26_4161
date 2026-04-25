
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define a cascading grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}               # Media nouns
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}      # Relations with media nouns
    ENTITY: {<NN.*>}                         # General entities
"""

# Create a RegexpParser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunks = chunk_parser.parse(tagged_tokens)

# Print the chunk tree
print(chunks)

# You can visualize the chunk tree (optional)
chunks.draw()
