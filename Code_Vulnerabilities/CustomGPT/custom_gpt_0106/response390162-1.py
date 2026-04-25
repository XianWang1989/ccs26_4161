
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the chunk grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                   # Media noun phrases
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}         # Relations after a verb
    ENTITY: {<NN.*>}                             # General entity
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Chunk the tagged tokens
result = chunk_parser.parse(tagged_tokens)

# Display the chunks
print(result)

# Draw the tree structure (if you have a graphical backend)
# result.draw()
