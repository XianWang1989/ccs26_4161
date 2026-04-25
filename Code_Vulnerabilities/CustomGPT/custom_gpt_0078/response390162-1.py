
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample text
text = "Adventure movies between 2000 and 2015 featuring performances by Daniel Craig"

# Tokenize and POS tagging
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
tree = chunk_parser.parse(tagged)

# Print the chunked tree
print(tree)

# Method to extract specific chunks
def extract_chunks(tree):
    for subtree in tree.subtrees():
        if subtree.label() in ["MEDIA", "RELATION", "ENTITY"]:
            print(subtree)

extract_chunks(tree)
