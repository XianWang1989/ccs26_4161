
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged_sequence = pos_tag(tokens)

# Define the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}               # Relation
    ENTITY: {<NN.*>}                                 # Entity
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Apply the chunk parser
chunks = chunk_parser.parse(tagged_sequence)

# Display the chunked result
print(chunks)

# Optionally, visualize the chunks
chunks.draw()
