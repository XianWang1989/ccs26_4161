
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Define your grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media entities
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}              # Relations (verbs followed by NPs)
    ENTITY: {<NN.*>}                                 # Any noun as an entity
"""

# Instantiate the chunk parser
chunk_parser = RegexpParser(grammar)

# Example phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Perform chunking
chunks = chunk_parser.parse(tagged_tokens)

print(chunks)

# Draw the tree structure (optional)
chunks.draw()
