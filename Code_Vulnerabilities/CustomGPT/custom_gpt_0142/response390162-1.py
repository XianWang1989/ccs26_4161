
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar for cascading chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}         # Chunk sequences of DT, JJ, NN
    RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}  # Chunk verbs followed by NPs
    ENTITY: {<NN.*>}                   # Chunk Nouns
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
parsed_tree = chunk_parser.parse(tagged_tokens)

# Display the parsed tree
print(parsed_tree)

# To visualize the parsed tree
parsed_tree.draw()
