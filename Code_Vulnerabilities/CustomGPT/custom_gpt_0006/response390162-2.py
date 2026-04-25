
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.*>}{<DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunked = chunk_parser.parse(tagged)

# Function to display chunks
def display_chunks(chunked):
    for subtree in chunked.subtrees():
        print(subtree)

# Display the resulting chunks
display_chunks(chunked)
