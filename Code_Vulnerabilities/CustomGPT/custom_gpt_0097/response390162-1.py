
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
result = chunk_parser.parse(tagged)

# Print the resulting tree
print(result)

# Optionally, you can visualize the tree
result.draw()
