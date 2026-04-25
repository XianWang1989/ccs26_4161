
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample input
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenizing and tagging the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Defining the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""

# Creating a chunk parser
chunk_parser = RegexpParser(grammar)

# Parsing the tagged sentence
tree = chunk_parser.parse(tagged)

# Displaying the chunked tree
print(tree)

# Drawing the tree (optional, for visualization)
# tree.draw()
