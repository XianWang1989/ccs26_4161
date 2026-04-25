
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define grammar for the cascaded chunker
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}              # Chunk sequences of DT, JJ, NN
    RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}    # Chunk verbs and their arguments followed by media
    ENTITY: {<NN.*>}                        # Single noun entities
"""

# Create RegexpParser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked_result = chunk_parser.parse(tagged_tokens)

# Display the chunked result
print(chunked_result)

# Optional: To visualize the result (Requires matplotlib)
# from nltk import Tree
# chunked_result.draw()
