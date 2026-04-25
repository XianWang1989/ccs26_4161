
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the chunk grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                          # Media noun phrases
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}                # Relations (verbs followed by noun phrases)
    ENTITY: {<NN.*>}                                   # Entities
    """

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Display the resulting structure
print(chunked)

# Optionally visualize the parsed tree
chunked.draw()
