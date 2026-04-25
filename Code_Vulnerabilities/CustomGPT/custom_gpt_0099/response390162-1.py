
import nltk
from nltk import pos_tag, tokenize
from nltk.chunk import RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize the phrase
tokens = nltk.word_tokenize(phrase)
tagged_tokens = pos_tag(tokens)

# Define the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Media noun phrase
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}            # Verb followed by noun phrase
    ENTITY: {<NN.*>}                               # Simple noun
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the resulting chunk tree
print(chunked)

# Draw the tree if needed (requires a GUI environment)
# chunked.draw()
