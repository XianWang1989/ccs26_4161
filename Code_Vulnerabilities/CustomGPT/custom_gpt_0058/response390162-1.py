
import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize, pos_tag

# Sample input text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by someone"

# Tokenize and tag the input text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define your grammar for chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}              # Chunk media terms
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}      # Chunk relations with an optional media
    ENTITY: {<NN.*>}                        # Chunk entities
    """

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged words
chunked = chunk_parser.parse(tagged)

# Show the result
print(chunked)

# Optional: Draw the tree structure
chunked.draw()
