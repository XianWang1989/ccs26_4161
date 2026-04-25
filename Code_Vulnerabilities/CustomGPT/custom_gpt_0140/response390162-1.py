
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Step 1: Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Step 2: Define the chunk grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""

# Step 3: Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Step 4: Parse the tagged tokens
chunked = chunk_parser.parse(tagged)

# Step 5: Print the resulting chunks
print(chunked)

# Optionally, visualize the parse tree
chunked.draw()
