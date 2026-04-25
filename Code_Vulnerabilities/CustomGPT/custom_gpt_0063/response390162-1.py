
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the words
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define a cascaded grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                         # Chunk sequences for MEDIA
    RELATION: {<VB.*>}{<DT>?<JJ>*<NN.*>+}              # Chunk verbs and following noun phrases for RELATION
    ENTITY: {<NN.*>}                                    # Chunk individual nouns for ENTITY
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the sentence
result = chunk_parser.parse(tagged)

# Print the chunked result
print(result)

# Draw the tree (optional)
result.draw()
