
import nltk
from nltk import pos_tag, word_tokenize

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Part-of-speech tagging
tagged = pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}             # Chunk sequences of DT, JJ, NN
  RELATION: {<VB.*>(<DT>?<JJ>*<NN.*>+)}  # Verbs followed by an NP
  ENTITY: {<NN.*>}                       # Single noun
"""

# Create a chunk parser
chunk_parser = nltk.RegexpParser(grammar)

# Parse the tagged sentence
parsed_tree = chunk_parser.parse(tagged)

# Display the parsed structure
print(parsed_tree)

# Draw the tree (uncomment below to visualize)
# parsed_tree.draw()
