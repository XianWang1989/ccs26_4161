
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar with multiple chunking rules
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}               # Chunk media nouns
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}       # Chunk verbs and their noun phrases
    ENTITY: {<NN.*>}                          # Chunk entities
"""

# Create a RegexpParser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunks = chunk_parser.parse(tagged)

# Display the chunks
print(chunks)

# Draw the chunk tree
chunks.draw()
