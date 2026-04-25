
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Define your grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Chunk media phrases
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}            # Chunk relations followed by media
    ENTITY: {<NN.*>}                               # Chunk single entities
"""

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence.lower())  # Convert to lowercase for consistency
tagged = pos_tag(tokens)

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence to extract chunks
parsed_tree = chunk_parser.parse(tagged)

# Print the resulting tree
print(parsed_tree)

# Visualize the chunk tree
parsed_tree.draw()
