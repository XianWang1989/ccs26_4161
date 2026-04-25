
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Define your input phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by Daniel Craig"

# Tokenize the sentence and tag parts of speech
tokenized_sentence = word_tokenize(sentence)
tagged_sentence = pos_tag(tokenized_sentence)

# Define the chunk grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                          # Media chunk
  RELATION: {<VB.*> <DT>?<JJ>*<NN.*>+}               # Relation chunk
  ENTITY: {<NN.*>}                                   # Entity chunk
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked_tree = chunk_parser.parse(tagged_sentence)

# Draw or print the result
print(chunked_tree)
chunked_tree.pretty_print()

# To extract specific words, you can traverse the parse tree
for subtree in chunked_tree.subtrees():
    if subtree.label() == 'RELATION':
        print("Found RELATION:", " ".join(word for word, pos in subtree.leaves()))
